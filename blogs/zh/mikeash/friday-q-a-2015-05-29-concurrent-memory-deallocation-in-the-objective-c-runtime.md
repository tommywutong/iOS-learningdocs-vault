---
title: 'Friday Q&A 2015-05-29：Objective-C 运行时的并发内存释放'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cae950de9698cb90'
translated: true
---

> 原文：[Friday Q&A 2015-05-29: Concurrent Memory Deallocation in the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html)　·　mikeash.com Friday Q&A

发表于 2015-06-05 13:06 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[I Do Not Agree To Your Terms](https://www.mikeash.com/pyblog/i-do-not-agree-to-your-terms.html)
上一篇：[Friday Q&A 2015-05-01: Fuzzing with afl-fuzz](https://www.mikeash.com/pyblog/friday-qa-2015-05-01-fuzzing-with-afl-fuzz.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-05-29：Objective-C 运行时的并发内存释放

作者：[Mike Ash](https://www.mikeash.com/)

**消息发送概念**
`objc_msgSend` 的工作方式是：查找被发送方法对应的实现（method implementation），然后跳转过去。从概念上讲，查找方法的过程是这样的：

```
    IMP lookUp(id obj, SEL selector) {
        Class c = object_getClass(obj);

        while(c) {
            for(int i = 0; i < c->numMethods; i++) {
                Method m = c->methods[i];
                if(m.selector == selector) {
                    return m.imp;
                }
            }

            c = c->superclass;
        }

        return _objc_msgForward;
    }
```

为了保护无辜者，一些名称已做更改。如果你对真实代码感兴趣，请查看 Objective-C 运行时源代码：

[http://www.opensource.apple.com/source/objc4/](http://www.opensource.apple.com/source/objc4/)

**方法缓存**
大多数 Objective-C 代码中充满了消息发送。如果每次都执行完整的方法查找，速度将慢得令人难以忍受。

解决办法是使用缓存。每个类都附带一个哈希表，它将选择器（selector）映射到方法实现（method implementation）。哈希表的构建是为了最大化读取效率，而 `objc_msgSend` 则使用精心调优的汇编语言代码来快速执行哈希表查找。这使得缓存命中时的消息发送耗时降至个位数纳秒。任何特定消息的首次使用仍然慢得令人难以置信，但之后就快了。

当我们想到缓存时，通常是指容量有限、旨在加速对最近使用的资源进行多次访问的某种机制。例如，你可能缓存从互联网加载的图片，这样连续两次获取就不会重复访问网络。但你也不想占用太多内存，因此可能会限制缓存中同时保存的图片数量，并在缓存填满后有新图片进入时丢弃最旧的图片。

这种方法对许多问题都适用，但可能会带来严重的性能问题。例如，如果你将图片缓存设置为存储 40 张图片，而 App 不断循环使用 41 张图片，那么你的缓存会突然变得毫无用处。

对于自己的 App，我们可以测试和调整缓存来避免这种情况，但 Objective-C 运行时没有这个选项。由于方法缓存对性能至关重要，而且每个条目相对较小，运行时不施加任何大小限制，而是根据需要扩容，以缓存所有已发送的消息。

请注意，缓存*会*被清空；每当可能导致缓存数据失效的事情发生时——例如将新代码加载到进程或修改类的方法列表——相应的缓存会被销毁并允许重新填充。

**调整大小、释放与线程**
调整缓存大小在概念上相当简单。看起来像这样：

```
    bucket_t *newCache = malloc(newSize);
    copyEntries(newCache, class->cache);
    free(class->cache);
    class->cache = newCache;
```

实际上，Objective-C 运行时在这里采取了一个小小的捷径：它甚至不将旧条目复制到新缓存中！毕竟，这只是一个缓存，并且没有*要求*保留其中包含的数据。条目会在消息发送时重新填充。所以实际上只是：

```
    free(class->cache);
    class->cache = malloc(newSize);
```

在单线程环境中，这就足够了，这篇文章也会很短。但 Objective-C 运行时当然必须支持多线程代码，这意味着所有这些代码都必须保证线程安全。任何给定类的缓存都可能被多个线程同时访问，因此这段代码必须小心处理，以保证能够容忍这种情况。

如上文所示，它无法做到这一点。在释放旧缓存和分配新缓存之间有一个时间窗口，在此期间另一个线程可能访问到无效的缓存指针。这可能导致它看到垃圾数据，如果底层内存被取消映射，甚至直接崩溃。

我们该如何解决这个问题？保护这种共享数据的典型方法是使用锁（lock）。代码会变成这样：

```
    lock(class->lock);
    free(class->cache);
    class->cache = malloc(newSize);
    unlock(class->lock);
```

要使其正常工作，所有访问都必须受锁保护，包括读取。这意味着 `objc_msgSend` 必须获取锁、在缓存中查找、然后释放锁。考虑到缓存查找本身只需要几纳秒，每次获取和释放锁会增加*大量*开销。性能影响太大了。

我们可以尝试用其他方式缩小这个时间窗口。例如，如果我们*先*分配并赋值新缓存，*然后*再释放旧缓存呢？

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    free(oldCache);
```

这有所帮助，但未解决问题。另一个线程可能获取了旧缓存指针，然后在访问其内容之前被系统抢占。在另一个线程再次运行之前，旧缓存可能已被销毁，导致与之前相同的问题。

如果我们加入一个延时呢？类似于：

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    after(5 /* 秒 */, ^{
        free(oldCache);
    });
```

这几乎肯定能奏效。但仍然可以想象，一个线程恰好在那个节骨眼上被抢占，并且被抢占足够长的时间，使得五秒的延时先触发。这使得崩溃极不可能发生，但并未完全消除。

与其使用任意的延时，不如等待时间窗口确认安全？让我们在 `objc_msgSend` 中添加一个计数器，使其看起来像这样：

```
    gInMsgSend++;
    lookUpCache(class->cache);
    gInMsgSend--;
```

一个合适的线程安全版本需要使用原子操作（atomics）来处理计数器，并使用适当的内存屏障来确保相关的加载/存储正确可见。就本文而言，请假设这些内容都存在。

有了计数器，缓存重新分配看起来像这样：

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);
    while(gInMsgSend)
        ; // 自旋
    free(oldCache);
```

注意，无需*阻塞* `objc_msgSend` 的执行来使其正常工作。一旦缓存释放代码确信在替换缓存指针之后的任何特定时刻，没有任何线程在 `objc_msgSend` 中，它就可以放心地释放旧缓存。在旧缓存指针被释放的过程中，另一个线程可能调用 `objc_msgSend`，但这个新调用不可能再看到旧指针，因此是安全的。

自旋（spinning）效率低下且不优雅。释放这些缓存并不特别紧急。释放内存是好事，但如果需要一些时间也不是大问题。与其自旋，不如维护一个未释放缓存的列表，每次释放某些内容时，尝试清除所有待处理的缓存：

```
    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);

    append(gOldCachesList, oldCache);
    if(!gInMsgSend) {
        for(cache in gOldCachesList) {
            free(cache);
        }
        gOldCachesList.clear();
    }
```

如果消息发送正在进行中，则不会立即释放旧缓存，但这没问题。下一次经过时会清除，或者再下一次，或者在未来*某个*时刻。

这个版本与 Objective-C 运行时的实际做法非常接近。

**零成本标志**
这里存在两个交互部分之间的极端不对称。`objc_msgSend` 端每秒可能运行数百万次，并且必须尽可能快。单次调用的最佳运行时间仅为几纳秒。另一方面，调整缓存大小是一个罕见操作，随着 App 继续运行，它通常会变得越来越少见。一旦 App 达到稳定状态（不再加载新代码或编辑消息列表，并且缓存已达到所需大小），这种情况永远不会发生。在此之前，随着缓存增长到所需大小，它可能发生几百或几千次，但与 `objc_msgSend` 相比，它极为罕见，对性能的敏感度也低得多。

由于这种不对称性，最好在消息发送端尽可能少做事情，即使这会使缓存释放部分慢得多。在 `objc_msgSend` 中节省一个 CPU 周期，即使以每次缓存释放操作花费百万个 CPU 周期为代价，这也是净收益，而且是巨大的收益。

即使是全局计数器也代价过高。这会在 `objc_msgSend` 中增加两次额外的内存访问，而这仍然会增加大量开销。它们需要是原子的并使用内存屏障，这使得情况更糟。幸运的是，Objective-C 运行时有一种技术，可以将 `objc_msgSend` 端的成本降至零，代价是使缓存释放代码慢得多。

假设的全局计数器的目的是跟踪任何线程何时位于特定代码区域内。线程已经有了一些跟踪它们当前正在运行什么代码的东西：程序计数器（program counter）。这是 CPU 的一个寄存器，用于跟踪当前指令的内存地址。我们可以检查每个线程的程序计数器，看它是否在 `objc_msgSend` 中，而不是使用全局计数器。如果所有线程都在外面，那么释放旧缓存是安全的。下面是实现看起来的样子：

```
    BOOL ThreadsInMsgSend(void) {
        for(thread in GetAllThreads()) {
            uintptr_t pc = thread.GetPC();
            if(pc >= objc_msgSend_startAddress && pc <= objc_msgSend_endAddress) {
                return YES;
            }
        }
        return NO;
    }

    bucket_t *oldCache = class->cache;
    class->cache = malloc(newSize);

    append(gOldCachesList, oldCache);
    if(!ThreadsInMsgSend()) {
        for(cache in gOldCachesList) {
            free(cache);
        }
        gOldCachesList.clear();
    }
```

这样，`objc_msgSend` 就不需要做任何特殊的事情了。它可以直接访问缓存，而无需担心标记该访问。它只是执行：

```
    lookUpCache(class->cache);
```

缓存释放代码效率相当低，因为它需要检查进程中每个线程的状态。但 `objc_msgSend` 的效率与为单线程环境编写时一样高，这是一个非常值得的权衡。这最终是 Apple 运行时代码的工作方式。

**真实代码**
Apple 实现此技术的代码位于 runtime 函数 `_collecting_in_critical` 中，定义在 [objc-cache.mm](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-cache.mm)。

关键的 PC 位置存储在全局变量中：

```
    OBJC_EXPORT uintptr_t objc_entryPoints[];
    OBJC_EXPORT uintptr_t objc_exitPoints[];
```

实际上有多个 `objc_msgSend` 实现（例如用于 `struct` 返回值），内部函数 `cache_getImp` 也直接访问缓存。为了安全地释放缓存，所有这些都需要检查。

该函数本身不带参数，返回 `int`，仅用作布尔标志，指示是否有任何线程位于关键函数之一中：

```
    static int _collecting_in_critical(void)
    {
```

为了集中讨论最精彩的部分，我将跳过该函数中不太有趣的代码片段。如果你想查看整个函数，请参阅 [opensource.apple.com](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-cache.mm)。

获取线程信息的 API 位于 mach 层面。`task_threads` 获取给定任务（task）（mach 中表示进程的术语）中所有线程的列表，此代码使用它来获取自身进程中的线程：

```
        ret = task_threads(mach_task_self(), &threads, &number);
```

这会在 `threads` 中返回一个 `thread_t` 值数组，并在 `number` 中返回线程数量。然后它遍历它们：

```
        for (count = 0; count < number; count++)
        {
```

获取线程的 PC 是在一个单独的函数中完成的，我们稍后会看到：

```
            pc = _get_pc_for_thread (threads[count]);
```

然后它遍历入口和出口点，并将 PC 与每个点进行比较：

```
            for (region = 0; objc_entryPoints[region] != 0; region++)
            {
                if ((pc >= objc_entryPoints[region]) &&
                    (pc <= objc_exitPoints[region]))
                {
                    result = TRUE;
                    goto done;
                }
            }
        }
```

循环之后，它将结果返回给调用者：

```
        return result;
    }
```

`_get_pc_for_thread` 是如何工作的？它是一个相对简单的代码片段，调用 `thread_get_state` 来获取目标线程的寄存器状态。将其放在单独函数中的主要原因是寄存器状态结构是与架构相关的，因为每种架构都有不同的寄存器。这意味着该函数需要为每个支持的架构提供单独的实现，尽管这些实现几乎相同。以下是 `x86-64` 的实现：

```
    static uintptr_t _get_pc_for_thread(thread_t thread)
    {
        x86_thread_state64_t            state;
        unsigned int count = x86_THREAD_STATE64_COUNT;
        kern_return_t okay = thread_get_state (thread, x86_THREAD_STATE64, (thread_state_t)&state, &count);
        return (okay == KERN_SUCCESS) ? state.__rip : PC_SENTINEL;
    }
```

注意，`rip` 是 `x86-64` 上 PC 的寄存器名称；R 代表“寄存器”（Register），IP 代表“指令指针”（Instruction Pointer）。

入口和出口点本身在定义相关函数的汇编语言文件中定义。它们看起来像这样：

```
    .private_extern _objc_entryPoints
    _objc_entryPoints:
        .quad   _cache_getImp
        .quad   _objc_msgSend
        .quad   _objc_msgSend_fpret
        .quad   _objc_msgSend_fp2ret
        .quad   _objc_msgSend_stret
        .quad   _objc_msgSendSuper
        .quad   _objc_msgSendSuper_stret
        .quad   _objc_msgSendSuper2
        .quad   _objc_msgSendSuper2_stret
        .quad   0

    .private_extern _objc_exitPoints
    _objc_exitPoints:
        .quad   LExit_cache_getImp
        .quad   LExit_objc_msgSend
        .quad   LExit_objc_msgSend_fpret
        .quad   LExit_objc_msgSend_fp2ret
        .quad   LExit_objc_msgSend_stret
        .quad   LExit_objc_msgSendSuper
        .quad   LExit_objc_msgSendSuper_stret
        .quad   LExit_objc_msgSendSuper2
        .quad   LExit_objc_msgSendSuper2_stret
        .quad   0
```

`_collecting_in_critical` 的使用方式与上述假设示例非常相似。它在释放剩余缓存垃圾的代码之前被调用。运行时实际上有两种模式：一种是在其他线程位于关键函数中时将垃圾留待下次处理；另一种是在循环中自旋直到安全为止，并始终释放垃圾：

```
    // 将收集操作与 objc_msgSend 及其他缓存读取器同步
    if (!collectALot) {
        if (_collecting_in_critical ()) {
            // objc_msgSend（或其他缓存读取器）当前正在查找缓存，
            // 可能仍在使用一些垃圾。
            if (PrintCaches) {
                _objc_inform ("CACHES: not collecting; "
                              "objc_msgSend in progress");
            }
            return;
        }
    }
    else {
        // 没有借口。
        while (_collecting_in_critical())
            ;
    }

    // 在此处释放垃圾
```

第一种模式（将垃圾留待下次处理）用于正常的缓存调整大小。第二种模式（始终释放垃圾的自旋模式）用于刷新所有类的所有缓存的运行时方法，因为这通常会产生大量垃圾。根据我对代码的检查，这仅在启用将所有消息发送记录到文件的调试日志记录设施时发生。它刷新缓存是因为消息缓存会干扰日志记录。

**结论**
性能与线程安全常常相互矛盾。不同代码部分对共享数据的访问方式往往存在不对称性，这为实现更高效的线程安全提供了可能。一个全局标志或计数器，用于指示何时修改操作不安全，是利用这种不对称性的一种方法。在 Objective-C 运行时中，Apple 更进一步，将每个线程的程序计数器用作隐式指示，表明线程何时正在执行不安全操作。这是一个特例，很难看到该技术还能在其他什么地方有用，但拆解它令人着迷。

今天就到这里。下次再见，带来更多精彩内容。 Friday Q&A 由读者想法驱动，所以如果你有想在这里看到的话题，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在销售收录这些文章的完整书籍！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷本，以及在 iBooks 和 Kindle 上销售。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.html)

添加你的想法，发表评论：

垃圾评论和离题帖子将被删除，恕不另行通知。违规者可能会被我公开羞辱，完全由我自行决定。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
