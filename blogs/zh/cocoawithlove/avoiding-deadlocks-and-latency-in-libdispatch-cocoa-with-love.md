---
title: 在 libdispatch 中避免死锁和延迟 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/06/avoiding-deadlocks-and-latency-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:732229487d0cde8c'
translated: true
---

> 原文：[Avoiding deadlocks and latency in libdispatch | Cocoa with Love](https://www.cocoawithlove.com/2010/06/avoiding-deadlocks-and-latency-in.html)　·　Cocoa with Love (Matt Gallagher)

libdispatch 全局队列（global queue）的系统级线程池（system-wide thread pool）是一种高效管理并发操作的简便方法，但它并不能解决所有线程问题，而且它自身也存在一类问题。在本文中，我将探讨基于线程池的解决方案（如 libdispatch 的全局并发队列）所固有的死锁和延迟问题，让你了解何时应使用此方案，何时需要另寻他法。

## 引言：libdispatch 的全局队列是受限资源

在 Mac OS X 10.6（Snow Leopard）中，Apple 引入了 Grand Central Dispatch (GCD) 来管理系统级线程池。GCD 的标准 API 是 libdispatch（顾名思义，此 API 是 libSystem 的一部分）。

与 libdispatch 交互的最简单方式是在全局队列上执行 `block`：

```objc
dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
dispatch_async(queue, ^{ /* 执行一些工作 */ });
```

对于不依赖顺序的离散工作包来说，这是一个很好的解决方案。然而，在本文中，我将探讨那些选择此方案并不合适的情况。

这种方法的关键限制在于：全局并发线程池（global concurrent thread pool）是一种受限资源——该池中活跃线程的数量等于你计算机上的 CPU 数量。

一旦达到此资源的限制，不加区分地使用它可能导致以下问题：

- 相较于其他解决方案更高的延迟
- 队列中相互依赖的任务（interdependent jobs）发生死锁

## 延迟问题

以下代码模拟了一个需要为多个客户端提供服务的微型 Web 服务器或类似程序。在此示例中，它同时处理来自不同客户端的 20 个请求。

实际上，该程序只是对每个客户端向 `/dev/null` 写入一个小字符串 100,000 次，但这足以模拟任何类似的网络或非 CPU 密集型操作。

```objc
int main(int argc, const char * argv[])
{
    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();

    FILE *devNull = fopen("/dev/null", "a");

    const int NumConcurrentBlocks = 20;
    const int NumLoopsPerBlock = 100000;

    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queue, ^{
            NSLog(@"Started block %d", i);
            for (int j = 0; j < NumLoopsPerBlock; j++)
            {
                fprintf(devNull, "Write to /dev/null\n");
            }
            NSLog(@"Finished block %d", i);
        });
    }

    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    fclose(devNull);

    return 0;
}
```

这个场景说明了使用 libdispatch 全局队列固有的延迟问题：在我的电脑上，前 4 个 `block` 立即启动，第一个在 1.5 秒后完成，此时下一个 `block` 才开始。最后一个 `block` 在入队 7.5 秒后才开始执行，并在第 9 秒完成。

虽然 libdispatch 中的全局队列被称为“并发”（concurrent），但它只在达到一个阈值之前是并发的。一旦并发槽位占满，全局队列就变成了串行（serial）——在这种情况下，限制被触发，串行特性增加了延迟。

如果这是一个负载很重的 Web 服务器，它不会对所有用户均匀地减慢速度，而是前几个用户获得响应，最后几个用户直接超时。

解决这类问题的方法是为每个 `block` 创建一个特定的队列。我们不把所有东西都推入全局队列（在我的测试电脑上限制为 4 个 `block`），而是为每个 `block` 创建一个单独的队列，使其能同时运行。

```objc
int main(int argc, const char * argv[])
{
    dispatch_group_t group = dispatch_group_create();
    FILE *devNull = fopen("/dev/null", "a");

    const int NumConcurrentBlocks = 20;
    dispatch_queue_t *queues = malloc(sizeof(dispatch_queue_t) * NumConcurrentBlocks);
    for (int q = 0; q < NumConcurrentBlocks; q++)
    {
        char label[20];
        sprintf(label, "Queue%d", q);
        queues[q] = dispatch_queue_create(label, NULL);
    }

    const int NumLoopsPerBlock = 100000;
    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queues[i], ^{
            NSLog(@"Started block %d", i);
            for (int j = 0; j < NumLoopsPerBlock; j++)
            {
                fprintf(devNull, "abcdefghijklmnopqrstuvwxyz\n");
            }
            NSLog(@"Finished block %d", i);
        });
    }

    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);
    fclose(devNull);

    return 0;
}
```

结果是所有 20 个 `block` 同时启动。它们都以大致相同的速度运行，并且大约在同一时间完成。

> **替代方案**：正如 Keith 在评论中建议的那样，由于这些操作是 I/O 密集型，而非 CPU 密集型，更好的解决方案是使用队列中的[文件写入源（file write source）](http://developer.apple.com/mac/library/documentation/General/Conceptual/ConcurrencyProgrammingGuide/GCDWorkQueues/GCDWorkQueues.html#//apple_ref/doc/uid/TP40008091-CH103-SW21)来代替标准的操作队列 `block`。文件写入源在 I/O 阻塞时会从队列中移除，这将允许所有 20 个源在全局并发队列（或任何其他单个队列）中公平地运行。

## 死锁

当一个 `block` 停止并等待第二个 `block` 完成，而第二个 `block` 因为需要第一个 `block` 持有的资源而无法进行时，就会发生死锁。

在以下程序中，有 20 个父 `block` 被入队（这将超出全局并发队列的受限资源）。每个父 `block` 都会生成一个子 `block`，该子 `block` 也被入队到同一个全局并发队列中。父 `block` 执行忙等待循环（busy wait loop），直到子 `block` 将其自身的整数添加到 `completedSubblocks` 集合中。

```objc
NSMutableSet *completedSubblocks;
NSLock *subblocksLock;

int main (int argc, const char * argv[])
{
    completedSubblocks = [[NSMutableSet alloc] init];
    subblocksLock = [[NSLock alloc] init];

    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();

    const int NumConcurrentBlocks = 20;
    for (int i = 0; i < NumConcurrentBlocks; i++)
    {
        dispatch_group_async(group, queue, ^{
            NSLog(@"Starting parent block %d", i);

            NSDate *endDate = [NSDate dateWithTimeIntervalSinceNow:1.0];
            while ([(NSDate *)[NSDate date] compare:endDate] == NSOrderedAscending)
            {
                // 忙等待 1 秒，让队列填满
            }

            dispatch_async(queue, ^{
                NSLog(@"Starting child block %d", i);

                [subblocksLock lock];
                [completedSubblocks addObject:[NSNumber numberWithInt:i]];
                [subblocksLock unlock];

                NSLog(@"Finished child block %d", i);
            });

            BOOL complete = NO;
            while (!complete)
            {
                [subblocksLock lock];
                if ([completedSubblocks containsObject:[NSNumber numberWithInt:i]])
                {
                    complete = YES;
                }
                [subblocksLock unlock];
            }

            NSLog(@"Finished parent block %d", i);
        });
    }

    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);

    [completedSubblocks release];
    [subblocksLock release];

    return 0;
}
```

在我的电脑上，前 8 个 `block` 被启动（填满了全局队列的并发 `block`），这些 `block` 阻塞了全局队列，导致子 `block` 永远无法运行。由于父 `block` 在等待子 `block`，而子 `block` 永远无法运行，结果就是死锁：程序永远无法完成。

你会注意到，对于 1 秒的延迟以及检测子 `block` 何时完成，我都使用了忙等待循环。通常，你会使用 `dispatch_sync` 来派发子 `block`（这是一种等待子 `block` 完成的不同方式），但实际情况是，当 libdispatch 使用其等待机制（或许多 Cocoa 或 OS 函数，如 `sleep`，它们类似地会放弃 CPU 时间）时，它足够聪明，能将一个 `block` 从其队列中移除。

虽然使用正确的函数来等待可以解决这个简单的示例，但它无法解决进程可能真正忙碌的情况。

最佳的解决方案是避免同一队列中 `block` 之间的依赖关系。

在类似的情况下，如果一个 `block`（子 `block`）消耗的时间很短，而另一个（父 `block`）很耗时（父 `block` 总是至少需要 1 秒），你可以简单地将这个消耗时间短的 `block` 放入一个单独的串行队列（serial queue）中。这将防止在所有情况下发生死锁。

在父子 `block` 都很耗时的情况下，你可以尝试：

- 为父 `block` 或子 `block` 的每次调用创建一个单独的队列，并将另一个放入全局队列中
- 将子 `block` 的功能合并到父 `block` 中，使其始终作为一个单独的 `block` 执行
- 仔细编写代码，确保任何依赖关系之前始终存在 libdispatch 的等待机制

## 结论

虽然 libdispatch 在简化并发多线程编程方面表现出色，但它并不能神奇地消除所有陷阱。

我在本文中探讨的问题，很大程度上是由于队列是共享资源这一事实造成的，并且在某些情况下，你必须小心资源是如何共享的。

从这个意义上说，这些问题并非直接与 libdispatch 相关（尽管我使用 libdispatch 来实现这些场景），它们是由于误用任何固定数量的服务器从队列中拉取数据的系统而可能引发的问题。

Grand Central Dispatch 的全局队列旨在用于 CPU 密集型操作。它将并发性限制为计算机的 CPU 数量，这对于 CPU 密集型操作是有益的；它能防止因任务切换而浪费 CPU 时间。这里的例子展示了其弊端：它可能会增加队列 `block` 的延迟，并且你需要小心同一队列上 `block` 之间的依赖关系。
