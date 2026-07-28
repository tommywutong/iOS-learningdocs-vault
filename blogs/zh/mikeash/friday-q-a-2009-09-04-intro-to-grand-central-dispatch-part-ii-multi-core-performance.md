---
title: 'Friday Q&A 2009-09-04：Grand Central Dispatch 入门，第二部分：多核性能'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:59746460e04f7c7b'
translated: true
---

> 原文：[Friday Q&A 2009-09-04: Intro to Grand Central Dispatch, Part II: Multi-Core Performance](https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)　·　mikeash.com Friday Q&A

发布于 2009-09-04 01:51 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2009-09-11：Grand Central Dispatch 入门，第三部分：Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)
上一篇：[Mobile Orchard 上的 Objective-C Runtime 播客节目](https://www.mikeash.com/pyblog/objective-c-runtime-podcast-episode-at-mobile-orchard.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-04：Grand Central Dispatch 入门，第二部分：多核性能

作者：[Mike Ash](https://www.mikeash.com/)

**概念**
为了在单个进程内利用多个 CPU 核心，必须使用多个线程。（我忽略多进程并发，因为它与 GCD 无关。）这在 GCD 世界里和纯线程世界里同样成立。在底层，GCD 全局分发队列（global dispatch queue）只是工作者线程（worker thread）池的抽象。这些队列上的 `block` 在工作者线程可用时被分派到上面。提交到自定义队列的 `block` 最终会经过全局队列，进入同一组工作者线程池。（除非你的自定义队列以主线程为目标，但你不会为了速度这么做！）

从 GCD 中提取多核性能的基本方法有两种：将单个任务或一组相关任务并行化到某个全局队列上，以及将多个无关或松散相关的任务并行化到多个自定义队列上。

**全局队列**
想象以下循环：

```
    for(id obj in array)
        [self doSomethingIntensiveWith:obj];
```

假设 `-doSomethingIntensiveWith:` 是线程安全的，并且可以与该方法的其他使用并行运行。如果确实如此，且 `array` 中经常包含多个对象，那么很容易使用 GCD 并行化此代码：

```
    dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    for(id obj in array)
        dispatch_async(queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
```

就这么简单，你就在多个核心上运行了。

当然，代码并不总是这么友好。有时你有操作数组的代码，但随后必须用结果执行一些工作：

```
    for(id obj in array)
        [self doSomethingIntensiveWith:obj];
    [self doSomethingWith:array];
```

在 GCD 示例中使用 `dispatch_async` 意味着这行不通。而且你不能只通过改用 `dispatch_sync` 来解决，因为那会导致每个迭代阻塞，破坏所有并行性。

解决这个问题的一种方法是使用 dispatch 组（dispatch group）。dispatch 组是一种将多个 `block` 分组在一起的方式，可以等待它们完成，也可以在它们完成后得到通知。它们通过 `dispatch_group_create` 创建，`dispatch_group_async` 函数允许向 dispatch 队列提交 `block` 并将其添加到组中。然后我们可以这样重写此代码以使用 GCD：

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
    for(id obj in array)
        dispatch_group_async(group, queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
    dispatch_release(group);

    [self doSomethingWith:array];
```

如果此工作可以相对于调用代码异步执行，那么我们可以做得更花哨，在后台运行 `-doSomethingWith:` 而不是等待。为此，我们将使用 `dispatch_group_notify` 来设置一个在组完成时运行的 `block`：

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_group_t group = dispatch_group_create();
    for(id obj in array)
        dispatch_group_async(group, queue, ^{
            [self doSomethingIntensiveWith:obj];
        });
    dispatch_group_notify(group, queue, ^{
        [self doSomethingWith:array];
    });
    dispatch_release(group);
```

现在不仅对数组对象的所有工作都会并行运行，而且最终工作也会相对于 App 的其余部分异步执行，从而提供更多的并行性。请注意，如果 `-doSomethingWith:` 需要在主线程上运行，例如操作 GUI，你只需将主队列（main queue）而不是全局队列传递给 `dispatch_group_notify`。

对于同步情况，GCD 提供了 `dispatch_apply` 函数作为便捷捷径。该函数并行多次调用单个 `block` 并等待其完成，就像我们想要的那样：

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_apply([array count], queue, ^(size_t index){
        [self doSomethingIntensiveWith:[array objectAtIndex:index]];
    });
    [self doSomethingWith:array];
```

这很好，但异步情况呢？没有我们可以使用的 `dispatch_apply` 的异步版本。但我们正在使用基于异步调用的 API！我们可以直接用 `dispatch_async` 将整个事情推入后台：

```
    dispatch_queue_t queue = dispatch_get_global_qeueue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_async(queue, ^{
        dispatch_apply([array count], queue, ^(size_t index){
            [self doSomethingIntensiveWith:[array objectAtIndex:index]];
        });
        [self doSomethingWith:array];
    });
```

简单！

这种方法的关键是识别出对许多不同数据片段同时执行相同工作的代码。如果你确保所执行的工作以线程安全的方式完成（超出本篇范围），那么你可以将循环替换为对 GCD 的调用以实现并行性。

为了看到性能提升，你需要执行相当大量的工作。与线程相比，GCD 轻量且开销低，但提交一个 `block` 到队列仍然有点昂贵。必须复制并排队 `block`，并以某种方式通知相应的工作者线程。为图像中的每个像素提交一个 `block` 可能不会带来好处。另一方面，在转换图像集合（collection）时为每个图像提交一个 `block` 可能会带来好处。GCD 不再有利可图的点位于两者之间。如有疑问，请进行实验。并行化 App 是一种优化，因此你应该始终在前后进行测量，以确保你的更改有帮助。（并确保你在正确的地方进行更改！）

**子系统并行**
前一节讨论了在 App 的单个子系统中利用多个核心。跨多个子系统这样做也很有用。

例如，想象一个 App 打开一个包含元数据的文稿（document）。文稿数据本身必须被解析并转换为用于显示的数据模型对象，元数据也是如此。然而，文稿数据和元数据并不交互。你可以为每个创建一个 dispatch 队列，然后并行运行它们。每块数据解析的代码在其内部完全是串行的，并且线程安全问题无需担心（只要它们之间没有共享数据），但它们仍然会并行运行。

文稿打开后，程序需要执行任务以响应用户操作。例如，它可能需要执行拼写检查、语法高亮、字数统计、自动保存以及其他此类事情。如果每个任务都使用单独的 dispatch 队列实现，它们将彼此并行运行，而无需多线程编程的许多困难。

通过使用 dispatch sources（我将在下周介绍），你可以让 GCD 直接将事件传递到自定义 dispatch 队列。例如，程序中监控网络套接字的部分可以被赋予其自己的 dispatch 队列，这将使其能够相对于 App 的其余部分并行运行。此外，通过使用自定义队列，此模块相对于自身将串行运行，从而简化编程。

**结论**
本周我们看到了如何使用 GCD 来提高 App 的性能并利用现代多核系统。尽管在编写并行 App 时仍需小心，但 GCD 使得利用所有可用计算能力比以往任何时候都更容易。

本周的 Friday Q&A 到此结束。下周请回来继续阅读 GCD 系列的下一个部分，届时我将讨论 dispatch sources——GCD 用于监控内部和外部事件的机制。像往常一样，如果你有关于某个主题的建议，请在评论中发表或[直接给我发邮件](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我正在销售包含这些文章的全套书籍！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
