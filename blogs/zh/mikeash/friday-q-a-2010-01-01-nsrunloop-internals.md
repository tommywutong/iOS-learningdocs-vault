---
title: 'Friday Q&A 2010-01-01：NSRunLoop 内部原理'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d2940c3a0a7f6b16'
translated: true
---

> 原文：[Friday Q&A 2010-01-01: NSRunLoop Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html)　·　mikeash.com Friday Q&A

发布于 2010-01-01 10:43 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2010-01-08: NSNotificationQueue](https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)
上一篇文章：[Friday Q&A 2009-12-18: Highlights From a Year of Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2009-12-18-highlights-from-a-year-of-friday-qa.html)
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [runloop](https://www.mikeash.com/pyblog/?tag=runloop)

Friday Q&A 2010-01-01：NSRunLoop 内部原理

作者：[Mike Ash](https://www.mikeash.com/)

如果你想尽可能彻底地理解某个东西，最好的办法是自己动手实现一个。这对一篇博客文章来说有点过分了，所以我不打算完整实现 `NSRunLoop`，而是走第二条最佳路线：用伪代码来规划其内部的关键特性。

**CoreFoundation**
在 Mac 上，`NSRunLoop` 构建在其 CoreFoundation 等价物 `CFRunLoop` 之上。大部分智能逻辑都在那里，Cocoa 这一侧基本上只是一个封装。在本次讨论中，我将忽略这个分层，把 `NSRunLoop` 视为一个独立的实体来考察。从这个角度看，`CFRunLoop` 可以看作是一个实现细节。

**自动释放池（Autorelease Pool）**
`NSRunLoop` 的基本工作之一是管理自动释放池，既为自己也为它所调用的代码管理。由于自动释放池与其它部分相比相当直接，而且只会让事情变得杂乱，我将忽略 `NSRunLoop` 的这一方面功能。

**基础（Fundamentals）**
`NSRunLoop` 的大部分神秘之处在于它的各种 `run` 方法。里面到底发生了什么？它是如何工作的？

`-run` 方法非常简单，因为文档是用 `-runMode:beforeDate:` 来描述它的：

如果没有输入源（input source）或定时器（timer）附加到运行循环（run loop），此方法会立即退出；否则，它会在 NSDefaultRunLoopMode 下通过反复调用 runMode:beforeDate: 来运行接收器。

因此它的实现看起来大概是这样：

```
    - (void)run
    {
        while([self hasSourcesOrTimers])
            [self runMode: NSDefaultRunLoopMode beforeDate: [NSDate distantFuture]];
    }
```

`-runUntilDate:` 方法类似：

如果没有输入源或定时器附加到运行循环，此方法会立即退出；否则，它会在 NSDefaultRunLoopMode 下通过反复调用 runMode:beforeDate: 来运行接收器，直到指定的到期日期。

它的实现应该是这样：

```
    - (void)runUntilDate: (NSDate *)limitDate
    {
        while([self hasSourcesOrTimers])
        {
            [self runMode: NSDefaultRunLoopMode beforeDate: limitDate];

            // 在循环末尾检查 limitDate，以确保
            // 运行循环始终至少运行一次
            if([limitDate timeIntervalSinceNow] < 0)
                break;
        }
    }
```

这很容易。那么 `-runMode:beforeDate:` 呢？嗯，所有复杂之处都在那里。

**输入源（Input Source）**
如 [Apple 的运行循环编程指南](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html) 所述，运行循环包含两种类型的源：输入源和定时器。输入源基本上是来自运行循环外部的一些外部信号。

在 Mac OS X 中，输入源是 Mach 端口（mach port）。虽然像 NSFileHandle 和 CFFileDescriptor 这样的东西看起来像是把非 Mach 端口的东西连接到了运行循环中，但这实际上是伪造的！它们在一个专用线程上监控其文件描述符源，然后通过一个 Mach 端口向运行循环发回信号。

（这在 10.6 中可能已经改变，现在有能够同时监控 Mach 端口和文件描述符的 API。然而，基本事实仍然是 Mach 端口是 OS X 上使用的主要输入源。）

大多数人一听到 Mach 端口就会走神。它们既不广为人知，也没有很好的文档记录。而且就我个人而言，我自己也不太了解它们。因此，我将探索一个替代的 `NSRunLoop`，它改用文件描述符作为其输入源。基本原理是一样的，而且文件描述符对大多数人来说更容易理解。

快速复习：什么是文件描述符（file descriptor，简称 FD）？一个 FD 是一个对象（不是 Objective-C 意义上的对象，而是概念上的），你可以从中读取、写入，或者同时读写。一个 FD 可能有数据可供读取、有空间可供写入，或者两者都没有。FD 的这种特定状态可以随时间变化。例如，想象一个代表与另一个应用程序通信的套接字的 FD。当那个其他应用程序写入套接字时，你应用程序中的 FD 将会有数据可供读取。如果该 FD 是运行循环的输入源，该运行循环将被唤醒并处理该源。同样，如果其他应用程序从套接字读取，你应用程序中的 FD 将会有空间可供写入，这也会唤醒运行循环并处理该源。这是运行循环的基本任务之一。

一个运行循环需要同时监控多个输入源。OS X 上有几个 API 可以做到这一点，但我在这里将使用的是 `select(2)`。

我不会详细说明如何使用 `select`（还记得吧，伪代码！），但基本要点相当简单：你给它三组 FD，分别用于监控读取、写入和错误。当有活动时它会返回，并且这三组 FD 会包含那些发生过相应活动的 FD。

因此，我们可以看出 `-runMode:beforeDate:` 的第一个版本是如何工作的。我将进一步简化，忽略 `select` 接受三组不同的 FD 这一事实，只使用一组。关键是我们对这些输入源上的活动感兴趣。

请记住，我在写伪代码，所以不要期望它看起来 100% 像真实的 Objective-C。

首先要检查是否有任何源。根据文档，如果没有，此方法立即返回 `NO`：

```
    - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimers])
            return NO;
```

接下来，创建一个空的 FD 集合：

```
        fd_set fdset;
        FD_ZERO(&fdset);
```

然后，在集合中设置每个输入源的 FD。我假设输入源类有一个 `-fileDescriptor` 方法，返回它想要监控的 FD：

```
        for(inputSource in [self inputSources])
            FD_SET([inputSource fileDescriptor], &fdset);
```

现在调用 `select`。记住，为了简化，我假装它只接受一个文件描述符集合而不是三个。我也忽略了所有错误检查：

```
        select(fdset, NULL);
```

一旦它返回，检查每个输入源以确定它是否已准备好进行处理。我遍历输入源的一个副本，因为输入源执行的代码可能会修改输入源集合：

```
        for(inputSource in [[[self inputSources] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];
```

文档说明此方法在运行循环以任何方式运行时返回 `YES`，所以这是最后要做的事情：

```
        return YES;
    }
```

**模式（Mode）**
到目前为止还不错，但还有一段路要走。这个方法完全忽略了它的参数！首先，我们来看看 `mode` 参数。

那么，`mode` 参数到底是什么？模式本质上是输入源和定时器源的一个分组。不同的源在不同的模式下处于活动状态。`NSRunLoop` 有 `NSDefaultRunLoopMode`，顾名思义，大多数源都被添加到这里。在 Cocoa 中，还有一些次要模式，比如 `NSEventTrackingRunLoopMode`，它用于在控制（control）上按住鼠标时。通过切换到这种模式，那些只被添加到默认模式下的源将不会触发，这防止了在用户正在做出菜单选择或移动滑块时运行不需要的代码。需要在事件跟踪期间触发的源可以被添加到该模式。需要在两种情况下都触发的源可以同时添加到两者。

你可以想象 `NSRunLoop` 包含一个像这样的输入源实例变量：

```
    NSMutableDictionary *_inputSources; // 将模式映射到 NSMutableSets
```

`NSRunLoop` 添加输入源的方法叫做 `-addPort:forMode:`，它的实现看起来像这样：

```
    - (void)addPort: (NSPort *)aPort forMode: (NSString *)mode
    {
        NSMutableSet *sourcesSet = [_inputSources objectForKey: mode];
        if(!sourcesSet)
        {
            // 这是第一次有任何东西使用这个模式
            // 所以为它创建一个新集合
            sourcesSet = [NSMutableSet set];
            [_inputSources setObject: sourcesSet forKey: mode];
        }
        [sourcesSet addObject: aPort];
    }
```

类似的移除方法：

```
    - (void)removePort: (NSPort *)aPort forMode: (NSString *)mode
    {
        NSMutableSet *sourcesSet = [_inputSources objectForKey: mode];
        [sourcesSet removeObject: aPort];

        // 这不是严格必需的，但如果调用者使用了大量一次性
        // 的"用完即弃"模式（它可能永远不会这么做），
        // 这可以防止我们泄漏集合
        if(![sourcesSet count])
            [_inputSources removeObjectForKey: mode];
    }
```

然后运行方法需要修改以匹配：

```
    - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;

        fd_set fdset;
        FD_ZERO(&fdset);

        for(inputSource in [_inputSources objectForKey: mode])
            FD_SET([inputSource fileDescriptor], &fdset);

        select(fdset, NULL);

        for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];

        return YES;
    }
```

**超时（Timeout）**
这段代码仍然忽略了一个参数，`limitDate`。这个参数的目的是即使没有输入源准备好也强制方法返回。它起到了超时的作用。为了实现这一点，代码简单地计算超时并将其作为最后一个参数传递给 `select`（实际上需要一个更复杂的超时结构，而不仅仅是一个 `NSTimeInterval`，但记住，伪代码！）：

```
     - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;

        fd_set fdset;
        FD_ZERO(&fdset);

        for(inputSource in [_inputSources objectForKey: mode])
            FD_SET([inputSource fileDescriptor], &fdset);

        NSTimeInterval timeout = [limitDate timeIntervalSinceNow];
        select(fdset, timeout);

        // 如果命中了超时，可能没有
        // 任何活跃的输入源，但如果确实如此，
        // 这个循环将什么都不做
        for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];

        return YES;
    }
```

**定时器源（Timer Source）**
这个实现已经足够好地处理了输入源和超时参数，但完全忽略了定时器。

与输入源一样，我假设有一个持有定时器的实例变量。并且像输入源一样，定时器被分组到模式中：

```
    NSMutableDictionary *_timerSources; // 将模式映射到 NSMutableSets
```

我将跳过 `-addTimer:forMode:` 的实现，因为它应该很明显，并且基本上与 `-addPort:forMode:` 相同。

将定时器支持添加到上面的代码中相对简单。可以查阅定时器列表以找到最早触发的那个。如果那个时间早于 `limitDate`，那么它将成为超时而不是 `limitDate`。在 `select` 运行之后，检查定时器列表以查看是否有任何定时器准备好触发，并触发那些准备好的。

有一个小问题，即定时器触发并**不会**使 `-runMode:beforeDate:` 返回。如果一个定时器触发了，它应该被处理，然后控制权应该返回到 `select`。这将继续直到一个输入源触发。如果一个输入源确实触发了，该方法仍然需要检查定时器列表并触发任何准备好的定时器，因为否则一个繁忙的输入源可能会阻止定时器运行。

考虑到所有这些，这里是添加了定时器支持后的代码样子：

```
     - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;

        // 有了定时器支持，这段代码必须循环，
        // 直到一个输入源触发
        BOOL didFireInputSource = NO;
        while(!didFireInputSource)
        {
            fd_set fdset;
            FD_ZERO(&fdset);

            for(inputSource in [_inputSources objectForKey: mode])
                FD_SET([inputSource fileDescriptor], &fdset);

            // 需要根据 limitDate
            // 和定时器列表设置超时
            // 先从 limitDate 开始
            NSTimeInterval timeout = [limitDate timeIntervalSinceNow];

            // 现在遍历定时器列表，
            // 将超时设置为定时器和
            // limitDate 中找到的最小值
            for(timer in [_timerSources objectForKey: mode])
                timeout = MIN(timeout, [[timer fireDate] timeIntervalSinceNow]);

            // 现在运行 select
            select(fdset, timeout);

            // 首先处理输入源（这个选择是任意的）
            for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
                if(FD_ISSET([inputSource fileDescrptor], &fdset))
                {
                    didFireInputSource = YES;
                    [inputSource fileDescriptorIsReady];
                }

            // 现在处理定时器
            // 为重复定时器更新 fireDate
            // 以及为非重复定时器从运行循环中移除定时器的责任
            // 在定时器类中，而不是在运行循环中
            for(timer in [[[_timerSources objectForKey: mode] copy] autorelease])
                if([[timer fireDate] timeIntervalSinceNow] <= 0)
                    [timer fire];

            // 检查我们是否超时，如果是，则中止！
            // 这在末尾检查，以确保定时器和输入在返回之前
            // 至少被处理一次
            if([limitDate timeIntervalSinceNow] < 0)
                break;
        }
        return YES;
    }
```

这就涵盖了所有必要的功能。最终的代码相当直接且易于理解。

**结论（Conclusion）**
这个练习告诉我们什么？我们必须小心，不要从这个伪代码中**过于**远离，因为不能保证它匹配 Apple 的实现。事实上，我知道一个最近让我吃过亏的例子就不匹配：Apple 的实现对于每次通过运行循环只会触发**一个**待处理的定时器，即使有多个定时器准备好触发，而这段代码会在返回前触发所有待处理的定时器一次。当然，还有一个主要区别是 Apple 的代码使用 Mach 端口而不是文件描述符，尽管它们的语义相似。

尽管有这个问题，从这类练习中可以学到很多东西。例如，运行循环模式是 Cocoa 程序员中常见的困惑点，而写出所有这些内容有助于弄清楚模式到底是什么以及它是如何工作的。

它还可以为推测 Cocoa 其他部分的实现提供信息。例如，我们可以推断出 `-performSelector:withObject:afterDelay:` 方法在内部是如何工作的。由于运行循环只处理源和定时器，它必须使用这两者之一。由于它是在延迟之后激活的，它必须使用定时器。在调试器中观察它的行为将确认这一点是正确的。再举一个例子，我们可以得出结论，`-performSelectorOnMainThread:withObject:waitUntilDone:` 必须使用一个 Mach 端口，因为它不能从辅助线程操控主线程上的定时器。（`NSRunLoop` 不是线程安全的。）

总而言之，这种技术总体上非常有用。我通常不会像这样写出详细的伪代码，但思考**如何**实现某些 Apple 代码确实有助于加深理解它是如何工作的以及文档说了什么，以及它所暗示但没有直接说出来的东西。你必须小心，确保你的结论最终基于文档和现实世界的约束，而不是基于你对它可能如何工作的特定想法的特殊性，但这只需要一点点细心。

仅仅是为了揭开一个类的神秘面纱也是有帮助的。很容易陷入魔法思维，认为一个类是难以理解的，高高在上于凡尘之上。事实是，虽然某些类的特定实现可能非常复杂（`CFRunLoop` 的源代码会让你头昏眼花），但它们所做的事情以及如何做的基本原理通常非常直接。对于 Cocoa 中 99.9% 的 API，它们之所以存在，不是因为它们在做一些你永远无法实现的惊人事情，而仅仅是为了节省你不得不自己编写所有这些代码的时间和麻烦。

这就是本周的全部内容。七天后回来，迎接另一个激动人心的版本。在那之前，[请继续给我发送你的主题想法](mailto:mike@mikeash.com)。Friday Q&A 是由读者驱动的，我得到的主题想法越多，这个系列就会变得越好。

你喜欢这篇文章吗？我正在销售包含这些文章的完整书籍！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上。 [点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-01-nsrunloop-internals.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
