---
title: 'Friday Q&A 2009-09-18：Grand Central Dispatch 入门，第四部分：杂项'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f720aa9e24094594'
translated: true
---

> 原文：[Friday Q&A 2009-09-18: Intro to Grand Central Dispatch, Part IV: Odds and Ends](https://www.mikeash.com/pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html)　·　mikeash.com Friday Q&A

发布于 2009-09-18 17:23 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2009-09-25: GCD 实践](https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html)
上一篇：[iPhone 开发故事：一年之后](https://www.mikeash.com/pyblog/the-iphone-development-story-one-year-later.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-18：Grand Central Dispatch 入门，第四部分：杂项

作者：[Mike Ash](https://www.mikeash.com/)

与前几周一样，我假设你在阅读本文之前已经阅读了之前的所有文章，因此熟悉到目前为止讨论的 GCD 的所有方面。如果还没有阅读过这些文章，请现在就阅读。

**暂停调度队列**
 调度队列（dispatch queue）可以随时暂停和恢复。要暂停，使用 `dispatch_suspend` 函数；要恢复，使用 `dispatch_resume`。它们的工作方式与你的预期基本一致。请注意，它们也适用于调度源（dispatch source）。

暂停调度队列的一个注意事项是，暂停是 block 粒度的。换句话说，暂停一个队列*不会*暂停当前正在执行的 block。实际情况是，允许当前 block 执行完毕，然后在该队列（或源）恢复之前，不允许再运行任何 block。

最后一点说明，直接来自手册页：如果你之前暂停了一个队列/源，那么*必须*在销毁它之前恢复它。

**调度队列目标**
 所有自定义调度队列都有目标队列的概念。本质上，自定义调度队列并不实际执行任何工作，而是将工作传递给其目标队列来执行。通常情况下，自定义队列的目标队列是默认优先级的全局队列。

自定义队列的目标队列可以通过 `dispatch_set_target_queue` 函数来设置。你可以向其传递任何其他调度队列，甚至是另一个自定义队列，只要你不创建循环。此函数可以通过简单地将自定义队列的目标队列设置为不同的全局队列来设置其优先级。如果你将自定义队列的目标设置为低优先级全局队列，则你的自定义队列上的所有工作都将以低优先级执行，对于高优先级全局队列也是如此。

另一个潜在的用途是将自定义队列的目标设为主队列。这将使得提交到该自定义队列的所有 block 都在主线程上运行。与直接使用主队列相比，这样做的好处是，你的自定义队列可以被独立地暂停和恢复，并且之后可能会被重新定位到全局队列，尽管你需要小心确保在此之后运行的所有 block 能够容忍不在主线程上运行！

还有一个潜在的用途是将自定义队列目标设为其他自定义队列。这将强制多个队列相对于彼此串行化，并实质上创建了一组队列，这些队列可以通过暂停/恢复它们所指向的队列来实现整体暂停和恢复。至于如何使用这种方法，想象一个正在扫描一组目录并加载其中文件的 App。为了避免磁盘争用，你需要确保每个物理磁盘上只有一个文件加载任务处于活动状态。然而，可以从物理上独立的磁盘同时读取多个文件。要实现这一点，你只需要构建一个反映磁盘结构的调度队列结构。

首先，你需要扫描系统并找到磁盘，为每个磁盘创建一个自定义调度队列。然后，你需要扫描文件系统，并为每个文件系统也创建一个自定义队列，将其目标队列指向相应磁盘的队列。最后，每个目录扫描器也可以有自己的队列，将目标指向目录所在文件系统的队列。目录扫描器可以枚举其目录，并直接为每个文件向自己的队列提交一个 block。由于系统的设置方式，这将固有地串行化对每个物理磁盘的所有访问，同时允许对不同的磁盘进行并行访问，除了初始队列设置过程之外，无需任何手动干预。

**信号量**
 调度信号量（dispatch semaphore）的工作方式与其他任何信号量一样，如果你熟悉其他多线程系统中的信号量，那么这对你来说会非常熟悉。

信号量本质上是一个整数，它具有初始计数值，并支持两个操作：signal（信号）和 wait（等待）。当信号量被发信号时，计数值递增。当线程在信号量上等待时，它将阻塞（如有必要），直到计数值大于 0，然后递减计数值。

使用 `dispatch_semaphore_create` 创建调度信号量，使用 `dispatch_semaphore_signal` 发信号，使用 `dispatch_semaphore_wait` 等待。这些函数的手册页展示了两个使用信号量的好例子，一个涉及同步工作完成，另一个涉及控制对有限资源的访问。我不打算自己编写更差的示例，而是建议你直接阅读手册页，了解这些对象的一些潜在用途。

**一次性初始化**
 GCD 还支持一次性初始化，如果你熟悉 pthread，这基本上与 `pthread_once` 调用相同。GCD 方法的主要优点是它使用 block 而不是函数指针，从而允许更自然的代码流程。

其中一个主要用途是以线程安全的方式懒加载初始化单例或其他共享数据。对于需要线程安全的单例，典型的单例初始化技术如下所示：

```
    + (id)sharedWhatever
    {
        static Whatever *whatever = nil;
        @synchronized([Whatever class])
        {
            if(!whatever)
                whatever = [[Whatever alloc] init];
        }
        return whatever;
    }
```

这没问题，但代价高昂；每次调用 `+sharedWhatever` 都会产生获取锁的开销，尽管这个锁基本上只需要一次。还有更花哨的方法，例如使用双重检查锁定或原子操作，但它们既困难又极其容易出错。

使用 GCD，你可以使用 `dispatch_once` 重写上述方法，如下所示：

```
    + (id)sharedWhatever
    {
        static dispatch_once_t pred;
        static Whatever *whatever = nil;
        dispatch_once(&pred, ^{
            whatever = [[Whatever alloc] init];
        });
        return whatever;
    }
```

这实际上比 `@synchronized` 方法稍微简单一些，而且 GCD 确保以一种快速的方式执行这些检查。它确保在任意线程能够越过 `dispatch_once` 调用之前，block 中的代码已经运行完毕，但不会强制代码在每次使用此函数时都承担同步的开销。事实上，如果你查看声明此函数的头文件，你会发现当前的实现实际上是一个宏，它在内联执行初始测试，这意味着在常见情况下，你甚至不会产生*函数调用*的开销，更不用说同步开销了。

**结论**
 这就结束了关于 Grand Central Dispatch 的系列文章。本周你了解了如何暂停、恢复和重新定位调度队列，以及这些功能的一些用途。你还了解了如何使用调度信号量和一次性初始化功能。在前几周，你了解了如何管理调度对象，如何创建/访问和使用不同类型的调度队列来完成不同的任务，利用多核系统的策略，以及如何使用 GCD 的事件系统监视事件。现在，你已经完整掌握了 GCD 如何运作以及如何使用它，所以去用它编写一些出色的新软件吧！

下周五 Q&A 再见。一如既往，如果你有想要探讨的主题建议，请将其发布在评论中或[直接给我发邮件](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我现在在售卖包含这些文章的整套书籍！第二卷和第三卷已出炉！它们有 ePub、PDF、纸质版以及 iBooks 和 Kindle 格式。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。屡犯者可能会在由我自行决定的公开羞辱中受到惩罚。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
