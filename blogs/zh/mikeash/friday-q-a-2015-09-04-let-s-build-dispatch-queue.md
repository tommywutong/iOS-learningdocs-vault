---
title: 'Friday Q&A 2015-09-04：让我们来构建 dispatch_queue'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f8bd4561ee19432'
translated: true
---

> 原文：[Friday Q&A 2015-09-04: Let's Build dispatch_queue](https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html)　·　mikeash.com Friday Q&A

发表于 2015-09-04 13:22 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2015-09-18：构建一个齿轮警告系统](https://www.mikeash.com/pyblog/friday-qa-2015-09-18-building-a-gear-warning-system.html)  
上一篇文章：[Friday Q&A 2015-08-14：一个用于未平滑文本的 Xcode 插件](https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2015-09-04：让我们来构建 dispatch_queue

作者：[Mike Ash](https://www.mikeash.com/)

**概述**  
调度队列（dispatch queue）是一个由全局线程池（thread pool）支持的作业队列。通常，提交到队列的作业会在后台线程上异步执行。所有线程共享一个全局的后台线程池，这使得系统更高效。

这就是我将要复现的 API 的本质。GCD 提供了许多高级功能，但为了简化，我会忽略它们。例如，全局池中的线程数量会根据待完成的工作量和系统的 CPU 利用率进行伸缩。如果你有一批作业正在大量消耗 CPU，然后你又提交了另一个作业，GCD 将避免为其创建新的工作线程，因为系统已经在 100% 运行，再增加一个线程只会降低效率。我将跳过这一点，只使用一个硬编码的线程数量上限。我也会跳过其他高级功能，例如目标队列（target queue）和并发队列的屏障（barrier）。

目标是专注于调度队列的本质：它们可以是串行（serial）或并发（concurrent）的，可以同步（synchronously）或异步（asynchronously）调度作业，并且它们由一个共享的全局线程池支持。

**代码**  
和往常一样，今天文章的代码可以在 GitHub 上找到：

[https://github.com/mikeash/MADispatchQueue](https://github.com/mikeash/MADispatchQueue)

如果你想边阅读边跟着做，或者只是想自己探索，都可以在那里找到。

**接口**  
GCD 是一个 C API。尽管在较新的 OS 版本中 GCD 对象已经变成了 Objective-C 对象，但 API 仍然是纯 C 的（加上 Apple 的 block 扩展）。这对于底层 API 来说很棒，GCD 呈现出一个非常清晰的接口，但就我个人而言，我更倾向于用 Objective-C 来重写。

Objective-C 类名为 `MADispatchQueue`，它只有四个调用：

1. 获取共享全局队列的方法。GCD 有多个不同优先级的全局队列，但为了简化，我们只用一个。
2. 一个初始化方法，可以将队列创建为并发或串行。
3. 一个异步调度调用。
4. 一个同步调度调用。

以下是接口声明：

```
    @interface MADispatchQueue : NSObject

    + (MADispatchQueue *)globalQueue;

    - (id)initSerial: (BOOL)serial;

    - (void)dispatchAsync: (dispatch_block_t)block;
    - (void)dispatchSync: (dispatch_block_t)block;

    @end
```

那么，目标是实现这些方法，使它们真正执行其声称的功能。

**线程池接口**  
支持队列的线程池有一个更简单的接口。它将负责实际运行提交的作业。而队列则负责在适当的时间提交其排队的作业，以维护队列的保证。

线程池只有一项工作：提交一些要运行的工作。因此，它的接口只有一个方法：

```
    @interface MAThreadPool : NSObject

    - (void)addBlock: (dispatch_block_t)block;

    @end
```

由于这是核心，让我们先实现它。

**线程池实现**  
先看实例变量（instance variable）。线程池会从多个线程（包括内部和外部）访问，因此需要是线程安全的。虽然 GCD 会尽可能使用快速的原子操作，但对于我的概念重建，我会坚持使用老式的锁。我需要在这个锁上等待和发送信号，而不仅仅是强制互斥，所以我使用 `NSCondition` 而不是普通的 `NSLock`。如果你不熟悉它，`NSCondition` 基本上是一个锁和一个条件变量的结合体：

```
    NSCondition *_lock;
```

为了知道何时启动新的工作线程，我需要知道池中有多少线程，有多少线程实际上正在忙碌地工作，以及我可以拥有的最大线程数：

```
    NSUInteger _threadCount;
    NSUInteger _activeThreadCount;
    NSUInteger _threadCountLimit;
```

最后，有一个要执行的 block 列表。这是一个 `NSMutableArray`，通过将新 block 追加到末尾并从开头移除来作为队列使用：

```
    NSMutableArray *_blocks;
```

初始化很简单。初始化锁，初始化 block 数组，并将线程数量限制设置为我们任意选择的 128：

```
    - (id)init {
        if((self = [super init])) {
            _lock = [[NSCondition alloc] init];
            _blocks = [[NSMutableArray alloc] init];
            _threadCountLimit = 128;
        }
        return self;
    }
```

工作线程运行一个简单的无限循环。只要 block 数组为空，它就会等待。一旦有一个 block 可用，它就会从数组中取出并执行它。执行时，它会增加活跃线程计数，完成后再次减少。让我们开始：

```
    - (void)workerThreadLoop: (id)ignore {
```

它做的第一件事是获取锁。注意，这是在循环开始*之前*完成的。原因在循环结束时就会清楚：

```
        [_lock lock];
```

现在永远循环：

```
        while(1) {
```

如果队列为空，就在锁上等待：

```
            while([_blocks count] == 0) {
                [_lock wait];
            }
```

注意，这里使用了一个循环，而不仅仅是 `if` 语句。原因是[虚假唤醒](https://en.wikipedia.org/wiki/Spurious_wakeup)。简而言之，即使没有信号，`wait` 也可能返回，因此为了正确行为，需要在 `wait` 返回时重新评估所检查的条件。

一旦有一个 block 可用，就将其出列：

```
            dispatch_block_t block = [_blocks firstObject];
            [_blocks removeObjectAtIndex: 0];
```

通过增加活跃线程计数来指示此线程现在正在处理一些事情：

```
            _activeThreadCount++;
```

现在是执行 block 的时候了，但我们必须先释放锁，否则我们将无法获得任何并发性，并且会出现各种有趣的死锁：

```
            [_lock unlock];
```

安全地释放锁之后，执行 block：

```
            block();
```

block 完成后，就该减少活跃线程计数了。这必须在持有锁的情况下完成，以避免竞态条件，这就是循环的结束：

```
            [_lock lock];
            _activeThreadCount--;
        }
    }
```

现在你可以理解为什么在进入上面的循环*之前*必须先获取锁了。循环中的最后一个操作是减少活跃线程计数，这需要持有锁。循环顶部的第一件事是检查 block 队列。通过在循环外部执行第一次加锁操作，后续的迭代可以为两个操作使用同一次加锁操作，而不是加锁、解锁然后又立即再次加锁。

现在来看 `addBlock:`：

```
    - (void)addBlock: (dispatch_block_t)block {
```

这里的一切都需要在获取锁的情况下完成：

```
        [_lock lock];
```

第一个任务是将新 block 添加到 block 队列中：

```
        [_blocks addObject: block];
```

如果有一个空闲的工作线程可以处理这个 block，那么就没太多事情要做。如果没有足够的空闲工作线程来处理所有未完成的 block，并且工作线程的数量还未达到上限，那么就该创建一个新的工作线程了：

```
        NSUInteger idleThreads = _threadCount - _activeThreadCount;
        if([_blocks count] > idleThreads && _threadCount < _threadCountLimit) {
            [NSThread detachNewThreadSelector: @selector(workerThreadLoop:)
                                     toTarget: self
                                   withObject: nil];
            _threadCount++;
        }
```

现在，一切准备就绪，工作线程可以开始处理这个 block。如果它们都在休眠，就唤醒一个：

```
        [_lock signal];
```

然后释放锁，我们就完成了：

```
        [_lock unlock];
    }
```

这样我们就有了一个线程池，它可以生成最多预设数量上限的工作线程，以服务传入的 block。现在，以此为基础来实现队列。

**队列实现**  
与线程池类似，队列将使用锁来保护其内容。与线程池不同的是，它不需要进行任何等待或发送信号，只需要基本的互斥，因此它使用一个普通的 `NSLock`：

```
    NSLock *_lock;
```

与线程池类似，它在 `NSMutableArray` 中维护一个待处理 block 的队列：

```
    NSMutableArray *_pendingBlocks;
```

队列知道它是串行还是并发：

```
    BOOL _serial;
```

当是串行时，它还会跟踪当前是否有一个 block 在线程池中运行：

```
    BOOL _serialRunning;
```

并发队列无论是否有任务在运行，行为都一样，因此它们不跟踪这个。

全局队列存储在一个全局变量中，底层的共享线程池也是如此。它们都在 `+initialize` 中创建：

```
    static MADispatchQueue *gGlobalQueue;
    static MAThreadPool *gThreadPool;

    + (void)initialize {
        if(self == [MADispatchQueue class]) {
            gGlobalQueue = [[MADispatchQueue alloc] initSerial: NO];
            gThreadPool = [[MAThreadPool alloc] init];
        }
    }
```

然后 `+globalQueue` 方法可以只返回这个变量，因为 `+initialize` 保证已经创建了它：

```
    + (MADispatchQueue *)globalQueue {
        return gGlobalQueue;
    }
```

这正是一个需要 `dispatch_once` 的场景，但在我重新实现 GCD API 时使用一个 GCD API 感觉像是在作弊，即使它不是同一个 API。

初始化一个队列包括分配锁和待处理 block 队列，并设置 `_serial` 变量：

```
    - (id)initSerial: (BOOL)serial {
        if ((self = [super init])) {
            _lock = [[NSLock alloc] init];
            _pendingBlocks = [[NSMutableArray alloc] init];
            _serial = serial;
        }
        return self;
    }
```

在我们处理剩余的公共 API 之前，需要构建一个底层方法，它将在线程池上调度一个单一的 block，然后可能会调用自身来运行另一个 block：

```
    - (void)dispatchOneBlock {
```

它存在的全部目的就是在线程池上运行任务，因此它在那里进行调度：

```
        [gThreadPool addBlock: ^{
```

然后它获取队列中的第一个 block。自然，这必须在持有锁的情况下进行，以避免灾难性崩溃：

```
            [_lock lock];
            dispatch_block_t block = [_pendingBlocks firstObject];
            [_pendingBlocks removeObjectAtIndex: 0];
            [_lock unlock];
```

拿到 block 并释放锁后，就可以安全地在后台线程上执行这个 block：

```
            block();
```

如果队列是并发的，那么它需要做的就这些了。如果是串行的，则还有更多工作：

```
            if(_serial) {
```

在一个串行队列上，额外的 block 会堆积起来，但在前面的 block 完成之前不能被执行。当一个 block 在这里完成时，`dispatchOneBlock` 会检查队列中是否还有其他待处理的 block。如果有，它会调用自身来调度下一个 block。如果没有，它会将队列的运行状态设置回 `NO`：

```
                [_lock lock];
                if([_pendingBlocks count] > 0) {
                    [self dispatchOneBlock];
                } else {
                    _serialRunning = NO;
                }
                [_lock unlock];
            }
        }];
    }
```

有了这个方法，实现 `dispatchAsync:` 就相对容易了。将 block 添加到待处理 block 队列，然后适当地设置状态并调用 `dispatchOneBlock`：

```
    - (void)dispatchAsync: (dispatch_block_t)block {
        [_lock lock];
        [_pendingBlocks addObject: block];
```

如果一个串行队列是*空闲的*，则将其状态设置为运行中并调用 `dispatchOneBlock` 来启动处理：

```
        if(_serial && !_serialRunning) {
            _serialRunning = YES;
            [self dispatchOneBlock];
```

如果队列是并发的，则无条件调用 `dispatchOneBlock`。这确保了新 block 能尽快被执行，即使另一个 block 已经在运行，因为允许多个 block 并发运行：

```
        } else if (!_serial) {
            [self dispatchOneBlock];
        }
```

如果一个串行队列已经在运行，那么不需要再做任何事情。现有的 `dispatchOneBlock` 运行最终会处理到刚刚添加到队列中的这个 block。现在释放锁：

```
        [_lock unlock];
    }
```

接下来是 `dispatchSync:`。GCD 在这方面很智能，它直接在调用线程上运行 block，同时阻止其他 block 在队列上运行（如果它是串行的）。我们不打算尝试这么智能。相反，我们将只使用 `dispatchAsync:`，并对其进行包装以等待执行完成。

它使用一个局部的 `NSCondition` 和一个 `done` 变量来指示 block 何时完成：

```
    - (void)dispatchSync: (dispatch_block_t)block {
        NSCondition *condition = [[NSCondition alloc] init];
        __block BOOL done = NO;
```

然后它异步调度一个 block。这个 block 会调用传入的 block，然后设置 `done` 并向 `condition` 发送信号：

```
        [self dispatchAsync: ^{
            block();
            [condition lock];
            done = YES;
            [condition signal];
            [condition unlock];
        }];
```

在原始的调用线程中，它在 `condition` 上等待，直到 `done` 被设置，然后返回。

```
        [condition lock];
        while (!done) {
            [condition wait];
        }
        [condition unlock];
    }
```

此时，block 的执行已经完成。成功了！这就是 `MADispatchQueue` 所需的最后一点 API。

**结论**  
一个全局线程池可以通过一个工作 block 队列和一些智能的线程生成来实现。使用一个共享的全局线程池，可以构建一个提供基本的串行/并发和同步/异步调度的基本调度队列 API。这个重建版本缺少 GCD 的许多优秀特性，而且效率肯定低得多，但即便如此，它也能让我们很好地了解此类机制内部工作原理可能是什么样的，并表明它毕竟不是魔法。（除了 [`dispatch_once`](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)。那全都是魔法。）

今天就到这里。下次再来获取更多乐趣、游戏和欢乐。Friday Q&A 由读者的想法驱动，所以如果你有什么想在下一次或未来在这里讨论的，请[告诉我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在销售一整本包含它们的书！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html)

添加你的想法，发表评论：

垃圾邮件和离题的帖子将被立即删除。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
