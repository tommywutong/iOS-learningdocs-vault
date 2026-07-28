---
title: 'Friday Q&A 2009-08-28：Grand Central Dispatch 入门（第一部分）：基础与派发队列'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6a7f7ec4e5b73876'
translated: true
---

> 原文：[Friday Q&A 2009-08-28: Intro to Grand Central Dispatch, Part I: Basics and Dispatch Queues](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html)　·　mikeash.com Friday Q&A

发表于 2009-08-28 14:16 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Mobile Orchard 上的 Objective-C Runtime 播客集](https://www.mikeash.com/pyblog/objective-c-runtime-podcast-episode-at-mobile-orchard.html)  
上一篇：[Unicode 注释支持](https://www.mikeash.com/pyblog/unicode-comments-support.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-08-28：Grand Central Dispatch 入门（第一部分）：基础与派发队列

作者：[Mike Ash](https://www.mikeash.com/)

**它是什么？**  
 Grand Central Dispatch（简称 GCD）是一个底层 API，它引入了一种新的方式来执行并发编程。就基本功能而言，它有点像 NSOperationQueue，因为它允许将程序的工作划分为独立的任务（task），然后将这些任务提交到工作队列以并发或串行执行。它比 NSOperationQueue 更底层、性能更高，并且不属于 Cocoa 框架（framework）。

除了提供并行执行代码的能力外，GCD 还提供了一个完全集成的事件处理系统。可以设置处理程序，以响应文件描述符、mach 端口、进程、定时器、信号以及用户生成的事件。这些处理程序通过 GCD 的并发执行机制来运行。

GCD 的 API 在很大程度上基于 `block`，我在之前的 Friday Q&A 中讨论过它，首先是[介绍 `block` 的基础知识](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html)，然后是[讨论在实际代码中使用 `block` 的实用方面](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)。虽然 GCD 可以不使用 `block`，而是使用传统的 C 机制（提供函数指针和上下文指针），但从实际角度来看，与 `block` 一起使用会更容易、功能也更强大。

有关 GCD 的文档，请查看 Snow Leopard 机器上的 `man dispatch`。

**为什么要用它？**  
 与传统的多线程编程相比，GCD 具有许多优势：

1. **易于使用：** GCD 比线程（thread）更容易使用。因为它基于工作单元而非计算线程，所以可以处理常见任务，例如等待工作完成、监控文件描述符、定期执行代码以及暂停工作。基于 `block` 的 API 使得在不同代码段之间传递上下文变得极其容易。
2. **高效率：** GCD 以轻量级方式实现，使得在许多创建专用线程代价过高的地方使用 GCD 变得实用且快速。这与易于使用有关：GCD 如此易于使用的部分原因在于，大多数情况下你只需使用它，而无需过于担心其效率问题。
3. **高性能：** GCD 会根据系统负载自动调整线程的使用，从而减少上下文切换并提高计算效率。

**派发对象（Dispatch Objects）**  
 尽管是纯 C 语言，但 GCD 是以面向对象的风格构建的。GCD 对象被称为派发对象（dispatch objects）。派发对象使用引用计数，与 Cocoa 对象非常相似。`dispatch_retain` 和 `dispatch_release` 函数可用于管理派发对象的引用计数以实现内存管理。请注意，与 Cocoa 对象不同，派发对象**不**参与垃圾回收，因此即使你启用了 GC，也必须手动管理 GCD 对象。

派发队列和派发源（dispatch sources）（稍后会详细介绍）可以暂停和恢复，可以关联任意的上下文指针，还可以关联一个终结器函数。有关这些功能的更多信息，请参阅 `man dispatch_object`。

**派发队列（Dispatch Queues）**  
 GCD 中的一个基本概念是派发队列（dispatch queue）。派发队列是一个接受任务并按其到达顺序执行任务的对象。派发队列可以是并发的或串行的。并发队列会根据系统负载同时执行多个任务，与 NSOperationQueue 非常相似。串行队列一次只执行一个任务。

GCD 中有三种主要类型的队列：

1. **主队列（main queue）：** 类似于主线程（main thread）。实际上，提交到主队列的任务会在进程的主线程上执行。可以通过调用 `dispatch_get_main_queue()` 获取主队列。由于主队列本质上与主线程绑定，因此它是一个串行队列。
2. **全局队列（global queues）：** 全局队列是在整个进程中共享的并发队列。存在三个全局队列：高优先级、默认优先级和低优先级队列。可以通过调用 `dispatch_get_global_queue` 并指定所需的优先级来访问全局队列。
3. **自定义队列（custom queues）：** 自定义队列（GCD 并没有这样称呼它们，也没有给它们一个特定名称，所以我称之为“自定义”队列）是使用 `dispatch_queue_create` 函数创建的队列。这些是串行队列，每次只执行一个任务。因此，它们可以用作同步机制，非常类似于传统多线程程序中的互斥锁。

**创建队列**  
 如果你想使用自定义队列，就必须创建一个。为此，只需调用 `dispatch_queue_create`。第一个参数是一个标签（label），仅用于调试目的。Apple 建议使用反向 DNS 命名来为队列赋予唯一名称，例如 `"com.yourcompany.subsystem.task"`。这些名称会出现在崩溃日志中，并且可以从调试器中查询，在尝试找出问题所在时非常有帮助。第二个参数是一个属性（attribute）参数，目前不支持，因此传递 `NULL`。

**提交任务**  
 向队列提交任务很简单：调用 `dispatch_async` 函数，并传递一个队列和一个 `block`。然后，当轮到该 `block` 执行时，队列将执行它。以下是一个使用全局队列在后台执行长时间运行任务的示例：

```
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        [self goDoSomethingLongAndInvolved];
        NSLog(@"Done doing something long and involved");
    });
```

`dispatch_async` 会立即返回，然后该 `block` 将在后台异步执行。

当然，在工作完成时仅仅执行一个 `NSLog` 并不是很有用。在典型的 Cocoa 应用程序中，你可能希望更新 GUI 的某一部分，而这又意味着需要在主线程上运行代码。你可以通过使用嵌套派发来轻松实现这一点，外层派发执行后台工作，然后在后台 `block` 内部再次派发到主队列，如下所示：

```
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        [self goDoSomethingLongAndInvolved];
        dispatch_async(dispatch_get_main_queue(), ^{
            [textField setStringValue:@"Done doing something long and involved"];
        });
    });
```

还有一个 `dispatch_sync` 函数，它执行相同的操作，但会等待 `block` 完成后再返回。结合 `__block` 类型限定符，这可以用来从正在执行的 `block` 中获取返回值。例如，你可能有一些在后台线程（或者更好的是，非主派发队列）上运行的代码，需要从 GUI 控制（control）中获取值。你可以通过使用 `dispatch_sync` 和 `dispatch_get_main_queue` 轻松做到这一点：

```
    __block NSString *stringValue;
    dispatch_sync(dispatch_get_main_queue(), ^{
        // __block 变量不会自动保留
        // 所以我们最好确保有一个可以保留的引用
        stringValue = [[textField stringValue] copy];
    });
    [stringValue autorelease];
    // 现在在后台使用 stringValue
```

然而，采用更异步的编程风格可能更好。与其阻塞后台处理来获取 GUI 值，你可以使用嵌套的 `block` 来终止后台处理，在主线程上执行你的获取操作，然后将进一步的处理提交回后台。你可以像这样编写代码：

```
    dispatch_queue_t bgQueue = myQueue;
    dispatch_async(dispatch_get_main_queue(), ^{
        NSString *stringValue = [[[textField stringValue] copy] autorelease];
        dispatch_async(bgQueue, ^{
            // 现在在后台使用 stringValue
        });
    });
```

根据你的需要，`myQueue` 可以是一个自定义队列，也可以是全局队列之一。

**替代锁**  
 自定义队列可以用作同步机制来替代锁。在传统的多线程编程中，你可能有一个设计为可以从多个线程使用的对象。为了实现这一点，它使用锁来保护对共享数据的所有访问，你可能会在实例变量中找到这样一个锁：

```
    NSLock *lock;
```

然后，访问看起来像这样：

```
    - (id)something
    {
        id localSomething;
        [lock lock];
        localSomething = [[something retain] autorelease];
        [lock unlock];
        return localSomething;
    }
    
    - (void)setSomething:(id)newSomething
    {
        [lock lock];
        if(newSomething != something)
        {
            [something release];
            something = [newSomething retain];
            [self updateSomethingCaches];
        }
        [lock unlock];
    }
```

使用 GCD，你可以用队列替换实例变量：

```
    dispatch_queue_t queue;
```

为了用作同步机制，队列必须是自定义队列，而不是全局队列，因此你将使用 `dispatch_queue_create` 来初始化它。然后，将所有访问共享数据的代码包装在 `dispatch_async` 或 `dispatch_sync` 中：

```
    - (id)something
    {
        __block id localSomething;
        dispatch_sync(queue, ^{
            localSomething = [something retain];
        });
        return [localSomething autorelease];
    }
    
    - (void)setSomething:(id)newSomething
    {
        dispatch_async(queue, ^{
            if(newSomething != something)
            {
                [something release];
                something = [newSomething retain];
                [self updateSomethingCaches];
            }
        });
    }
```

请注意，派发队列极其轻量，因此完全可以在你使用锁的任何时候使用它们。

此时你可能会问，这听起来不错，但意义何在？我只是将代码从一种机制切换到了另一种看起来差不多的机制。为什么要这样做？

GCD 方法实际上有几个优点：

1. **并行性：** 注意第二个版本的代码中 `-setSomething:` 是如何使用 `dispatch_async` 的。这意味着对 `-setSomething:` 的调用会立即返回，然后大部分工作将在后台执行。如果 `updateSomethingCaches` 是一个代价高昂的操作，并且调用者也正在进行处理器密集型任务，这将是一个显著的收益。
2. **安全性：** 使用 GCD，不可能意外编写出未解锁锁的代码路径。在普通的锁定代码中，无意中在锁中间放置 `return` 语句、使用条件化退出或其他同样不幸的情况并不少见。使用 GCD，队列始终继续运行，你不可避免地会正常地将控制权返回给它。
3. **控制：** 可以随意暂停和恢复派发队列，这对于基于锁的方法来说不容易做到。还可以将自定义队列指向另一个派发队列，使其继承该队列的属性。通过这种方式，可以让队列指向不同的全局队列来调整其优先级，甚至可以让队列在主线程上执行代码（如果出于某种原因需要这样做）。
4. **集成性：** GCD 事件系统与派发队列集成。对象需要使用的任何事件或定时器都可以指向该对象的队列，从而使处理程序自动在该队列上运行，并自动与对象同步。

**结论**  
 现在你已经了解了 Grand Central Dispatch 的基础知识，包括如何创建派发队列、如何向派发队列提交任务，以及如何将队列用作多线程程序中锁的替代品。下周我将向你展示如何使用 GCD 编写执行并行处理的代码，以从多核系统中提取更多性能。在接下来的几周里，我将更深入地讨论 GCD 的更多内容，包括事件系统和队列目标设置。

本周的 Friday Q&A 到此结束。下周再来了解更多 GCD 的精彩内容。虽然我已经为几周的主题做了规划，但这并不意味着我不需要你的建议。恰恰相反：Friday Q&A 是由你的建议驱动的，建议越多，我在这系列结束时就更能写出更好的文章。如果你有想要涵盖的主题建议，请在评论中发布，或者[直接通过电子邮件发送给我](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我正在售卖满满全是这些文章的书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
