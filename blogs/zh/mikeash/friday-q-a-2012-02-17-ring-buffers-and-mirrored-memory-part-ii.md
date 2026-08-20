---
title: 'Friday Q&A 2012-02-17: 环形缓冲区和镜像内存：第二部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f6f61f547929344'
translated: true
---

> 原文：[Friday Q&A 2012-02-17: Ring Buffers and Mirrored Memory: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)　·　mikeash.com Friday Q&A

发布于 2012-02-17 12:50 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)  
上一篇文章：[Deadlocks and Lock Ordering: a Vignette](https://www.mikeash.com/pyblog/deadlocks-and-lock-ordering-a-vignette.html)  
标签：[code](https://www.mikeash.com/pyblog/?tag=code) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2012-02-17: 环形缓冲区和镜像内存：第二部分

作者：[Mike Ash](https://www.mikeash.com/)

**代码**  
和上次一样，我们将讨论的代码可在 GitHub 上获取：

[https://github.com/mikeash/MAMirroredQueue](https://github.com/mikeash/MAMirroredQueue)

**目标**  
镜像内存（mirrored memory）技巧允许将指向内部缓冲区的指针暴露给外部世界，因为数据和空闲空间始终是连续的。目标是创建一个 API，让这一切变得易于使用。在默认操作下，环形缓冲区（ring buffer）还应该能够增长以容纳新写入的数据。对于多线程使用，环形缓冲区的大小可以锁定，此时缓冲区对于同时存在的一个读取者和一个写入者是线程安全的。针对这种情况，线程安全应无需锁即可实现。

**API**  
环形缓冲区实现在一个名为 `MAMirroredQueue` 的类中：

```
    @interface MAMirroredQueue : NSObject
```

对于读取，有三个方法。一个方法获取可读取的数据量，一个方法返回指向数据的指针，一个方法推进指针：

```
    - (size_t)availableBytes;
    - (void *)readPointer;
    - (void)advanceReadPointer: (size_t)howmuch;
```

这样，客户端可以找出可以读取多少数据，访问数据，然后在完成后通过推进指针将这些数据从环形缓冲区中移除。

对于写入数据，接口类似。不过，不是用方法来查询数据量，而是有一个方法简单地确保所需的空闲空间可用：

```
    - (BOOL)ensureWriteSpace: (size_t)howmuch;
    - (void *)writePointer;
    - (void)advanceWritePointer: (size_t)howmuch;
```

`ensureWriteSpace:` 方法返回成功或失败。当分配未锁定时（默认状态），它将始终成功。当分配被锁定时（为确保线程安全），仅当缓冲区中有足够的空闲空间时才成功，否则返回 `NO`。

写入 API 中的另外两个方法与读取 API 相同：一个用于获取数据指针，另一个用于在写入数据后推进它。

在讨论了这么多关于锁定分配的内容后，我们可能需要一些方法来实际管理它：

```
    - (void)lockAllocation;
    - (void)unlockAllocation;
```

队列初始状态是未锁定的。如果需要线程安全操作，可以通过调用 `ensureWriteSpace:` 分配所需的空间，之后 `lockAllocation` 确保缓冲区不会被重新分配。如果将来需要扩展缓冲区，可以使用 `unlockAllocation` 后跟另一个 `ensureWriteSpace:` 来实现。

最后，我还编写了一对围绕上述功能的类 UNIX 包装器：

```
    - (size_t)read: (void *)buf count: (size_t)howmuch;
    - (size_t)write: (const void *)buf count: (size_t)howmuch;
```

这些不是必需的，实际上效率较低，因为 API 需要将数据复制到环形缓冲区中和从环形缓冲区中复制出来，但拥有一个共享 POSIX `read` 和 `write` 调用语义的 API 也是很不错的。

**实例变量**  
缓冲区本身由三个实例变量描述：

```
    char *_buf;
    size_t _bufSize;
    BOOL _allocationLocked;
```

我希望这些都是不言自明的。请注意，`_buf` 是 `char *`，以便于进行指针运算，这在后面会派上用场。虽然 `gcc` 和 `clang` 允许，但严格来说，`void *` 指针不允许进行指针运算，因此对于按字节寻址的实体，`char *` 是一个方便的选择。

除了缓冲区，我们还需要一个读取指针和一个写入指针：

```
    char *_readPointer;
    char *_writePointer;
```

**实用函数**  
页面大小对于此代码很重要，它需要能够将数字向上和向下舍入到页面大小的倍数。我编写了两个围绕 mach 宏的简单包装器来管理这一点：

```
    static size_t RoundUpToPageSize(size_t n)
    {
        return round_page(n);
    }

    static void *RoundDownToPageSize(void *ptr)
    {
        return (void *)trunc_page((intptr_t)ptr);
    }
```

第一个只是将字节大小向上舍入到最接近的页面大小倍数，第二个将指针向下舍入到最近的页面边界。

**代码**  
首先是 `dealloc` 方法。我假设使用 `ARC`，因此无需调用 `super`。它所做的就是释放已分配的缓冲区（如果已分配）：

```
    - (void)dealloc
    {
        if(_buf)
            free_mirrored(_buf, _bufSize, MIRROR_COUNT);
    }
```

`MIRROR_COUNT` 只是一个 `#define`，它描述要分配多少份镜像副本。有趣的是，它被设置为 `3`，而不是你可能期望的 `2`，这就是为什么我的镜像分配器支持任意数量的镜像，而不是只硬编码两个。关于此原因的更多讨论将在后面进行。

没有初始化方法，因为将所有实例变量设置为 `0` 或 `NULL` 就足够了。环形缓冲区初始状态为空，全零状态恰好可以描述这一点。

接下来，我们有 `availableBytes` 方法。它首先将写入指针减去读取指针：

```
    - (size_t)availableBytes
    {
        ptrdiff_t amount = _writePointer - _readPointer;
```

通常，这仅是缓冲区中的数据字节数。但是，如果在计算此值时另一个线程正在修改此缓冲区，指针可能会发生移动。如果它们只是因读取或写入量而移动，那没问题。我们最终可能会计算出可用字节数的旧值或新值，但两者都可以正常工作。

然而，指针也可能因缓冲区的大小而移动。当读取指针进入第二个镜像区域时，它会被重置回第一个区域，写入指针也会随之移动。因此，此处计算的大小可能小于零（如果我们在写入指针更新后但在读取指针更新前观察），也可能大于缓冲区大小（如果我们在读取指针更新后但在写入指针更新前观察）。由于我们知道可用字节数**必须**在零和缓冲区大小之间，因此很容易修正：只检查这些情况，并相应调整数量：

```
        if(amount < 0)
            amount += _bufSize;
        else if((size_t)amount > _bufSize)
            amount -= _bufSize;

        return amount;
    }
```

接下来是 `readPointer`。它只是返回实例变量：

```
    - (void *)readPointer
    {
        return _readPointer;
    }
```

接下来是 `advanceReadPointer:`。这只是将数量添加到读取指针：

```
    - (void)advanceReadPointer: (size_t)howmuch
    {
        _readPointer += howmuch;
```

但这里还没结束。如果这会使得读取指针超过第一个镜像区域的末尾，则需要将读取指针和写入指针都拉回来。对于读取指针，只需减去 `_bufSize` 即可。由于写入指针可能会同时被读取者线程（通过此方法）和写入者线程（在 `advanceWritePointer:` 中）修改，因此需要使用原子操作来更新它。我使用内置的 `__sync_sub_and_fetch` 函数来实现：

```
        if((size_t)(_readPointer - _buf) >= _bufSize)
        {
            _readPointer -= _bufSize;
            __sync_sub_and_fetch(&_writePointer, _bufSize);
        }
    }
```

接下来是 `ensureWriteSpace:`。第一部分很简单：通过从总缓冲区大小减去 `[self availableBytes]` 来找出有多少空闲空间可用，如果请求的数量小于这个值，一切就绪：

```
    - (BOOL)ensureWriteSpace: (size_t)howmuch
    {
        size_t contentLength = [self availableBytes];
        if(howmuch <= _bufSize - contentLength)
            return YES;
```

否则，我们知道空闲空间**不足**以满足请求。如果分配已锁定，那就这样了，游戏结束，返回 `NO`：

```
        else if(_allocationLocked)
            return NO;
```

如果分配未锁定，那么是时候重新分配缓冲区了。

首先要做的是确定要分配多少内存，然后分配一个该大小的新缓冲区。回想一下，因为镜像分配器使用虚拟内存技巧，它必须分配页面大小的倍数。我们至少需要 `contentLength + howmuch` 的内存，因此新的缓冲区大小是通过将该数字向上舍入到最接近的页面大小来确定的：

```
        size_t newBufferLength = RoundUpToPageSize(contentLength + howmuch);
```

接下来，分配新缓冲区：

```
        char *newBuf = allocate_mirrored(newBufferLength, MIRROR_COUNT);
```

现在有了新缓冲区，代码会分支一些。如果已经存在一个缓冲区，那么我们是在重新分配内存，必须将数据从旧缓冲区复制到新缓冲区：

```
        if(_bufSize > 0)
        {
```

我们又要玩虚拟内存游戏了。Mach 提供了一个 `vm_copy` 函数，它可以复制页面对齐的内存而无需实际复制。相反，页面会被重新映射并设置为写时复制。对于这种情况，我们将立即释放旧内存，这意味着实际上从未复制任何数据，系统只是玩弄一些虚拟内存技巧使其看起来像是复制了。

我们想从读取指针开始复制，但因为所有内容都必须页面对齐，所以复制必须从包含读取指针的页面的开头开始：

```
            char *copyStart = RoundDownToPageSize(_readPointer);
```

同样，长度必须是页面大小的倍数。从 `copyStart` 开始，我们需要复制 `_writePointer - copyStart` 个字节，但这需要向上舍入以适应页面大小：

```
            size_t copyLength = RoundUpToPageSize(_writePointer - copyStart);
```

现在设置好了，我们可以将这些数据“复制”到新缓冲区中：

```
            vm_copy(mach_task_self(), (vm_address_t)copyStart, copyLength, (vm_address_t)newBuf);
```

现在数据已复制，我们需要计算新读取指针的位置。我们通过将 `_readPointer` 向下舍入到 `copyStart` 复制了额外的字节。新的读取指针等于 `newBuf` 加上额外字节的数量：

```
            char *newReadPointer = newBuf + (_readPointer - copyStart);
```

在我开发代码时，这个位置特别麻烦，所以我添加了一个断言以确保能尽早且明确地失败：

```
            if(*newReadPointer != *_readPointer)
                abort();
```

现在我们可以释放旧缓冲区并重新赋值读取指针：

```
            free_mirrored(_buf, _bufSize, MIRROR_COUNT);
            _readPointer = newReadPointer;
```

写入指针设置为等于读取指针加上之前计算的内容长度：

```
            _writePointer = _readPointer + contentLength;
        }
```

对于不存在先前缓冲区的情况，代码很简单：只需将读取和写入指针设置为新缓冲区的开头：

```
        else
        {
            _readPointer = newBuf;
            _writePointer = newBuf;
        }
```

新缓冲区已分配，数据已复制（如果需要），现在剩下的就是设置 `_buf` 和 `_bufSize` 实例变量，然后向调用方返回 `YES`：

```
        _buf = newBuf;
        _bufSize = newBufferLength;

        return YES;
    }
```

接下来是 `writePointer` 方法，它同样只是一个简单的访问器：

```
    - (void *)writePointer
    {
        return _writePointer;
    }
```

`advanceWritePointer:` 方法也很简单，对 `_writePointer` 执行原子加操作：

```
    - (void)advanceWritePointer: (size_t)howmuch
    {
        __sync_add_and_fetch(&_writePointer, howmuch);
    }
```

请注意，与 `advanceReadPointer:` 不同，此方法不需要任何检查来将指针回绕到第一个镜像数据部分。`advanceReadPointer:` 方法处理读取和写入指针的回绕。由于此处没有发生回绕，写入指针可以长时间位于第二个镜像数据部分，但这完全没问题。

通过让写入指针始终位于读取指针之前，此代码避免了一个恼人的歧义。使用读取和写入指针的环形缓冲区通常在读取和写入指针相等时遇到问题。没有简单的方法来区分缓冲区为空（两个指针相等，因为它们之间没有数据）和缓冲区为满（两个指针相等，因为它们之间没有空闲空间）。

环形缓冲区的实现通常通过禁止缓冲区完全填满来避免这种情况，而是将“满”定义为比真正的满容量少一个单位，或者使用指针加计数而不是两个指针。

这两种替代方案在这种情况下都没有吸引力。在进行疯狂的虚拟内存游戏时，人为地将缓冲区缩小一个字节尤其痛苦，因为使用此环形缓冲区的代码很可能也希望处理整个页面，而如果从缓冲区中丢失一个字节，它基本上就丢失了整整 4kB 的页面。使用指针和计数会使实现无锁的线程安全性变得极其困难，甚至完全不可能，因为写入指针变成了从其他两个值计算得出的派生值，这两个值都由读取线程修改，并且当两者同时更新时，从另一个线程的角度看，它们可能暂时不一致。

通过镜像分配进行的虚拟内存游戏提供了第三种更好的方式：简单地使用两个指针，并通过使写入指针等于读取指针加上缓冲区大小来表示“满”。这是很自然的，由于镜像分配，它工作得很好，并且易于处理。

接下来是分配锁定方法。这些仅操作 `_allocationLocked` 实例变量。这些方法中不需要做其他事情，因为它们只修改 `ensureWriteSpace:` 的行为。代码如下：

```
    - (void)lockAllocation
    {
        _allocationLocked = YES;
    }

    - (void)unlockAllocation
    {
        _allocationLocked = NO;
    }
```

接下来，我们有类 UNIX 兼容性包装器。这些有助于说明更原始、更直接的 API 是如何使用的。`read:count:` 方法使用 `availableBytes` 计算出要读取多少数据，从 `readPointer` 复制数据，然后调用 `advanceReadPointer:` 将数据标记为已读取：

```
    - (size_t)read: (void *)buf count: (size_t)howmuch
    {
        size_t toRead = MIN(howmuch, [self availableBytes]);
        memcpy(buf, [self readPointer], toRead);
        [self advanceReadPointer: toRead];
        return toRead;
    }
```

`write:count:` 的情况稍微复杂一些，它的行为取决于分配是否被锁定。如果分配已锁定，则它只写入缓冲区剩余空间能容纳的数据量。否则，它会使用 `ensureWriteSpace:` 来将缓冲区增长到合适的大小（如果需要）：

```
    - (size_t)write: (const void *)buf count: (size_t)howmuch
    {
        if(_allocationLocked)
            howmuch = MIN(howmuch, _bufSize - [self availableBytes]);
        else
            [self ensureWriteSpace: howmuch];
```

其余部分很简单。它将数据复制到 `writePointer`，推进写入指针，并返回写入的数据量：

```
        memcpy([self writePointer], buf, howmuch);
        [self advanceWritePointer: howmuch];
        return howmuch;
    }
```

这就完成了镜像队列的实现。

**线程安全**  
此实现的目标之一是在存在一个读取者线程和一个写入者线程的情况下实现线程安全。以上代码实现了这一点，但为什么这样是安全的，并不完全清楚。没有锁，并且读取指针甚至不使用原子操作进行更新。

首先，请注意，此代码仅在分配被锁定的情况下是线程安全的。这意味着 `ensureWriteSpace:` 中所有棘手的重新分配代码都不会起作用。这很好，因为要使该代码在没有锁的情况下实现线程安全将极其困难。鉴于此，我们可以认为 `_buf` 和 `_bufSize` 是常量。可能由一个线程修改同时又被另一个线程读取的变量只有 `_readPointer` 和 `_writePointer`。

考虑两个独立的情况是最容易的。首先，即使写入者线程正在修改这些值，读取者线程也需要正确。其次，即使读取者线程正在修改这些值，写入者线程也需要正确。如果两者都成立，那么整个事情就是正确的。

让我们看看第一种情况，确保读取者线程在面对写入者线程的修改时是正确的。写入者线程只修改 `_writePointer`。读取者线程依赖于 `_writePointer` 值的唯一地方是在 `availableBytes` 中：

```
    ptrdiff_t amount = _writePointer - _readPointer;
```

这种非同步访问是完全安全的。存在一个竞态条件（race condition），即不确定读取线程将看到 `_writePointer` 的旧值还是新值。然而，这并不重要。`_writePointer` 只会增加，可用字节数也只会增加。如果它看到旧值，它仍然计算出一个**正确**的可用字节数，只是稍微过时。如果它看到新值，那就更好了。因此，读取者是安全的。

现在，让我们看看写入者在面对读取者的变化时的安全性。读取者可以修改两个指针，因此分析稍微复杂一些。写入者代码也会调用 `availableBytes`，一个名义上属于读取者端的方法，因此该方法必须对两者都安全。

读取者线程改变 `_writePointer` 的唯一方式是通过这一行：

```
    __sync_sub_and_fetch(&_writePointer, _bufSize);
```

由于底层缓冲区的镜像结构，`_writePointer` 的旧值和新值在这里都是正确的。`availableBytes` 可以处理任一值，并且在任何一种情况下都会返回正确的答案。同样，当 `writePointer` 返回值时，无论它是旧值还是新值都没有关系，因为就向它们写入数据时发生的情况而言，两者是等价的。最后，`advanceWritePointer:` 是安全的，因为它也使用 `__sync` 内置函数来修改 `_writePointer`，确保两个更新将以**某种**顺序应用，而具体的顺序并不重要。

写入者线程使用 `_readPointer` 的唯一地方是在 `availableBytes` 中。就像写入者线程修改其指针而读取者调用 `availableBytes` 的对应情况一样，在写入者计算 `availableBytes` 时，读取者线程修改 `_readPointer` 是安全的。推进读取指针会减少可用字节数，这**增加**了写入空间量。如果写入者线程在此处看到 `_readPointer` 的旧值，它会计算出更旧、更少的写入空间，这仍然是安全的，只是稍微陈旧。

写入者线程在面对读取者线程的更改时是安全的，反之亦然。因此，此代码确实是线程安全的。

**三重镜像**  
我承诺过会解释为什么 `MAMirroredQueue` 分配其缓冲区的**三份**镜像副本，现在就是时候了。

通常，两份副本对于连续的环形缓冲区来说就足够了。然而，请记住，此实现有点奇怪，即使对于镜像环形缓冲区也是如此，它使用单独的读取和写入指针，并允许写入指针位于第二个镜像区域中。这实现了无锁的线程安全，并允许使用整个缓冲区，而不会出现两个指针相等时的那种奇怪歧义。然而，这也需要存在第三个镜像区域。

这种需求极其罕见，但还是可能发生。首先，我们需要一个数据部分已经绕回到开头的缓冲区。在普通的环形缓冲区中，它看起来像这样：

```
         read
          |
          v
    +----------+
    |xxx  xxxxx|
    +----------+
        ^
        |
       write
```

在镜像环形缓冲区中，它看起来像这样：

```
         read
          |
          v
    +----------+----------+
    |xxx  xxxxx|xxx  xxxxx|
    +----------+----------+
                   ^
                   |
                  write
```

到目前为止，一切顺利。写入指针是有效的，将数据写入空白区域是正确的。现在，假设有独立的读取者线程和写入者线程在同时操作此缓冲区。读取者线程向上移动读取指针：

```
                 read
                  |
                  v
    +----------+----------+
    |  x       |  x       |
    +----------+----------+
                   ^
                   |
                  write
```

读取者线程的下一步是将读取指针和写入指针都向下移动到第一个镜像区域。**但是！** 在这发生之前，假设写入者突然要写入大量数据。（记住，在抢占式线程的世界中，两个线程可以以各种奇怪的顺序运行。）在读取线程能够移动任何指针之前，写入线程计算可用空间，将数据写入缓冲区，然后崩溃：

```
                 read
                  |
                  v
    +----------+----------+
    |  x       |  xXXXXXXX|XX
    +----------+----------+
                   ^
                   |
                  write
```

写入者写到了第二个镜像段的末尾之外！它看到了大量可用的空闲空间，这是正确的，但问题在于，这个空闲空间的末尾只能通过位于第一个镜像段中的写入指针来访问。由于我们允许写入指针停留在第二个镜像段中，因此有可能出现问题。这是一个短暂的竞态窗口（race window），需要非常特定的条件才能触发，但它是可能发生的，并且需要防范。

幸运的是，通过简单地分配第三个镜像段，这个问题很容易解决。在这种情况下，序列如下所示：

```
         read
          |
          v
    +----------+----------+----------+
    |xxx  xxxxx|xxx  xxxxx|xxx  xxxxx|
    +----------+----------+----------+
                   ^
                   |
                  write

                 read
                  |
                  v
    +----------+----------+----------+
    |  x       |  x       |  x       |
    +----------+----------+----------+
                   ^
                   |
                  write

                 read
                  |
                  v
    +----------+----------+----------+
    |XXxXXXXXXX|XXxXXXXXXX|XXxXXXXXXX|
    +----------+----------+----------+
                   ^
                   |
                  write
```

有了末尾额外的镜像区域，过剩的数据被写入一个安全的位置，一切正常运作。此时，读取线程会介入，将指针向下移动，然后程序继续正常运行。

**结论**  
至此，我们对镜像内存环形缓冲区的探索就结束了。我希望这段旅程能让你有所启发。哦，源代码采用标准的 BSD 许可证全部提供，以防你需要在你的 App 中使用它。

下次回来，我们将迎来另一集激动人心的内容。Friday Q&A 一如既往地由读者驱动，因此请同时[将你的主题想法发送过来](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我正在销售装满这些文章的整本书！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会被公开羞辱，由我自行决定。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
