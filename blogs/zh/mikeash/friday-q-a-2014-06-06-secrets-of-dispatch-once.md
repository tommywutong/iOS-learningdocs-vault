---
title: 'Friday Q&A 2014-06-06：dispatch_once 的秘密'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b123985c08c83fa4'
translated: true
---

> 原文：[Friday Q&A 2014-06-06: Secrets of dispatch_once](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)　·　mikeash.com Friday Q&A

发布于 2014-06-06 13:27 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2014-06-20: Interesting Swift Features](https://www.mikeash.com/pyblog/friday-qa-2014-06-20-interesting-swift-features.html)
上一篇文章：[Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)
标签：[atomic](https://www.mikeash.com/pyblog/?tag=atomic) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2014-06-06：dispatch_once 的秘密

作者：[Mike Ash](https://www.mikeash.com/)

**API**
`dispatch_once` 的行为体现在其名称中。它只执行一次，且仅一次。

它接受两个参数。第一个是用于追踪「一次」的谓词（predicate）。第二个是在首次调用时执行的 block。调用形式如下：

```
    static dispatch_once_t predicate;
    dispatch_once(&predicate, ^{
        // 某个一次性任务
    });
```

这是一个非常棒的 API，用于惰性初始化共享状态（shared state），无论是全局字典、单例实例（singleton instance）、缓存，还是其他任何需要在第一次使用时进行一些设置的实体。

在单线程环境中，这个调用会显得有些平淡无奇，可以用一个简单的 `if` 语句替代。然而，我们生活在一个多线程的世界里，而 `dispatch_once` 是线程安全的。它保证来自多个线程的多个对 `dispatch_once` 的同时调用只会执行该 block 一次，并且所有线程都会等待执行完成，`dispatch_once` 才会返回。即使这一点自己实现起来也不算太难，但 `dispatch_once` 还非常快，而这一点确实很难做到。

**单线程实现**
让我们先看看该函数的一个简单的单线程实现。这在实际意义上几乎毫无用处，但有助于具体理解其语义。注意，`dispatch_once_t` 只是 `long` 的一个 `typedef`，初始化为零，其他值的含义留给实现来定义。以下是该函数：

```
    void SimpleOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(!*predicate) {
            block();
            *predicate = 1;
        }
    }
```

实现很简单：如果谓词为零，则调用 block 并将其设置为 1。后续调用将看到 1，而不再调用 block。这正是我们想要的，除了在多线程环境中完全不安全之外。两个线程可能同时命中 `if` 语句，导致它们都调用 block，这很糟糕。不幸的是，通常情况下，使这段代码线程安全意味着巨大的性能损失。

**性能**
在讨论 `dispatch_once` 的性能时，实际上需要考虑三种不同的场景：

1. 对给定谓词的 `dispatch_once` 的首次调用，即执行 block 的那次。
2. 首次调用之后、block 完成执行之前的 `dispatch_once` 调用。此时，调用方必须等待 block 执行完毕才能继续。
3. 首次调用之后且 block 已执行完毕的 `dispatch_once` 调用。此时无需等待，调用方可以立即继续。

场景 #1 的性能在很大程度上并不重要，只要不是慢得离谱就行。毕竟它只发生一次。

场景 #2 的性能也不太重要。它可能发生几次，但只在 block 执行期间发生。在大多数情况下，它根本不会发生。即使发生了，很可能也只发生一次。即使在压力测试中，大量线程同时调用 `dispatch_once` 并且 block 需要很长时间才能执行完毕，调用次数也仍然会限制在数千次以内。这些调用无论如何都必须等待 block，因此它们在等待过程中消耗一些不必要的 CPU 时间并不是什么大问题。

场景 #3 的性能极其重要。这种性质的调用在程序执行过程中可能发生数百万次甚至数十亿次。我们希望使用 `dispatch_once` 来保护一次性计算的执行，而这些计算的结果会被广泛使用。理想情况下，对一个计算任务引入 `dispatch_once` 所增加的成本，应该不超过预先显式完成该计算并从某个全局变量返回结果。换句话说，一旦进入场景 #3，我们确实希望这两段代码的执行性能完全相同：

```
    id gObject;

    void Compute(void) {
        gObject = ...;
    }

    id Fetch(void) {
        return gObject;
    }

    id DispatchFetch(void) {
        static id object;
        static dispatch_once_t predicate;
        dispatch_once(&predicate, ^{
            object = ...;
        });
        return object;
    }
```

当内联并优化后，`SimpleOnce` 函数几乎可以达到这个目标。在我的测试中，在我的电脑上，它大约需要半纳秒来执行。这将成为线程安全版本的金标准。

**锁**
使代码线程安全的标准方法是用锁（lock）保护对共享数据的所有访问。这里有点棘手，因为没有一个好地方可以把锁放在它要保护的数据旁边。`dispatch_once_t` 仅仅是一个 long，没有空间容纳锁。

我们可以修改 API 以接受一个包含锁和标志位的结构体。但为了保持与 `dispatch_once` 相同的签名，并且因为这仅仅是演示代码，我决定改用单个全局锁。该代码使用一个 `static pthread_mutex_t` 来保护对谓词的所有访问。在实际程序中，如果有很多不同的谓词，这将是一个糟糕的主意，因为不相关的谓词也会相互等待。对于这个我只是用一个谓词进行测试的快速示例来说，这没问题。代码与之前相同，只是周围加了一个锁：

```
    void LockedOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

        pthread_mutex_lock(&mutex);
        if(!*predicate) {
            block();
            *predicate = 1;
        }
        pthread_mutex_unlock(&mutex);
    }
```

这段代码是线程安全的，但不幸的是它慢得多。在我的电脑上，每次调用大约需要 30 纳秒，而之前版本只需半纳秒。锁相当快，但在纳秒级的场景下还是不够。

**自旋锁**
自旋锁（spinlock）是一种实现锁的方式，旨在最大限度地减少锁本身的开销。这个名字来源于自旋锁实现：在需要等待时，它会在锁上"自旋"，反复轮询以检查锁是否已被释放。普通的锁会与操作系统协调，让等待的线程休眠，并在锁释放时唤醒它们。这可以节省 CPU 时间，但额外的协调并非没有成本。通过减少这种协调，自旋锁在锁未被持有时节省了时间，代价是在多个线程试图同时获取锁时效率较低。

OS X 通过 `OSSpinLock` 函数提供了[一个方便的自旋锁 API](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/spinlock.3.html)。用 `OSSpinLock` 实现 `LockedOnce` 只需要更改几个名称：

```
    void SpinlockOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        static OSSpinLock lock = OS_SPINLOCK_INIT;

        OSSpinLockLock(&lock);
        if(!*predicate) {
            block();
            *predicate = 1;
        }
        OSSpinLockUnlock(&lock);
    }
```

这是一个相当大的改进，在我的电脑上每次调用大约需要 6.5 纳秒，而 `pthread_mutex` 版本每次调用需要 30 纳秒。然而，它仍然远未达到不安全版本的半纳秒时间。

**原子操作**
原子操作（Atomic Operations）是底层 CPU 操作，即使没有锁（lock）也始终是线程安全的。（从技术上讲，它们在硬件级别使用锁，但这只是一个实现细节。）它们正是你首先用来实现锁的东西。当锁的开销太大时，直接使用原子操作是提高性能的一种方法。没有锁的线程编程可能极其棘手，所以除非你真的、真的需要，否则不建议这样做。在这种情况下，我们讨论的是一个可能被大量使用的操作系统库，所以它可能符合条件。

原子操作的基石是比较并交换（compare and swap）。这是一个单一操作，相当于执行以下代码：

```
    BOOL CompareAndSwap(long *ptr, long testValue, long newValue) {
        if(*ptr == testValue) {
            *ptr = newValue;
            return YES;
        }
        return NO;
    }
```

换句话说，它测试内存中的某个位置是否包含一个特定值，如果是，则将其替换为新值。它返回该值是否匹配。由于比较并交换是作为原子的 CPU 指令实现的，因此可以保证，如果多个线程都对同一个内存位置执行相同的比较并交换，只有一个会成功。

这个版本的函数的实现策略是为谓词分配三个值。`0` 表示从未被触及。`1` 表示 block 当前正在执行，任何调用方都应等待。`2` 表示 block 已完成，所有调用方都可以返回。

将使用比较并交换来检查是否为 `0`，如果是，则原子地转换为 `1`。如果成功，那么该线程就是第一个发起调用的线程，它将运行 block。运行 block 后，它会将谓词设置为 `2` 以表示完成。

如果比较并交换失败，那么它将进入一个循环，重复检查是否为 `2`，直到成功。这将使其等待另一个线程完成 block 的执行。

第一步是将谓词指针转换为 `volatile` 指针，以告知编译器该值可能在函数执行过程中被其他线程更改：

```
    void AtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        volatile dispatch_once_t *volatilePredicate = predicate;
```

然后是比较并交换。Gcc 和 clang 都提供了各种以 `__sync` 开头的内置函数来实现原子操作。也有较新的以 `__atomic` 开头的函数，但对于这个实验，我坚持使用我熟悉的。这个调用对谓词执行原子的比较并交换，测试是否为 `0`，如果匹配则将其设置为 `1`：

```
        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
```

如果操作成功，该函数返回 `true`。在这种情况下，这意味着谓词是 `0`，并且这个调用是第一个。这意味着接下来的任务是调用 block：

```
            block();
```

一旦 block 完成，就需要将谓词设置为 `2`，以向任何等待的线程以及将来的调用方表明这一事实。然而，在此之前，我们需要一个内存屏障（memory barrier）来确保所有人看到正确的读写顺序。稍后会详细介绍这一点。`__sync_synchronize` 内置函数执行一个内存屏障：

```
            __sync_synchronize();
```

然后可以安全地设置谓词：

```
            *volatilePredicate = 2;
        } else {
```

如果谓词不是 `0`，则进入一个循环等待它变成 `2`。如果它已经是 `2`，这个循环将立即终止。如果它是 `1`，那么它将停留在循环中，不断重新测试谓词的值，直到它变成 `2`：

```
            while(*volatilePredicate != 2)
                ;
```

在返回之前，这里也需要一个内存屏障，以匹配上面的屏障。再次强调，稍后会详细介绍：

```
            __sync_synchronize();
        }
    }
```

这是可行的，并且应该是安全的。（无锁线程代码足够棘手，以至于我不想在投入更多思考之前就明确宣布这一点。但这是一个相当简单的场景，而且无论如何我们并不是要在这里构建可用于生产的东西。）

性能如何？结果并不理想。在我的电脑上，每次调用大约需要 20 纳秒，比自旋锁版本高很多。

**提前退出**
这段代码可以应用一个明显的优化。常见的情况是 `predicate` 包含 `2`，但代码首先测试 `0`。通过首先测试 `2` 并提前退出，可以使常见情况更快。代码很简单：在函数顶部添加一个对 `2` 的检查，如果成功，则在内存屏障后返回：

```
    void EarlyBailoutAtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(*predicate == 2) {
            __sync_synchronize();
            return;
        }

        volatile dispatch_once_t *volatilePredicate = predicate;

        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
            block();
            __sync_synchronize();
            *volatilePredicate = 2;
        } else {
            while(*volatilePredicate != 2)
                ;
            __sync_synchronize();
        }
    }
```

与第一个版本的代码相比，这是一个不错的改进，每次调用大约需要 11.5 纳秒。然而，这仍然远低于半纳秒的目标，并且甚至比自旋锁代码还要慢。

内存屏障不是免费的，这解释了为什么这段代码比目标慢这么多。至于为什么比自旋锁慢，是因为有不同类型的可用内存屏障。`__sync_synchronize` 生成一条 `mfence` 指令，这是最谨慎的一种，可以处理诸如 SSE4 流式读/写之类的高端操作，而 `OSSpinLock` 则使用一种适用于普通代码的较便宜的屏障。我们可以调整这段代码中使用的精确屏障以获得更好的性能，但很明显其开销仍然高于我们的期望，所以我会跳过这个。

**不安全的提前退出**
让我们再看一个代码版本。它与前一个版本相同，只是去掉了内存屏障：

```
    void UnsafeEarlyBailoutAtomicBuiltinsOnce(dispatch_once_t *predicate, dispatch_block_t block) {
        if(*predicate == 2)
            return;

        volatile dispatch_once_t *volatilePredicate = predicate;

        if(__sync_bool_compare_and_swap(volatilePredicate, 0, 1)) {
            block();
            *volatilePredicate = 2;
        } else {
            while(*volatilePredicate != 2)
                ;
        }
    }
```

毫不奇怪，它的性能与 `SimpleOnce` 一样快，每次调用大约半纳秒。由于 `*predicate == 2` 是迄今为止最常见的情况，几乎每次调用都只执行这个检查并返回。在 block 已被调用过的情况下，它执行的工作量与 `SimpleOnce` 相同。

然而，正如名称所示，缺少内存屏障使其不安全。为什么？

**分支预测、乱序执行与你**
我们想象我们的 CPU 是简单的机器。我们告诉它做一件事，它就去做。然后我们告诉它做下一件事，它就去做。如此重复，直到我们感到厌烦或断电。

曾几何时，这确实是事实。旧的 CPU 确实是简单的机器，完全像这样工作。它们取一条指令，然后执行它。然后它们取下一条指令，再执行它。

不幸的是，虽然这种方法简单、廉价、容易，但它也不是很快。摩尔定律使我们能够将越来越多的晶体管塞进 CPU。8086 大约由 29,000 个晶体管构成。一颗 Intel Haswell 架构的 CPU 包含超过十亿个晶体管。

市场需要更好的计算机游戏（以及少数人希望更快地执行各种不值得提及的乏味业务任务），这要求 CPU 制造商利用这些进步来实现更好的性能。现代 CPU 是数十年努力将更多晶体管转化为更快计算机的产物。

有很多技巧可以使 CPU 更快。其中之一是流水线。当你审视执行单个 CPU 指令所涉及的过程时，有很多小步骤：

```
    1. Load the instruction from memory.
    2. Decode the instruction. (That is, figure out which instruction it is, and figure out what the operands are.)
    3. Load the input data.
    4. Perform the operation on the input data.
    5. Save the output.
```

在早期的 CPU 上，工作序列看起来像这样：

```
    load instruction
    decode
    load data
    operation
    save data
    load instruction
    decode
    load data
    operation
    save data
    ...
```

但是，只要你有足够的资源，你实际上可以并行执行其中的许多操作。在流水线 CPU 上，工作序列最终可能看起来更像这样：

```
    load instruction
    decode                load instruction
    load data             decode                load instruction
    operation             load data             decode
    save data             operation             load data
                          save data             operation
                                                save data
```

这快多了！有了足够的晶体管，事情可以变得更加复杂，许多指令可以同时并行执行。

更进一步，如果看起来能加快速度，指令甚至可以完全乱序执行。与上面简化的例子不同，现实世界中的指令往往需要更多步骤，并且它们所需的步骤数有很大差异。例如，对主存的读写可能需要大量时间。通过执行指令流中后续的其他工作，CPU 可以从事生产性的工作，而不是空闲等待。因此，CPU 可能会发现，以与指令流中相应指令出现顺序不同的顺序发出内存读写是有利的。

这一切的最终结果是，你的代码并不总是按照它看起来的顺序运行。如果你写：

```
    x = 1;
    y = 2;
```

你的 CPU 可以先执行对 `y` 的写入。编译器在某些情况下也可以像这样重排语句，但即使你消除了这一点，CPU 仍然可以这样做。如果你的系统中有多个 CPU（如今我们几乎总是如此），那么其他 CPU 将会看到这些乱序的写入。即使写入是按顺序执行的，其他 CPU 也可以执行乱序的_读取_。综上所述，另一个正在读取 `x` 和 `y` 的线程可能会看到 `y = 2`，同时仍然看到 `x` 的旧值。

有时你绝对需要这些值以正确的顺序写入和读取，这就是内存屏障发挥作用的地方。在上述代码中添加一个内存屏障可以确保 `x` 首先被写入：

```
    x = 1;
    memory_barrier();
    y = 2;
```

类似地，在读取时使用屏障可以确保读取以正确的顺序执行：

```
    use(x);
    memory_barrier();
    use(y);
```

然而，由于内存屏障存在的全部意义就是对抗 CPU 试图加速的努力，因此存在固有的性能损失。

这与 `dispatch_once` 和惰性初始化相关，因为存在多个按顺序执行的读取和写入，并且它们的顺序极其重要。例如，典型的惰性对象初始化模式如下所示：

```
    static SomeClass *obj;
    static dispatch_once_t predicate;
    dispatch_once(&predicate, ^{ obj = [[SomeClass alloc] init]; });
    [obj doStuff];
```

如果在读取 `predicate` 之前读取了 `obj`，那么这段代码有可能在其仍然包含 `nil` 时读取它，紧接着另一个线程将最终值写入该变量并将 `predicate` 设置为已完成状态。然后这段代码可能读取 `predicate`，认为任务已完成，从而继续使用未初始化的 `nil`。甚至可以想象，这段代码可能读取了 `obj` 的正确值，但从为该对象分配的内存中读取了未初始化的值，从而导致在尝试发送 `doStuff` 时崩溃。

因此，`dispatch_once` 需要一个内存屏障。但正如我们所看到的，内存屏障相对较慢，如果我们能够避免，我们不想在常见情况下付出这个代价。

**分支预测与投机执行**
流水线、乱序模型对于线性指令序列来说效果很好，但条件分支（conditional branch）会导致问题。在分支条件（通常依赖于紧接的前一条指令）能够被评估之前，CPU 不知道从哪里开始获取更多指令。CPU 必须停止，等待前面的工作完成，然后评估分支条件并恢复执行。这被称为流水线停顿，可能导致显著的性能损失。

为了弥补这一点，CPU 会进行投机执行（speculative execution）。当它们看到条件分支时，它们会猜测分支可能会走向哪一边。现代 CPU 拥有复杂的分支预测硬件，通常能够以超过 90% 的正确率进行猜测。它们开始从猜测的分支中执行指令，而不是仅仅等待分支条件被评估。如果事实证明猜测是正确的，那么它只需继续执行。如果猜测是错误的，它会丢弃所有投机执行的结果，并在另一个分支上重新开始。

这正是 `dispatch_once` 读取端的情况，也就是我们希望尽可能快的那个端。在 `predicate` 的值上存在一个条件分支。CPU 应该预测分支会走常见路径，即绕过执行 block 并立即返回。在此分支的投机执行期间，CPU 可能会在另一个线程初始化这些值之前从内存加载后续值。如果那个猜测最终被证明是正确的，那么它就提交了使用未初始化值的投机执行结果。

**非对称屏障**
写屏障通常需要对等。写入端需要一个屏障以确保写入以正确的顺序完成，读取端也需要一个屏障以确保读取以正确的顺序完成。然而，在这种特定情况下，我们的性能需求是完全不对称的。我们可以容忍写入端的大幅减速，但我们希望读取端尽可能快。

诀窍在于挫败导致问题的投机执行。当分支预测不正确时，投机执行的结果会被丢弃，这意味着丢弃内存中可能未初始化的值。如果 `dispatch_once` 能够在初始化值对所有 CPU 可见之后_强制_发生一次分支预测错误，问题就解决了。

在 `predicate` 上的条件分支之后，最早可能的投机性内存读取与条件分支实际被评估之间有一个关键的时间间隔。这个间隔的具体长度取决于特定 CPU 的设计，但通常最多在几十个 CPU 周期以内。

如果写入端在写入初始化值和将最终值写入 `predicate` 之间等待至少那么长的时间，那么一切安好。然而，要确保这一点有点棘手，因为所有这些疯狂的乱序执行会再次发挥作用。

在 Intel CPU 上，`dispatch_once` 为此目的滥用了 `cpuid` 指令。`cpuid` 指令的存在是为了获取有关 CPU 身份和功能的信息，但它也强制序列化指令流，并且需要相当长的时间来执行，在某些 CPU 型号上需要数百个周期，这足以完成工作。

如果你查看 `dispatch_once` 的实现，你会发现读取端完全没有屏障：

```
    DISPATCH_INLINE DISPATCH_ALWAYS_INLINE DISPATCH_NONNULL_ALL DISPATCH_NOTHROW
    void
    _dispatch_once(dispatch_once_t *predicate, dispatch_block_t block)
    {
        if (DISPATCH_EXPECT(*predicate, ~0l) != ~0l) {
            dispatch_once(predicate, block);
        }
    }
    #define dispatch_once _dispatch_once
```

这是在头文件中，并且始终内联到调用方。`DISPATCH_EXPECT` 是一个宏，它告诉编译器生成代码，告知 CPU `*predicate` 为 `~0l` 的分支是更可能的分支。这可以提高分支预测的成功率，从而提高性能。最终，这只是一个简单的 `if` 语句，没有任何类型的屏障。性能测试证实了这一点：对真正的 `dispatch_once` 的调用匹配 0.5ns 的目标。

写入端可以在实现中找到。在调用 block 之后和做任何其他事情之前，`dispatch_once` 使用了这个宏：

```
    dispatch_atomic_maximally_synchronizing_barrier();
```

在 Intel 上，该宏生成一条 `cpuid` 指令，并在针对其他 CPU 架构时生成相应的汇编代码。

**结论**
多线程是一个奇怪而复杂的地方，现代 CPU 可以在你背后做许多事情，这使得情况更加复杂。内存屏障允许你在确实需要事情以特定顺序发生时通知硬件，但这是有代价的。`dispatch_once` 的特殊需求使其能够以一种非常规的方式绕过这个问题。通过在相关的内存写入之间等待足够长的时间，它确保读取方始终看到一致的画面，而无需在每次访问时付出内存屏障的代价。

今天就到这里。下次再来了解更多激动人心的内容，很可能关于 Swift，因为这是目前的热门话题。如果你有希望在此处涵盖的主题，并且不是「谈谈 Swift」（这是一个不错的主题，但目前已经有足够的请求了），请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售包含它们的整本书！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
