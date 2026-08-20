---
title: 'Friday Q&A 2009-09-25：GCD 实践'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1caafbd18fd5ad2d'
translated: true
---

> 原文：[Friday Q&A 2009-09-25: GCD Practicum](https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html)　·　mikeash.com Friday Q&A

发布于 2009-09-25 11:52 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-10-02：Care and Feeding of Singletons](https://www.mikeash.com/pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html)  
上一篇：[Friday Q&A 2009-09-18：Grand Central Dispatch 入门，第四部分：零碎事项](https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [性能](https://www.mikeash.com/pyblog/?tag=performance) [源代码](https://www.mikeash.com/pyblog/?tag=sourcecode)

Friday Q&A 2009-09-25：GCD 实践

作者：[Mike Ash](https://www.mikeash.com/)

**概述**  
我将分四步讲解如何对这个程序进行并行化。第一步是基本的串行程序，后续步骤会逐步将其构建成一个使用 GCD 的完全并行程序。如果你想跟着做，可以[下载全部四步的完整源代码](https://www.mikeash.com/pyblog/imagegcd.zip)。但不要运行 `imagegcd2.m`。稍后你会明白原因。

**原始程序**  
我们要处理的程序很简单，它会遍历 `~/Pictures` 目录中的内容，并为其生成缩略图。这是一个纯命令行程序，虽然大部分工作使用了 Cocoa。它的 main 函数如下：

```
    int main(int argc, char **argv)
    {
        NSAutoreleasePool *outerPool = [NSAutoreleasePool new];
        
        NSApplicationLoad();
        
        NSString *destination = @"/tmp/imagegcd";
        [[NSFileManager defaultManager] removeItemAtPath: destination error: NULL];
        [[NSFileManager defaultManager] createDirectoryAtPath: destination
                                        withIntermediateDirectories: YES
                                        attributes: nil
                                        error: NULL];
        
        
        Start();
        
        NSString *dir = [@"~/Pictures" stringByExpandingTildeInPath];
        NSDirectoryEnumerator *enumerator = [[NSFileManager defaultManager] enumeratorAtPath: dir];
        int count = 0;
        for(NSString *path in enumerator)
        {
            NSAutoreleasePool *innerPool = [NSAutoreleasePool new];
            
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                path = [dir stringByAppendingPathComponent: path];
                
                NSData *data = [NSData dataWithContentsOfFile: path];
                if(data)
                {
                    NSData *thumbnailData = ThumbnailDataForData(data);
                    if(thumbnailData)
                    {
                        NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg", count++];
                        NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                        [thumbnailData writeToFile: thumbnailPath atomically: NO];
                    }
                }
            }
            
            [innerPool release];
        }
        
        End();
        
        [outerPool release];
    }
```

完整的代码清单（包括所有辅助函数）请[参考配套的源代码下载](https://www.mikeash.com/pyblog/imagegcd.zip)。这个程序是 `imagegcd1.m`。不过重要的部分都在这里了。`Start` 和 `End` 只是使用 `gettimeofday` 的简单计时函数。`ThumbnailDataForData` 使用 Cocoa 将数据加载为图像，将其按比例缩小至不超过 320x320，然后将结果编码为 JPEG。

**幼稚的并行化**  
初看起来，这个程序很容易并行化。循环的每次迭代都可以推送到 GCD 的全局队列上。我们可以通过 dispatch group 来等待所有任务完成。最后一个技巧：为了确保每次迭代仍能获得唯一的文件名编号，我们将使用 `OSAtomicIncrement32` 对 `count` 进行原子递增。新代码如下：

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(0, 0);
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                NSString *fullPath = [dir stringByAppendingPathComponent: path];
                
                NSData *data = [NSData dataWithContentsOfFile: fullPath];
                if(data)
                {
                    NSData *thumbnailData = ThumbnailDataForData(data);
                    if(thumbnailData)
                    {
                        NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                   OSAtomicIncrement32(&count;)];
                        NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                        [thumbnailData writeToFile: thumbnailPath atomically: NO];
                    }
                }
            }
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

这个程序是 `imagegcd2.m`。但**不要运行它！**

如果你无视了我的警告并运行了它，大概现在正在重启电脑后重新加载这个页面。如果你还没有运行，那么会发生的情况是（至少在你有很多图片的情况下），你的电脑会卡死，而且除非你能等待比预期长得多的时间，否则很可能无法修复。

**问题所在**  
是什么导致了所有这些麻烦？问题出在 GCD 的智能上。GCD 在一个全局线程池上运行任务，线程池的大小会根据系统负载进行缩放。例如，我的电脑有四个核心，所以如果我用任务塞满 GCD，GCD 会运行四个工作线程来占满所有核心。如果电脑上的其他程序开始工作，GCD 会稍微缩减线程数量，为其他任务留出空间。

然而，GCD 也可能会**增加**活跃线程的数量。如果某个工作线程阻塞了，就会发生这种情况。想象这四个工作线程正在运行，然后其中一个突然做了类似读取文件这样的事情。它去等待磁盘，而你的核心就被闲置了。GCD 会看到这种情况，并生成另一个工作线程来填补空缺。

现在，想想这里会发生什么。主循环非常快地将任务推送到全局队列上。GCD 会启动几个工作线程，并开始从队列中取出任务。这些任务一开始只做很少的工作，然后立即去从磁盘读取文件。那块缓慢的、旋转的磁盘。

而且别忘了磁盘的另一个重要特性：除非你有 SSD 或 fancy 的 RAID，否则**它们在争用情况下会变得慢得多**。

这前四个任务同时命中磁盘，磁盘疯狂地试图同时满足四个请求。GCD 只看 CPU 使用率，发现 CPU 核心大部分空闲，于是开始生成更多工作线程。这些线程也猛撞磁盘这堵墙，导致 GCD 进一步生成更多线程，等等。

最终，文件读取开始完成。现在，不再是四个核心对应四个线程，而是有上百个。如果使用 CPU 时间的工作线程太多，GCD 会缩减数量，但它在缩减时机上受到限制。它不能在一个任务执行中途杀死工作线程，甚至不能暂停它们。它必须等到整个任务完成后，才能杀死该任务所在的线程。所有这些正在处理中的任务阻止了 GCD 减少工作线程数量。

这数百个线程开始完成图像数据的读取并开始处理。它们在 CPU 上也会相互妨碍，尽管 CPU 处理争用的能力比磁盘好得多。问题是，这些线程在获取文件数据后做的第一件事就是解码。如果你有很多 JPEG 文件，这些图像数据会膨胀 10 倍或更多。如果有数百个这样的任务同时进行，你就会开始耗尽内存。物理 RAM 用完了会发生什么？更多的磁盘使用！

现在你陷入了一个恶性反馈循环。磁盘争用导致更多工作线程，进而导致更多内存使用，进而导致更多磁盘争用。这个过程会失控，直到 GCD 达到其 512 个工作线程的极限。以典型的图片大小来说，512 个正在处理的任务足以让你的系统陷入交换地狱，并且需要很长时间才能恢复。很可能你在一段时间内甚至无法杀死这个任务。

这是你在使用 GCD 时真正需要注意的一点。GCD 在限制 CPU 使用的并发任务数量方面非常出色，但对于其他资源的争用它却无能为力。如果你的任务涉及 IO 或任何可能导致阻塞的操作，你必须警惕这个问题。

**解决方法**  
整个问题的根源是 IO 争用导致的失控反馈。消除争用，问题就解决了。

GCD 通过自定义队列让这变得很容易。自定义队列本质上是串行的。如果我们专门为 IO 创建一个自定义队列，并将所有文件读取/写入操作都放到该队列上，那么磁盘每次只会被命中一个文件，争用也就消失了。

这是使用 IO 队列改造后的程序主循环：

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(0, 0);
    dispatch_queue_t ioQueue = dispatch_queue_create("com.mikeash.imagegcd.io", NULL);
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
        {
            NSString *fullPath = [dir stringByAppendingPathComponent: path];
            
            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                NSData *data = [NSData dataWithContentsOfFile: fullPath];
                if(data)
                    dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
                        NSData *thumbnailData = ThumbnailDataForData(data);
                        if(thumbnailData)
                        {
                            NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                       OSAtomicIncrement32(&count;)];
                            NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                                [thumbnailData writeToFile: thumbnailPath atomically: NO];
                            }));
                        }
                    }));
            }));
        }
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

这个程序是 `imagegcd3.m`。GCD 让通过简单的嵌套将任务的不同部分推送到不同队列变得如此简单，真是太棒了。这个程序会在……大部分情况下表现得相当不错。

问题是它本质上不稳定，因为不同的部分没有同步。这段代码中的数据流如下：

```
    Main Thread          IO Queue            Concurrent Queue
    
    find paths  ------>  read  ----------->  process
                                             ...
                         write <-----------  process
```

图中的箭头是**非阻塞**的，并且只是缓冲正在传递的对象。

现在想象一台机器，其磁盘速度足够快，读取文件的速度比 CPU 处理它们的速度还快。这并不难想象：虽然 CPU 快得多，但它做的工作量也**大得多**。从磁盘读取的数据开始在队列中堆积。这些数据占用内存，如果你有很多大图片，可能会占用大量内存。

然后你耗尽了物理 RAM，开始交换。

这可能导致另一个像第一个那样的失控反馈循环。如果任何原因导致工作线程阻塞，GCD 会分出一个新线程，新线程会立即开始尝试分配大量内存，并因持续的内存压力而阻塞。GCD 会分出更多任务，导致更多内存压力，然后你又回到了交换地狱。

这个反馈的有趣之处在于，与第一次 GCD 尝试不同，它在某种程度上是自我调节的。随着 IO 争用达到顶峰，IO 队列会停止，直到情况恢复正常后才会取得显著进展。一旦恢复正常，你又回到低内存使用率和良好吞吐量的状态，直到缓冲数据再次积累过多。

最终结果是：程序在平滑处理和陷入困境之间交替。

注意，如果磁盘更慢，同样的问题仍然可能出现，因为缩略图会在运行结束时被缓冲，但由于数据量小得多，问题可能会轻得多。

**真正解决问题**  
既然上次尝试的问题在于操作的不同阶段之间缺乏同步，那我们就来同步它们。简单的方法是使用信号量（semaphore）来限制任意时刻正在处理的任务数量。

还剩一个问题：我们应该允许多少个任务？

显然，它应该随系统中的 CPU 核心数量而变化，因为我们想充分利用可用的资源。但是，简单地限制为核心数量是个坏主意，因为每个任务的大部分时间都是 IO。也不能太高，否则我们会耗尽内存。

我决定将任务数量设为核心数的两倍。我的推理是，这会使任务数量扩展到 IO 时间等于处理时间为止。如果 IO 时间比处理时间长，那么 IO 本身就是瓶颈，因此让并发任务数超过这个值没有意义。如果 IO 时间明显少于处理时间，那么 GCD 会自动将工作线程数量保持得足够低，以确保 CPU 上的争用最小。

主循环现在的样子如下：

```
    dispatch_queue_t ioQueue = dispatch_queue_create("com.mikeash.imagegcd.io", NULL);
    
    int cpuCount = [[NSProcessInfo processInfo] processorCount];
    dispatch_semaphore_t jobSemaphore = dispatch_semaphore_create(cpuCount * 2);
    
    dispatch_group_t group = dispatch_group_create();
    __block uint32_t count = -1;
    for(NSString *path in enumerator)
    {
        WithAutoreleasePool(^{
            if([[[path pathExtension] lowercaseString] isEqual: @"jpg"])
            {
                NSString *fullPath = [dir stringByAppendingPathComponent: path];
                
                dispatch_semaphore_wait(jobSemaphore, DISPATCH_TIME_FOREVER);
            
                dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                    NSData *data = [NSData dataWithContentsOfFile: fullPath];
                    dispatch_group_async(group, globalQueue, BlockWithAutoreleasePool(^{
                        NSData *thumbnailData = ThumbnailDataForData(data);
                        if(thumbnailData)
                        {
                            NSString *thumbnailName = [NSString stringWithFormat: @"%d.jpg",
                                                       OSAtomicIncrement32(&count;)];
                            NSString *thumbnailPath = [destination stringByAppendingPathComponent: thumbnailName];
                            dispatch_group_async(group, ioQueue, BlockWithAutoreleasePool(^{
                                [thumbnailData writeToFile: thumbnailPath atomically: NO];
                                dispatch_semaphore_signal(jobSemaphore);
                            }));
                        }
                        else
                            dispatch_semaphore_signal(jobSemaphore);
                    }));
                }));
            }
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

现在我们终于有了一个运行流畅、处理快速的程序。

**基准测试**  
我在包含 7913 张图片的库上获得了以下运行时间：

| **程序** | **时间（秒）** |
|---|---|
| `imagegcd1.m` | 984 |
| `imagegcd2.m` | 未运行 |
| `imagegcd3.m` | 300 |
| `imagegcd4.m` | 279 |

请注意，因为我比较懒，在运行之前没有关闭其他所有程序，所以程序没有完全独占 CPU。考虑到这一点，对于我的 4 个 CPU 核心来说，总共 3.5 倍的加速已经相当不错了。

有趣的是，版本 3 表现得还不错。我确实观察到它表现出我之前讨论的循环行为，但不是很频繁。这很可能是因为我的机器有 15GB 的 RAM。在内存较少的系统上，它的表现可能会差得多。我观察到它一度使用了高达 10GB 的 RAM。如果我将其编译为 32 位，它会迅速耗尽虚拟内存并崩溃。版本 4 从未使用任何显著数量的 RAM。

**结论**  
GCD 是一项了不起的技术，做了很多有用的事情，但它不能为你包办一切。特别是，执行 IO 并可能消耗大量内存的并发任务必须仔细管理。即便如此，GCD 提供的工具也使得构建一个不会压垮计算机资源的系统变得容易。

本周的 Friday Q&A 就到此为止。下周再来参加另一期精彩的内容。与此同时，[把你的讨论主题发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我出了整本书来收录它们！第二卷和第三卷现已推出！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-25-gcd-practicum.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
