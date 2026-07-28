---
title: 'Friday Q&A 2010-07-30：CoreFoundation 对象的置零弱引用'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:825dc66eab42d190'
translated: true
---

> 原文：[Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)　·　mikeash.com Friday Q&A

发布于 2010-07-30 19:01 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2010-08-12：实现 NSCoding](https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html)
上一篇文章：[介绍 MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)
标签：[corefoundation](https://www.mikeash.com/pyblog/?tag=corefoundation) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack)

Friday Q&A 2010-07-30：CoreFoundation 对象的置零弱引用

作者：[Mike Ash](https://www.mikeash.com/)

**代码**
和之前一样，你可以从我的公共 Subversion 仓库获取 `MAZeroingWeakRef` 的代码：

```
    svn co http://mikeash.com/svn/ZeroingWeakRef/
```

或者点击上面的链接浏览。如果你上次已经有一个本地副本，请务必更新，因为从那以后我做了大量改动。

**前置阅读**
这篇文章假设你对 CoreFoundation 以及 CF-ObjC 桥接的工作原理有相当好的了解。如果还没有，你可能希望阅读或至少参考 [Friday Q&A 2010-01-22：Toll Free Bridging 内部实现](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)。

**回顾**
置零弱引用（zeroing weak reference）是一种对对象的引用，它不参与保持该对象存活。当目标对象被销毁时，置零弱引用会自动变成 `NULL`。当请求置零弱引用的目标时，调用方保证要么获得一个有效的引用，要么得到 `NULL`。这对于各种用途都很有用，[正如上一篇文章所涵盖的](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)。

为了在 Cocoa 中实现这一点，`MAZeroingWeakRef` 通过动态创建目标类的一个子类并更改目标的类，来覆写目标对象的 `dealloc` 方法。这个被覆写的 `dealloc` 方法会清零指向目标的 `MAZeroingWeakRef` 对象。

如果你就此止步，会存在线程安全和复活（resurrection）方面的问题。想象一个线程对对象的最后一个强引用调用了 `release`，导致它接着调用 `dealloc`。想象在这两个调用之间，另一个线程通过一个置零弱引用访问该对象。由于 `dealloc` 尚未被调用，它返回了一个对该对象的引用。但是，因为 `dealloc` 调用已经准备就绪，`MAZeroingWeakRef` 执行的 `retain/autorelease` 操作无法挽救该对象免于被销毁。灾难！

这个问题通过同时覆写 `release` 来解决。通过在 `release` 中获取一个也在检索置零弱引用目标时使用的锁，可以确保这种复活场景不会发生。

**免费桥接对象（Toll-Free Bridged Objects）**
这个方案对于普通的 Objective-C 对象效果很好，但对于桥接的 CoreFoundation 对象则会严重失败。更改桥接对象的类会导致无限递归。CoreFoundation 函数做的第一件事就是检查被调用对象的类。如果该类不匹配官方的 `NSCF` 类，它会假定这是一个纯 Objective-C 类，并调用等效的 Objective-C 方法。`NSCF` 类上的等效 Objective-C 方法只会调用 CoreFoundation 函数。如此反复，然后崩溃。

在这种情况下，动态子类并非严格必要。我可以改为直接在 `NSCF` 类上交换 `dealloc` 和 `release` 方法，让它们执行我的脏活。这样效率稍低（因为会影响该类的每一个对象，而不仅仅是弱引用的对象），但这应该没问题。

麻烦在于这行不通。如果你对这样一个对象调用 `CFRelease`，它会直接进入该对象的引用计数和释放逻辑，而从不调用 Objective-C 的方法。所以这个方案只能捕获事情的一面，基本上没用。

在经历所有这些之后，我四处寻找解决方案。除非修补 `CFRelease`（我非常不想这样做，尤其是因为这种方法在 iPhone 上无效，在那里修改可执行代码是被禁止的），我想不出任何办法。

我几乎要放弃这个问题，只能认命禁止对 CoreFoundation 对象的弱引用，就在这时我偶然发现了……

**解决方案**
我开始翻阅 CoreFoundation 的源代码（可从 [opensource.apple.com](http://www.opensource.apple.com/) 获取），试图找到一种钩住释放事件的方法，这时我在 `CFRelease` 的代码中偶然发现了这个小宝贝：

```
    void (*func)(CFTypeRef) = __CFRuntimeClassTable[typeID]->finalize;
    if (NULL != func) {
        func(cf);
    }
    // 我们重新检查 lowBits 以查看对象在 finalize 过程中是否被再次 retain。
    // 这允许终结器复活对象，
    // 但主要目的是允许终结器能够管理
    // 从唯一化缓存（uniquing caches）中移除对象，这可能与其他线程产生竞争，
    // 这些线程正在从这些缓存中分配（查找并找到）对象，
    // 那个线程在这种情况下会执行额外的 retain。
    if (isAllocator || OSAtomicCompareAndSwap32Barrier(1, 0, (int32_t *)&((CFRuntimeBase *)cf)->_rc)) {
        goto really_free;
    }
```

关于复活的注释是关键。虽然我无法拦截 `CFRelease` 来消除竞态条件，但我可以检测到它并允许对象复活，这样我就能从这种情况中恢复。我有思路了！

实现这个方案需要覆写 CoreFoundation 的 finalize 函数。CoreFoundation 没有支持这种操作的机制，所以我必须深入 CF 的源代码，并以粗暴的方式切入。这意味着我所做的一切并非完全受支持，并且可能出错，尽管我相信这些东西实际上相当稳定。

**CoreFoundation 类**
CoreFoundation 类只是一个看起来像这样的结构体：

```
    typedef struct __CFRuntimeClass {	// Version 0 struct
        CFIndex version;
        const char *className;
        void (*init)(CFTypeRef cf);
        CFTypeRef (*copy)(CFAllocatorRef allocator, CFTypeRef cf);
        void (*finalize)(CFTypeRef cf);
        Boolean (*equal)(CFTypeRef cf1, CFTypeRef cf2);
        CFHashCode (*hash)(CFTypeRef cf);
        CFStringRef (*copyFormattingDesc)(CFTypeRef cf, CFDictionaryRef formatOptions);	// str with retain
        CFStringRef (*copyDebugDesc)(CFTypeRef cf);	// str with retain
        void (*reclaim)(CFTypeRef cf);
    } CFRuntimeClass;
```

它基本上就是一个表，其中包含一些所有 CF 对象都支持的常见操作的函数指针。所有特定于类的功能都作为函数实现，完全没有动态查找（除了免费桥接支持中提供的东西）。

然后覆写 finalize 函数就变得容易了。首先，使用这个函数查找给定 CF 类型 ID 的 `CFRuntimeClass`：

```
    extern CFRuntimeClass * _CFRuntimeGetClassWithTypeID(CFTypeID typeID);
```

然后我可以用我自己的函数替换 `finalize` 函数指针。我仍然需要调用原始函数，所以我创建了一个自己的表来存储原始函数指针，按 CF 类型 ID 索引：

```
    typedef void (*CFFinalizeFptr)(CFTypeRef);
    static CFFinalizeFptr *gCFOriginalFinalizes;
    static size_t gCFOriginalFinalizesSize;
```

如果你还记得上次，我的工具函数 `CreateCustomSubclass` 负责为给定对象创建一个动态的 Objective-C 子类。原始实现会检查该对象是否是一个桥接的 CoreFoundation 对象，如果是则简单断言。新的实现处理将 `finalize` 函数指针交换到我自定义的函数：

```
    static Class CreateCustomSubclass(Class class, id obj)
    {
        if(IsTollFreeBridged(class, obj))
        {
            CFTypeID typeID = CFGetTypeID(obj);
            CFRuntimeClass *cfclass = _CFRuntimeGetClassWithTypeID(typeID);

            if(typeID >= gCFOriginalFinalizesSize)
            {
                gCFOriginalFinalizesSize = typeID + 1;
                gCFOriginalFinalizes = realloc(gCFOriginalFinalizes, gCFOriginalFinalizesSize * sizeof(*gCFOriginalFinalizes));
            }

            do {
                gCFOriginalFinalizes[typeID] = cfclass->finalize;
            } while(!OSAtomicCompareAndSwapPtrBarrier(gCFOriginalFinalizes[typeID], CustomCFFinalize, (void *)&cfclass->finalize));
            return class;
        }
        else
            // 原始的 ObjC 动态子类创建代码在这里
```

这里没什么太复杂的。第一部分只是获取必要的信息。中间的 `if` 语句处理表太小的情况（进行大小调整）。（CF 类型 ID 是小整数，所以用它们索引的平面数组效果很好。）最后一部分使用原子调用交换原始函数指针，以确保线程安全，以防其他人恰好同时尝试同样的事情。

有了这个改变，`IsTollFreeBridged` 必须 100% 可靠就变得至关重要。旧的实现只是查找以 `NSCF` 开头的类名，这还不够好。我想出了一个完全可靠的测试，使用一个私有的 CoreFoundation Objective-C 类表：

```
    extern Class *__CFRuntimeObjCClassTable;
```

这个表将 CF 类型 ID 映射到 `NSCF` Objective-C 类。检查桥接性质就变成了获取相关对象的类型 ID，获取该类型 ID 的桥接类，然后看对象的类是否匹配：

```
    static BOOL IsTollFreeBridged(Class class, id obj)
    {
        CFTypeID typeID = CFGetTypeID(obj);
        Class tfbClass = __CFRuntimeObjCClassTable[typeID];
        return class == tfbClass;
    }
```

`finalize` 交换重新指向 `CustomCFFinalize`。这个函数简单地通过查看 `CFGetRetainCount` 来检查是否复活，如果尚未发生复活，则清除所有对该对象的弱引用并调用原始的 `finalize` 函数：

```
    static void CustomCFFinalize(CFTypeRef cf)
    {
        WhileLocked({
            if(CFGetRetainCount(cf) == 1)
            {
                ClearWeakRefsForObject((id)cf);
                void (*fptr)(CFTypeRef) = gCFOriginalFinalizes[CFGetTypeID(cf)];
                if(fptr)
                    fptr(cf);
            }
        });
    }
```

简单吧？对吧……？

**复活从死亡中归来**
不幸的是，这里存在一个竞态条件。想象以下序列：

1. **线程 1**
    1. `CFRelease(obj)`
    2. `CFRelease` 调用 `CustomCFFinalize`
    3. 在 `CustomCFFinalize` 开始执行之前，该线程被抢占
2. **线程 2**
    1. `[ref target]` 获取对 `obj` 的引用
    2. `obj` 被 `MAZeroingWeakRef` retain 并 autorelease
    3. 外层的自动释放池被 drain，导致 `CFRelease(obj)`
    4. `CFRelease` 调用 `CustomCFFinalize`
    5. `CustomCFFinalize` 清除弱引用并调用原始的 `finalize`
    6. `CustomCFFinalize` 返回
3. **线程 1**
    1. 在 `CustomCFFinalize` 的开头恢复执行
    2. `CustomCFFinalize` 检查引用计数，仍然是 1
    3. `CustomCFFinalize` 对同一个对象第二次调用原始的 `finalize`
    4. 可怕的火焰崩溃发生

更糟糕的是，即使存在会复活的 finalize 函数，`CFRelease` 本身也不安全。它在 finalize 函数返回后再次检查对象的引用计数。但是，对象可能在此间隙中被复活然后销毁，导致错误的内存访问。为了使其安全，在 `CFRetain` 本身返回之前，我们**不能**允许对象有任何被销毁的可能性。

因此存在一个极其罕见、难以命中，但完全真实的竞态条件，可能导致此代码崩溃。

**黑客等级三**
为了解决这个问题，我将 CoreFoundation 对象分为两类。有些对象是弱引用的目标，其余不是。这有两个目的。首先，它允许我在销毁从未成为弱引用目标的对象时采取快速路径。其次，我可以跟踪引用的对象是否仍有可能被复活。

这是通过简单地维护一个 `CFMutableSet` 来存储被引用的对象来实现的。检查对象的状态就是测试集合成员资格。对象在调用 `RegisterRef` 时被插入集合。当 finalize 在引用计数为 1 时执行时，对象被移除，这确保了它不能再被复活。

新的 `CustomCFFinalize` 然后被分成两部分。如果对象有弱引用，它首先检查引用计数是否为 1，以判断它是否已被复活：

```
static void CustomCFFinalize(CFTypeRef cf)
    {
        WhileLocked({
            if(CFSetContainsValue(gCFWeakTargets, cf))
            {
                if(CFGetRetainCount(cf) == 1)
                {
```

如果引用计数仍然是 1，那么对象没有被复活。然而，销毁它仍然不安全，因为可能有多个线程停在这个位置。相反，代码清除所有弱引用，_retain_ 该对象以故意复活它，然后安排稍后释放它：

```
                    ClearWeakRefsForObject((id)cf);
                    CFSetRemoveValue(gCFWeakTargets, cf);
                    CFRetain(cf);
                    CallCFReleaseLater(cf);
                }
            }
```

如果对象没有弱引用，那么简单地调用原始 finalize 函数，不制造任何麻烦：

```
            else
            {
                void (*fptr)(CFTypeRef) = gCFOriginalFinalizes[CFGetTypeID(cf)];
                if(fptr)
                    fptr(cf);
            }
        });
    }
```

很容易，对吧？但 `CallCFReleaseLater` 函数到底是如何工作的呢？

使用 `autorelease` 可以达到目的，但这是纯粹的 CF 代码，不能保证调用者实际上已经设置了一个自动释放池。想法不错，但就是行不通。

某种在 `CFRelease` 退出时进行钩子的方法会是理想的。但如前所述，根本没有可用的钩子，所以这条路也走不通。

最终，我从 Ed "Master of All Things Arcane" Wynne 那里获得了灵感，指出可以使用一种类似于 Objective-C 运行时中缓存清理方案的完全疯狂的技术来实现。

**疯狂方案**
重新陈述问题：我需要在最初的 `CFRelease` 调用完成后的某个时间对该对象调用 `CFRelease`。由于无法在发出原始 `CFRelease` 调用的线程上安排此事，我利用了一个后台线程。

后台线程如何知道原始的 `CFRelease` 调用何时完成？

一个线程有可能访问另一个线程的 PC（程序计数器，当前执行指令的位置）。通常这没什么用，但 Objective-C 运行时使用它来查看销毁过时的缓存数据是否安全，方法是查看是否有其他线程位于访问它的函数中。

同样，这段代码可以检查原始调用线程的 PC，看看它是否仍在 `CFRelease` 内部。如果不是，那么调用一定已经完成，所以现在再次释放对象是安全的。

在 OS X 上（据我所知）获取另一个线程 PC 的唯一方法是使用 mach 调用，所以第一步是获取当前 mach 线程的引用。这个引用也需要被 "retain"（mach 端口是像 Objective-C 对象一样引用计数的），这样如果线程在此期间被销毁，它不会失效：

```
static void CallCFReleaseLater(CFTypeRef cf)
    {
        mach_port_t thread = pthread_mach_thread_np(pthread_self());
        mach_port_mod_refs(mach_task_self(), thread, MACH_PORT_RIGHT_SEND, 1 ); // "retain"
```

接下来，将这个线程引用和 CF 对象指针发送给一个后台线程。我使用 `NSOperationQueue` 来处理后台操作。我创建一个 `NSInvocationOperation` 来处理释放（将其指向 `MAZeroingWeakRef` 上的一个类方法，因为它不能处理纯函数）并将其添加到队列中。所有内容都包裹在一个自动释放池中，以防此代码从一个尚未拥有自动释放池的上下文中被调用：

```
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        SEL sel = @selector(releaseLater:fromThread:);
        NSInvocation *inv = [NSInvocation invocationWithMethodSignature: [MAZeroingWeakRef methodSignatureForSelector: sel]];
        [inv setTarget: [MAZeroingWeakRef class]];
        [inv setSelector: sel];
        [inv setArgument: &cf atIndex: 2];
        [inv setArgument: &thread atIndex: 3];

        NSInvocationOperation *op = [[NSInvocationOperation alloc] initWithInvocation: inv];
        [gCFDelayedDestructionQueue addOperation: op];
        [op release];
        [pool release];
    }
```

`releaseLater:fromThread:` 的代码基于一个循环。它持续检查目标线程的 PC，直到该 PC 移出了目标范围。一旦移出，它就释放对象以及传入的线程。首先是循环：

```
    + (void)releaseLater: (CFTypeRef)cf fromThread: (mach_port_t)thread
    {
        BOOL retry = YES;

        while(retry)
        {
```

接下来，获取目标线程的 PC。（`GetPC` 是一个辅助函数，我马上会讲到。）

```
            BLOCK_QUALIFIER void *pc;
            // 确保获取 PC 时它位于我们内部代码之外，
            // 这样就不必检查所有嵌套调用
            WhileLocked({
                pc = GetPC(thread);
            });
```

现在开始检查 PC 的有效性。首先查看它是否包含任何内容。如果没有，假设发生了临时错误并重试（这可能不是最佳策略……）：

```
            if(pc)
            {
```

接下来，查看 PC 是否在 `CustomCFFinalize` 内部。由于它是从 `CFRelease` 调用的，有可能目标线程仍在那里，我们需要等待它退出。为此，检查 PC 是否在 `CustomCFFinalize` 函数的开始和紧随其后的函数的开始之间。（编译器在内存中按顺序布局函数，所以 `IsTollFreeBridged` 的开始紧跟在 `CustomCFFinalize` 的结束之后）：

```
                if(pc < (void *)CustomCFFinalize || pc > (void *)IsTollFreeBridged)
                {
```

如果该测试通过，查看 PC 是否在 `CFRelease` 内部。我不知道 CoreFoundation 中函数的顺序，所以我不能使用同样的技巧。相反，我使用 `dladdr` 调用。它会返回指定地址之前的最后一个符号及其他信息。我可以将其与 `_CFRelease`（实际处理 `CFRelease` 调用内部逻辑的私有函数）进行对比。如果匹配，稍后重试：

```
                    Dl_info info;
                    int success = dladdr(pc, &info;);
                    if(success)
                    {
                        if(info.dli_saddr != _CFRelease)
                        {
```

如果所有测试都通过，那么就可以继续了。清除 `retry` 表示测试成功，调用 `CFRelease`，并释放线程引用：

```
                            retry = NO; // 成功！
                            CFRelease(cf);
                            mach_port_mod_refs(mach_task_self(), thread, MACH_PORT_RIGHT_SEND, -1 ); // "release"
                        }
                    }
                }
            }
        }
    }
```

最后一件事，`GetPC` 函数。实现高度依赖特定架构。通用部分看起来像这样：

```
    static void *GetPC(mach_port_t thread)
    {
        // 架构特定代码在此

        kern_return_t ret = thread_get_state(thread, flavor, (thread_state_t)&state, &count;);
        if(ret == KERN_SUCCESS)
            return (void *)state.PC_REGISTER;
        else
            return NULL;
    }
```

仓库中的实际代码包含定义 `state`、`flavor` 以及 Intel 32/64、PPC 32/64 和 ARM 的其他部分的条件编译。

就是这样了！

**收尾工作**
在上一篇文章中，我提到了 `COREFOUNDATION_HACK_LEVEL` 宏，它控制 `MAZeroingWeakRef` 中包含多少 hack。当设置为 0 时，它不使用私有 API。它拒绝引用 CoreFoundation 对象，并通过检查类名是否以 `NSCF` 前缀来检测它们。当设置为 1 时，它仅使用私有 API 进行可靠的 CoreFoundation 对象检查。现在级别 1 是默认值。

当我写上一篇文章时，我实际上并不知道这个微妙的复活竞态条件。因此，我添加了一个额外的 hack 级别。Hack 级别 2 使用私有的 CoreFoundation 调用来允许引用 CF 对象，但不会消除我上面描述的复活竞态条件。最后，新添加的 hack 级别 3 进入上面描述的完全 CoreFoundation hack 状态，并通过在后台线程中执行最终的 `CFRelease` 来消除竞态条件。

这些可以通过文件顶部的 `COREFOUNDATION_HACK_LEVEL` 宏来控制。我建议 Mac 开发使用级别 1（对 CoreFoundation 对象的弱引用通常不需要），iOS 开发使用级别 0（Apple 对使用私有 API 非常敏感）。但是，如果你有冒险精神或者需要对 CF 对象的弱引用，你可以将其设置为 3，一切_应该_仍然有效……如果你这样做了，请记住，这些真正可怕的 hack 只有在你实际创建了对一个 CF 对象的弱引用时才会激活，所以你可以启用它以防万一不小心引用了 CF 对象，而不必担心在正常情况下它会造成什么可怕的事情。

**结论**
在上一篇文章中，我展示了如何相对容易地创建 Objective-C 对象的置零弱引用。在这篇文章中，我展示了即使不容易，至少是可能对 CoreFoundation 对象做同样的事情。需要大量涉足私有 API，但这个解决方案应该是相当稳健的。

这类 hack 极具挑战性，但也非常有趣。CoreFoundation 源代码对此类事情是宝贵的资源，但一如既往，你必须警惕可能在将来发生变化的私有符号。其他底层开源代码，如 Objective-C 运行时，也是很好的阅读材料。最后，当你需要了解 Apple 没有提供源代码的库是如何工作时，`otx` 是一个非常强大的工具。

Friday Q&A 这一期就到这里。两周后再回来，看更多疯狂的把戏。

一如既往，Friday Q&A 由用户的创意驱动。如果你有一个想要在这里讨论的话题，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在销售装满这些文章的全套书籍！第二卷和第三卷现在已经出版！它们提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
