---
title: 'Friday Q&A 2009-09-11：Grand Central Dispatch 入门，第三部分：Dispatch Sources'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:66bed6781cfc2da7'
translated: true
---

> 原文：[Friday Q&A 2009-09-11: Intro to Grand Central Dispatch, Part III: Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)　·　mikeash.com Friday Q&A

发表于 2009-09-11 15:28 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[GCD 不是 Blocks，Blocks 不是 GCD](https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)
上一篇文章：[Friday Q&A 2009-09-04：Grand Central Dispatch 入门，第二部分：多核性能](https://www.mikeash.com/pyblog/friday-qa-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-09-11：Grand Central Dispatch 入门，第三部分：Dispatch Sources

作者：[Mike Ash](https://www.mikeash.com/)

请注意，我假定你已经阅读了本系列的前两篇文章。第一篇特别重要，第二篇次之。如果还没读过，请现在就去阅读。

在继续之前，本周有一些好消息：[GCD 已经开源](http://libdispatch.macosforge.org/)！这是 Apple 非常棒的一步。源代码相当整洁，读起来非常有趣。

**什么是 Dispatch Sources**
简而言之，dispatch source 是一个监控某种事件的对象（object）。当事件发生时，它会自动将一个 `block` 调度到 dispatch queue 上执行。

这听起来有点宽泛。我们说的是哪种事件呢？

以下是 10.6.0 中 GCD 支持的全部事件列表：

1. Mach 端口发送权状态（state）变化。
2. Mach 端口接收权状态变化。
3. 外部进程状态变化。
4. 文件描述符准备好读取。
5. 文件描述符准备好写入。
6. 文件系统节点事件。
7. POSIX 信号。
8. 自定义定时器。
9. 自定义事件。

这包含了很多有用的东西。它基本上涵盖了 `kqueue` 支持的所有内容，外加 Mach 端口、内置的定时器支持（不用再使用 timeout 参数自己构建了），以及自定义事件。

**自定义事件**
这些事件大多是不言自明的，但你可能会想知道自定义事件是什么。简而言之，这是一种通过调用 `dispatch_source_merge_data` 函数自己发出信号的事件。

对于发出事件信号的函数来说，这个名字有点奇怪。之所以这样命名，是因为 GCD 会自动合并（coalesce）在事件处理程序有机会运行之前发生的多个事件。你可以多次将数据“合并”（merge）到 dispatch source 中，如果 dispatch queue 在这整个期间都很忙，GCD 只会调用事件处理程序一次。

有两种类型的自定义事件可用：`DISPATCH_SOURCE_TYPE_DATA_ADD` 和 `DISPATCH_SOURCE_TYPE_DATA_OR`。自定义事件源有一个 `unsigned long` 类型的 `data` 属性，你也会向 `dispatch_source_merge_data` 传递一个 `unsigned long`。使用 `_ADD` 变体时，事件通过将所有数字相加来合并。使用 `_OR` 变体时，事件通过执行逻辑或来合并。当事件处理程序执行时，它可以使用 `dispatch_source_get_data` 访问当前值，然后数据会被重置为 0。

让我们看一个可能有用的场景。想象一些执行需要更新进度条的异步代码。由于主线程（main thread）对 GCD 来说只是另一个 dispatch queue，我们可以将 GUI 工作推送到主队列（main queue）上。然而，事件可能很多，我们不想对 GUI 进行冗余更新；如果主线程忙于其他工作，最好尽可能合并所有更改。

Dispatch sources 非常适合这种情况，使用 `DISPATCH_SOURCE_TYPE_DATA_ADD` 类型。我们可以合并已完成的工作量，然后主线程代码可以确定自上次事件以来完成了多少工作，并按该量更新进度指示符（progress indicator）。

说了这么多，来看一些代码：

```
    dispatch_source_t source = dispatch_source_create(DISPATCH_SOURCE_TYPE_DATA_ADD, 0, 0, dispatch_get_main_queue());
    dispatch_source_set_event_handler(source, ^{
        [progressIndicator incrementBy:dispatch_source_get_data(source)];
    });
    dispatch_resume(source);

    dispatch_apply([array count], globalQueue, ^(size_t index) {
        // 处理 index 处的数据
        dispatch_source_merge_data(source, 1);
    });
```

（关于这段代码，我想提一点，最初使用 dispatch sources 时曾让我无比困扰。这困扰了我很久，以至于我要用粗体表示。**Dispatch sources 总是以挂起状态启动！如果希望传递事件，必须在创建后恢复它们！**）

假设你已经将进度指示符配置为正确的 min/max 值，那么这一切将完美运行。数据将被并行处理。每完成一块数据，它就会向 dispatch source 发出信号，并将 dispatch source 数据加 1，我们将其视为已完成的工作单元数。事件处理程序按自上次运行以来已完成的工作单元数增加进度指示符。如果主线程空闲且工作单元完成得慢，事件处理程序将在每个工作单元完成时被调用，提供实时结果。如果主线程忙或工作单元完成得快，完成事件将被合并，进度指示符只会在主线程可以处理时更新一次。

这时你可能会想，这听起来不错，但如果我**不**希望事件被合并呢？有时候你只希望每个信号都引起一个操作，而不需要任何智能合并。其实，这实际上非常简单，你只需要换个角度思考。如果你希望每个信号都引起一个操作，请使用 `dispatch_async` 而不是 dispatch source。毕竟这就是它的作用：将一个 `block` 调度到目标队列上执行。事实上，使用 dispatch source 而不是 `dispatch_async` 的唯一原因就是为了利用合并功能。

**内置事件**
这就是如何使用自定义事件，那内置事件呢？让我们看一个使用 GCD 从标准输入读取的示例：

```
    dispatch_queue_t globalQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_source_t stdinSource = dispatch_source_create(DISPATCH_SOURCE_TYPE_READ,
                                                           STDIN_FILENO,
                                                           0,
                                                           globalQueue);
    dispatch_source_set_event_handler(stdinSource, ^{
        char buf[1024];
        int len = read(STDIN_FILENO, buf, sizeof(buf));
        if(len > 0)
            NSLog(@"Got data from stdin: %.*s", len, buf);
    });
    dispatch_resume(stdinSource);
```

这非常简单！因为我们使用了全局队列（global queue），处理程序会自动在后台运行，与应用程序的其余部分并行，这意味着如果事件发生时应用程序正在做其他事情，会自动获得并行加速。

与标准的 UNIX 方式相比，这还有一个很好的好处，即无需编写循环。使用典型的 `read` 调用时，你必须始终保持警惕，因为它返回的数据可能比请求的少，并且还可能遭受像 `EINTR`（被中断的系统调用）这样的瞬时“错误”。使用 GCD，在这些情况下你可以直接退出而不做任何事。如果你在文件描述符上留下了未读取的数据，GCD 将再次调用你的处理程序。

对于标准输入来说这不是问题，但对于其他文件描述符，你需要考虑在完成读取（或写入）描述符后如何清理。你不能在 dispatch source 仍然活跃时关闭描述符。如果另一个文件描述符被创建（可能来自另一个线程）并且碰巧得到了相同的编号，你的 dispatch source 将突然读取（或写入）它不应该接触的东西。调试起来会非常不愉快。

正确实现清理的方法是使用 `dispatch_source_set_cancel_handler`，并为其提供一个关闭文件描述符的 `block`。然后，你可以使用 `dispatch_source_cancel` 取消 dispatch source，导致处理程序被调用，文件描述符被关闭。

使用其他 dispatch source 类型也非常类似。通常，你将源的标识符（mach 端口、文件描述符、进程 ID 等）作为 dispatch source 的句柄（handle）。`mask` 参数通常不使用，但对于 `DISPATCH_SOURCE_TYPE_PROC`，它指示你感兴趣接收的进程事件类型。然后只需提供一个处理程序，恢复 source，就大功告成了。这些 dispatch source 还提供特定于源的数据，可以使用 `dispatch_source_get_data` 函数访问。例如，文件描述符会将描述符上可用的大致字节数作为 dispatch source 数据。进程源会提供一个掩码，指示自上次调用以来发生的事件。有关每种 source 类型数据含义的完整列表，请参阅 man 页面。

**定时器**
定时器事件有点不同。它们不使用 `handle`/`mask` 参数，而是使用一个单独的函数 `dispatch_source_set_timer` 来配置定时器。此函数接受三个单独的参数来控制定时器何时触发：

`start` 参数控制定时器的首次触发时间。此参数的类型是 `dispatch_time_t`，这是一个不透明类型，你不能直接操作。函数 `dispatch_time` 和 `dispatch_walltime` 可用于创建它们，如果你需要这些值，可以使用常量 `DISPATCH_TIME_NOW` 和 `DISPATCH_TIME_FOREVER`。

`interval` 参数是一个整数，不言而喻。`leeway` 参数则很有趣。这个参数告诉系统你希望定时器触发的精度有多高。定时器永远不能保证 100% 精确，但这个参数让你告诉系统你希望它多努力。如果你希望定时器每 5 秒触发一次，并且尽可能精确，可以传递 0。另一方面，考虑一个周期性的任务，比如检查新邮件。你想每 10 分钟检查一次，但这不必精确。你可以传递 60 秒的 leeway，告诉系统你接受定时器在计划时间后最多 60 秒内触发。

这有什么意义呢？简而言之，降低功耗。相比起在休眠和唤醒之间不断循环以分散地完成任务，如果操作系统能够让 CPU 尽可能长时间地休眠，然后在唤醒时一次性完成一大堆事情，能效会更高。通过为定时器提供较大的 leeway，你可以让系统将你的定时器与其他操作合并，从而将任务分组在一起。

**结论**
现在你知道了如何使用 GCD 的 dispatch source 工具来监控文件描述符、运行定时器、合并自定义事件以及执行其他类似活动。由于 dispatch sources 与 dispatch queues 完全集成，你可以使用任何可用的 dispatch queue。你可以让 dispatch source 在主线程上运行其处理程序，在其中一个全局队列上并行运行，或者通过使用自定义队列，与程序的特定模块序列化运行。

本周就到这里。下周我将结束 Grand Central Dispatch 的讨论，并谈谈如何挂起、恢复和重定向 dispatch queues，如何使用 dispatch semaphores，以及如何使用 GCD 的一次性初始化工具。和往常一样，如果你对未来的 Friday Q&A 有什么主题建议，请在评论中发表或[直接给我发邮件](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我正在出售满是这些内容的整本书！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上提供。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)

添加你的想法，发表评论：

垃圾邮件和跑题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
