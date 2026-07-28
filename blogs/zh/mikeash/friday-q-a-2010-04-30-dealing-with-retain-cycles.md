---
title: 'Friday Q&A 2010-04-30：处理循环引用'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5ea1bef61a70053'
translated: true
---

> 原文：[Friday Q&A 2010-04-30: Dealing with Retain Cycles](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)　·　mikeash.com Friday Q&A

发布于 2010-04-30 15:29 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[又一个没有 Friday Q&A 的星期](https://www.mikeash.com/pyblog/another-week-without-friday-qa.html)
上一篇文章：[Friday Q&A 2010-04-23：实现自定义滑块](https://www.mikeash.com/pyblog/friday-qa-2010-04-23-implementing-a-custom-slider.html)
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [release](https://www.mikeash.com/pyblog/?tag=release) [retain](https://www.mikeash.com/pyblog/?tag=retain)

Friday Q&A 2010-04-30：处理循环引用

作者：[Mike Ash](https://www.mikeash.com/)

**循环引用（Retain Cycles）**
首先我们需要讨论循环引用到底是什么。假设你已经熟悉了标准的 Cocoa 内存管理。最简单的循环引用就是两个对象互相 retain（保留）对方：

```
    Object A
     |    ^
     |    |
     v    |
    Object B
```

在一般情况下，它可以是任何一组对象，形成像这样的循环链接链。虽然不常见，但有可能出现三个、四个、五个甚至更多对象相互指向形成一个环。

循环引用之所以是个问题，是因为 Cocoa 内存管理的标准做法是在对象的 `dealloc` 方法中释放这些 retained（已保留）引用。然而，如果一个对象正在被 retain，它就**不会**执行 `dealloc`。属于循环引用一部分的对象将永远不会被释放，如果与 App 的其余部分分离，就会泄漏。

请注意，循环引用可能涉及你自己的类，但也可能涉及 Cocoa 类。Cocoa 类中循环引用最常见的两个罪魁祸首是 `NSTimer` 和 `NSThread`。

还要注意，循环引用只影响使用手动内存管理的代码。Cocoa 的垃圾回收器能够检测并销毁那些彼此有强引用（strong reference）但外部没有引用的对象。然而，如果你使用的是 retain/release 内存管理（例如在 iPhone 上），循环引用是一个巨大的威胁，甚至在使用垃圾回收的 App 中，如果你用 `CFRetain` 和 `CFRelease` 绕过回收器，循环引用也可能出现。

**避免循环引用**
Apple 的内存管理指南指出，当两个对象具有父子关系时，父对象应 retain 子对象。如果子对象需要回指父对象的引用，该引用应该是未 retain 的弱引用（weak reference）。这样父对象可以被释放，然后它就能释放对子对象的引用，从而避免循环。

然而，有时你有两个对象是平级的。两者都不是对方的父对象，但它们需要相互引用。如果这些引用是 retained 的，那么你就有了一个循环。

处理这个问题的一种方法是将关系重新定义为父子关系。你可以任意选择一个作为父对象，它持有一个对另一个的 retained 引用。另一个则可以持有一个对第一个的弱引用。循环图看起来像这样：

```
    Object A
     |    ^
     |    :
     v    :
    Object B
```

为了安全起见，Object A 在销毁时应该始终将 B 的弱引用置为 nil，以确保 B 之后不会尝试向它发送消息：

```
    - (void)dealloc
    {
        [_b setAReference: nil];
        [_b release];
        [super dealloc];
    }
```

（这也是任何弱引用的好做法，包括像 `NSTableView` 数据源之类的东西。）

另一种方法是让另一个对象充当两个子对象的共同父对象。这种方式在子对象之间使用 retained 或弱引用都可以。使用 retained 引用：

```
           Object C
           |      |
           |      |
           v      v
    Object A<====>Object B
```

在这个场景中，你仍然有一个循环引用，但是 C 可以在释放其引用时打破这个循环：

```
    - (void)dealloc
    {
        // 通过置零引用来打破循环
        [_a setBReference: nil];

        // 这打破了两个方向的循环；这是可选的
        [_b setAReference: nil];

        [_a release];
        [_b release];

        [super dealloc];
    }
```

你也可以在子对象之间使用弱引用：

```
           Object C
           |      |
           |      |
           v      v
    Object A<::::>Object B
```

在这种情况下，C 为了安全也应该清除弱引用，但不这样做也能解决问题。

哪种方式更好？它们基本等价。我认为使用 retained 引用稍微安全一些，无论是从以后改变对象图时仍然能正常工作，还是从更能抵抗代码错误的角度来看。

**`NSThread` 和 `NSTimer`**
`NSThread` 和 `NSTimer` 是循环引用的常见原因。写出像下面这样的代码并不罕见：

```
    - (id)init
    {
        ...
        _timer = [[NSTimer scheduledTimerWithTimeInterval: 0.1 target: self selector: @selector(whatever) userInfo: nil repeats: YES] retain];
        ...
    }

    - (void)dealloc
    {
        [_timer invalidate];
        [_timer release];
        [super dealloc];
    }
```

这里有一个循环引用！这个对象 retain 了定时器，而定时器 retain 了它的目标。注意，你不能通过不 retain `_timer` 来解决这个问题。运行循环（run loop）也会 retain 定时器，并且在调用 `invalidate` 之前不会释放它。这相当于对定时器的第二个 retained 引用，即使没有显式的 retained 引用，也会导致本质上是一个环。

同样的问题也发生在 `NSThread` 上，当你指定 `self` 作为目标，然后在 `dealloc` 中关闭线程时。`dealloc` 方法永远不会运行，所以线程永远不会被关闭。

有两种方法可以处理这个问题。一种是强制显式失效，另一种是将你的代码拆分成两个类。

当你释放对 `NSTimer` 的最后引用时，定时器不一定被销毁。只要定时器处于激活状态，运行循环就保持对它的引用。要销毁一个重复定时器，你不能仅仅释放所有对它的引用，你必须显式地使其失效。

你可以将这个概念借用到你自己的类中。只需公开你自己的 `invalidate` 方法，并用它来销毁定时器：

```
    - (void)invalidate
    {
        [_timer invalidate];
        [_timer release];
        _timer = nil;
    }
```

当然，这会将实现细节泄漏到你的接口中，但强制调用者显式声明他们何时完成对你的对象的使用，并不总是坏事。

另一种方法是将你的代码拆分成两个类。你有一个暴露给外部世界的外壳类，它管理线程或定时器。然后你有一个实现类，它是线程或定时器的目标，并完成大部分实际工作：

```
    @implementation MyClassImpl

    - (id)init
    {
        ...
        _timer = [[NSTimer scheduledTimerWithTimeInterval: 0.1 target: self selector: @selector(_timerAction) userInfo: nil repeats: YES] retain];
        ...
    }

    - (void)invalidate
    {
        [_timer invalidate];
        [_timer release];
        _timer = nil;
    }

    - (void)doThingy
    {
        // do stuff here
    }

    - (void)_timerAction
    {
        // periodic code here
    }

    @end
```

```
    @implementation MyClass

    - (id)init
    {
        ...
        _impl = [[MyClassImpl alloc] init];
        ...
    }

    - (void)dealloc
    {
        [_impl invalidate];
        [_impl release];

        [super dealloc];
    }

    - (void)doThingy
    {
        // just pass it on to the "real" code
        [_impl doThingy];
    }

    @end
```

通过将实现与接口分离，你避免了循环引用。实际上，`MyClass` 成了共同的父对象，而 `MyClassImpl` 和 `NSTimer` 是子对象。父对象在销毁时手动打破子对象之间的循环引用。在外部，父对象保留了正常的 retain/release 语义，无需显式失效。

**Block**
因为 `block`会 retain 它们引用的对象，所以它们也是循环引用的另一个绝佳候选。考虑以下代码：

```
    - (id)init
    {
        ...
        _observerObj = [[NSNotificationCenter defaultCenter] addObserverForName: ... queue: [NSOperationQueue mainQueue] usingBlock: ^(NSNotification *note) {
            [self doSomethingWith: note];
        }];
        [_observerObj retain];
        ...
    }

    - (void)dealloc
    {
        [[NSNotificationCenter defaultCenter] removeObserver: _observerObj];
        [_observerObj release];
        [super dealloc];
    }
```

因为通知 block引用了 `self`，所以 `block` 会 retain `self`。结果是一个微妙的循环引用。即使你不直接引用 `self`，也可能发生这种情况；简单地引用一个实例变量（instance variable）就会间接引用 `self`，这会导致 `block`  retain 它。

用于 `NSTimer` 和 `NSThread` 的解决方案在这里同样适用：要么在类的 API 中添加显式失效，要么将类拆分为两部分。

还有一个 `block` 特有的解决方案你可以使用，即通过一个声明为 `__block` 的变量来引用 `self`，这样 `self` 就不会被 retain：

```
        __block MyClass *blockSelf = self;
        _observerObj = [[NSNotificationCenter defaultCenter] addObserverForName: ... queue: [NSOperationQueue mainQueue] usingBlock: ^(NSNotification *note) {
            [blockSelf doSomethingWith: note];
        }];
```

这避免了循环，因为 `blockSelf` 没有被 retain。如果你这样做，要小心避免直接引用实例变量，因为它们仍然会引用原始的 `self`。如果你需要访问一个实例变量，通过执行 `blockSelf->_someIvar` 显式地经由 `blockSelf` 来间接访问。

**查找循环**
在很大程度上，标准的泄漏查找技术在查找导致泄漏的循环引用时会很有效。Instruments 是找到它们的好方法，无论是 ObjectAlloc 工具还是 Leaks 工具。如果你有一个难以弄清楚的循环，它跟踪每个对象的 `retain` 和 `release` 调用的能力可以帮上大忙。

如果你更喜欢命令行，或者只是需要更容易搜索的文本，`leaks` 命令行工具也很方便。

在寻找循环时，请注意，如果有一个外部引用进入循环，泄漏工具并不总能找到循环。例如，考虑一个涉及 `NSTimer` 的循环。运行循环有一个对定时器的引用，定时器也有一个对你的对象的引用，所以它们都是可达的。Leaks 工具和 `leaks` 工具都不会认为这是泄漏。然而，如果它们什么都不做且无休止地累积，那么它仍然是一个泄漏，即使它们在技术上是可达的。ObjectAlloc 工具会显示这种累积，即使其他工具不会识别出泄漏。

**结论**
循环引用是 Cocoa 内存管理系统上一个不幸的瑕疵。然而，只要稍加注意，通过对对象层次结构进行微小的改动，它们就可以以最小的痛苦避免或修复。要特别注意 `NSTimer` 和 `NSThread`（但不要忽略其他代码！），然后要么消除循环，要么添加显式打破它的代码。

这就是本周的全部内容。七天后回来参加下一次 Friday Q&A。一如既往，Friday Q&A 由读者提交驱动。如果你有一个希望在这里讨论的主题想法，请[发送过来](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我正在销售包含它们的整本书！第二卷和第三卷现已出版！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被无通知删除。违规者可能会由我酌情公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
