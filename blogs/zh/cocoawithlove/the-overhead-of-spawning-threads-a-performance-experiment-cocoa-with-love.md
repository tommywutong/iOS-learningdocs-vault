---
title: '线程生成的开销（一项性能实验）| Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/09/overhead-of-spawning-threads.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:258b0f0c8022d670'
translated: true
---

> 原文：[The overhead of spawning threads (a performance experiment) | Cocoa with Love](https://www.cocoawithlove.com/2010/09/overhead-of-spawning-threads.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我随性地看一看以不同方式处理任务时的相对性能开销：在主线程（main thread）中执行所有任务、将任务发送给单个工作线程、为每个任务生成新线程，以及使用 Grand Central Dispatch（GCD）。这不会是一次特别深入的探究，只是对任务管理中简单性与性能的一次快速概览。

## 引言

我有一些项目需要支持 Mac OS X Leopard 和 iOS 3.x，因此这些项目无法使用 libdispatch（也就是 Grand Central Dispatch）。

在这些无法使用 GCD 的场景下，我很好奇，妥善设置基于 CFRunLoop 的专用工作线程，与采用更随意、为每个任务生成一个新 NSThread 的做法相比，它们的开销差异到底有多大。这篇文章展示了这次探究的结果。

我还加入了 GCD 的结果，以便与这些传统的 Cocoa 线程方法进行比较。GCD 比任何其他线程方法都快得多，这应该不出所料。不过，关于 GCD 队列配置会如何影响不同计算机上的性能，这里也有一些有意思的信息。

## 测试设置

测试相对直接：

- 需要运行多个任务队列。
- 每个队列串行运行多个任务。
- 任务的完整集合并不能提前知道——每个任务完成后，才会将下一个任务加入队列。

在代码中，我把每个队列上运行的任务数量称为“迭代次数（iterations）”，因为每个队列实际上只有一个任务对象，而它又会把自己作为下一个任务重新添加回队列。

这些任务本身没有实际工作要做（除了递减迭代计数）。这里的目的纯粹是测试不同任务排队和管理方法的开销。

## 队列实现

### SingleThreadedQueue

单线程队列仅仅是把所有任务添加到一个 NSMutableArray 中，并按添加顺序在当前线程中运行它们。

这个测试完全不涉及工作线程，实际上属于“对照”情况。

运行所有任务需要循环直到队列为空，并在每次迭代中运行一个任务。

```objc
- (void)queueJob:(Job *)aJob
{
    if (!jobQueue)
    {
        jobQueue = [[NSMutableArray alloc] init];
        [jobQueue addObject:aJob];
        
        while ([jobQueue count] > 0)
        {
            Job *nextJob = [jobQueue objectAtIndex:0];
            [jobQueue removeObjectAtIndex:0]; 
            [nextJob performIterationAndRequeueInJobRunner:self];
        }
        
        [jobQueue release];
        jobQueue = nil;
    }
    else
    {
        [jobQueue addObject:aJob];
    }
}
```

其他工作外面的 `if (!jobQueue)` 条件，是为了避免当 `performIterationAndRequeueInJobRunner:` 方法再次调用 `queueJob:` 以将下一个任务加入队列时，在栈上发生递归。

### RunLoopQueue

运行一个专用工作线程需要创建并启动一个 `NSThread`，但一旦线程启动，你就可以通过 `performSelector:` 把任务添加到它上面。

```objc
- (void)queueJob:(Job *)aJob
{
    [aJob
        performSelector:@selector(performIterationAndRequeueInJobRunner:)
        onThread:runLoopThread 
        withObject:self
        waitUntilDone:NO];
}
```

### DetachThreadQueue

这里的要点是我们要为每个任务创建一个新线程。我们还需要一个线程入口点，负责搭建一个 `NSAutoreleasePool`（或我们可能需要的其他线程上下文）并实际运行任务本身。

```objc
- (void)queueJob:(Job *)aJob
{
    [NSThread detachNewThreadSelector:@selector(threadEntry:)
        toTarget:self withObject: aJob];
}
```

```objc
- (void)threadEntry:(Job *)aJob
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    [aJob performIterationAndRequeueInJobRunner:self];
    [pool release];
}
```

### DetachThreadWithVerificationQueue

然而，在拿这个测试做实验时，我遇到了一个以前从未碰到过的问题：Mac OS X 的线程限制。根据命令行函数 `sysctl kern.maxfiles`，我这整个操作系统的线程限制约为 12288（该限制取决于 RAM）——你得相当莽撞才能把它们用光，但这并非不可能。

烦人的地方在于，当 `NSThread` 无法启动一个实际线程时，你不会收到错误——取而代之的是，线程永远不会启动，而你只能纳闷为什么什么都没发生。

因此，我引入了一点额外代码来确保线程正常启动。这段代码把一个 NSCondition 传入分离出来的线程，如果这个条件在 10 秒内没有被通知，就假定线程启动失败。

```objc
- (void)queueJob:(Job *)aJob
{
    NSCondition *startedCondition = [[NSCondition alloc] init];
    NSDictionary *threadParameters =
        [NSDictionary dictionaryWithObjectsAndKeys:
            aJob, @"job",
            startedCondition, @"condition",
        nil];
    
    [startedCondition lock];
    
    [NSThread detachNewThreadSelector:@selector(threadEntry:)
        toTarget:self withObject:threadParameters];
    
    if (![startedCondition waitUntilDate:[NSDate dateWithTimeIntervalSinceNow:10.0]])
    {
        NSLog(@"Thread creation failed.");
        [aJob killJob];
    }
    
    [startedCondition unlock];
    [startedCondition release];
}
```

```objc
- (void)threadEntry:(id)threadParameters
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSCondition *startedCondition = [threadParameters objectForKey:@"condition"];
    Job *aJob = [threadParameters objectForKey:@"job"];
    
    [startedCondition lock];
    [startedCondition signal];
    [startedCondition unlock];
    
    [aJob performIterationAndRequeueInJobRunner:self];
    [pool release];
}
```

### GCD 专用队列

一旦你使用 `dispatch_queue_create` 创建了一个队列，向它发送任务就非常简单：

```objc
- (void)queueJob:(Job *)aJob
{
   dispatch_async(queue, ^{
      [aJob performIterationAndRequeueInJobRunner:self];
   });
}
```

### DispatchGlobalConcurrentQueue

这里 `queueJob` 的实现完全相同，唯一的区别在于队列是通过 `dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0)` 获取的。

```objc
- (void)queueJob:(Job *)aJob
{
   dispatch_async(queue, ^{
      [aJob performIterationAndRequeueInJobRunner:self];
   });
}
```

## 结果

我的计算机是一台支持超线程（HyperThreading）的 4 核 Mac Pro。这与这些测试尤其相关，因为它在硬件上理应能支持 8 个线程。让我们看看结果如何。

在下面的耗时结果表中，使用了以下缩写：

- Single — SingleThreadedQueue
- RunLoop — RunLoopQueue
- Detach — DetachThreadQueue
- Detach w/ Ver. — DetachThreadWithVerificationQueue
- GCD-DQ — DispatchDedicatedQueue
- GCD-GCQ — DispatchGlobalConcurrentQueue

| 配置 | Single | RunLoop | Detach | Detach w/ Ver. | GCD-DQ | GCD-GCQ |
|---|---|---|---|---|---|---|
| 1 个队列, 10 万次迭代 | 0.035990 | 0.776727 | 6.356978 | 7.166419 | 0.052294 | 0.102622 |
| 4 个队列, 2.5 万次迭代 | 0.036177 | 0.243689 | 4.513922 | 4.643964 | 0.038666 | 0.044127 |
| 8 个队列, 1.25 万次迭代 | 0.036134 | 0.199367 | 13.750981 | 11.947684 | 0.025748 | 0.046173 |
| 16 个队列, 6250 次迭代 | 0.036132 | 0.200769 | 40.493681 | 30.934207 | 0.025616 | 0.046114 |

所有时间均以秒为单位。迭代次数是每个队列的（总迭代次数始终为 10 万次）。

直观比较除 Detach Thread 方法之外的所有方法：

![](https://www.cocoawithlove.com/assets/objc-era/chart1.png)

纵轴以秒为单位。

我故意把图表的顶部截掉了，但 RunLoop 版本在第一次测试中耗时 0.776727 秒——比此图表顶部高出三倍多。

![](https://www.cocoawithlove.com/assets/objc-era/chart2.png)

我将 Detach Thread 方法单独放在一张图表中，因为它们要慢一个数量级以上。同样，纵轴以秒为单位。

## 分析

由于这些测试旨在测试任务队列的开销，而 SingleThreadedQueue 没有线程开销，只需要执行 `NSArray` 操作，因此它通常最快并不令人意外——除了在 8 个和 16 个队列的情况下，DispatchDedicatedQueue 更快（很可能是因为它那点微不足道的实际开销被我计算机中的多个核心消化掉了）。

我的计算机可以在硬件上运行 8 个线程。这很可能就能解释为什么 8 个队列是生成 RunLoop 和 GCD 专用队列的最佳数量。不过，GCD 全局并发队列从未用满全部 8 个可能线程（其总 CPU 使用率峰值为 59%，大约相当于使用了 4 个线程），因此它在 4 个并发队列时性能达到峰值。

DetachThread 队列实际使用的线程数是队列数的两倍（前一个和下一个任务的队列会同时存在），因此这些队列在 4 个队列时达到峰值。有趣的是，“带验证（with verification）”的版本在超过 4 个队列后，性能开始超过“不带验证（without）”的版本——我怀疑这是因为验证中用到的互斥锁（mutex）实际上略微降低了活跃线程数。

显然，分离线程具有非常高的开销——大约每生成 12000 个线程需要 1 秒。如果你只生成 20 或 30 个线程，这不会成为问题，但要生成成百上千个则完全是浪费时间——而且随着任何给定时刻活跃线程数的增加，情况只会变得更糟。

## 结论

> 你可以下载本文中用到的代码 [ThreadingOverheads.zip](https://www.cocoawithlove.com/assets/objc-era/ThreadingOverheads.zip) (14kb)

虽然为不频繁的任务（多至每秒几十个）分离新线程是可行的，但一个全新线程的开销不容小觑，因此如果你的任务数量多且规模小，一个能重用线程的方案就相当重要。即便是在 GCD 出现之前 Cocoa 中基于 RunLoop 的解决方案（也就是传统的工作线程做法），一旦任务数量达到数万级别，其开销也是显而易见的。

很容易理解为什么 Apple 选择引入 Grand Central Dispatch——相对典型的基于 RunLoop 的工作线程，它将任务队列的开销降低了一个数量级，而且它们还更易于创建和使用。
