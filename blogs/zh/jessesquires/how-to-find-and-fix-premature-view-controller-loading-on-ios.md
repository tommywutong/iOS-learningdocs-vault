---
title: 如何发现并修复 iOS 上视图控制器的过早加载
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/02/20/ios-view-controller-loading/'
original_language: en
published: 2023-02-20
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e00397ae8b86c406'
translated: true
---

> 原文：[How to find and fix premature view controller loading on iOS](https://www.jessesquires.com/blog/2023/02/20/ios-view-controller-loading/)　·　Jesse Squires

在参与一个大型 iOS 客户端项目时，我一直在调查 App 启动时间缓慢的原因。我们有一个猜想：问题**部分**在于加载到内存中的视图控制器（View Controller）太多了，尤其是在 App 启动期间，有些视图控制器甚至根本没有呈现给用户。是什么原因导致视图控制器加载过早？如何发现这种情况？又该如何修复？让我们一探究竟。

### 视图控制器的生命周期

[`UIViewController`](https://developer.apple.com/documentation/uikit/uiviewcontroller) 是 iOS 开发中的一个基础组件（[归档文档](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457-CH2-SW1)）。为了调试我们的问题，需要理解视图控制器的生命周期。如果你无意（或有意）干扰它，就可能会引发意想不到的问题。

（简化后的）事件序列和状态转换如下：

1. `init()` — 初始化视图控制器。
2. 初始化后的视图控制器通过某个呈现方法被呈现，例如 [`present(_:animated:completion:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621380-present)。
3. `loadView()` — 视图被创建并加载到内存中。
4. `viewDidLoad()` — 在视图加载完成后调用。
5. `viewWillAppear(_:)` — 在视图即将出现时调用。
6. `viewDidAppear(_:)` — 在视图呈现完成后调用。
7. `viewWillDisappear(_:)` — 在视图即将消失时调用。
8. `viewDidDisappear(_:)` — 在视图被解除后调用。

如果你开发过 iOS App，你一定实现过这些方法中的大部分。而且你大概很清楚每项方法适合或不适合执行什么类型的任务。

需要强调的是，视图控制器拥有的视图（即 `self.view`）**不会**在呈现（presentation）**开始前**被加载——至少，正确的行为应该是这样。不幸的是，有一个小错误可能会改变上述事件顺序：在 `init()` 方法中访问 `self.view`。这样做会过早地启动视图生命周期事件。`self.view` 的[文档](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621460-view)中写道：

> 如果你在该属性值为 `nil` 时访问它，视图控制器会自动调用 `loadView()` 方法并返回生成的视图。

完成后，`loadView()` 会触发对 `viewDidLoad()` 的调用。请注意，其余的外观方法**也不会**提前调用，它们只会在实际呈现发生时调用。结果就是，在初始化之后，`loadView()` 和 `viewDidLoad()` 会立即被调用——**早于**任何呈现操作的发起。

1. `init()`（错误地访问了 `self.view`）
2. `loadView()`
3. `viewDidLoad()`
4. 稍后时刻，通过 `present(_:animated:completion:)` 等方法进行呈现。
5. `viewWillAppear(_:)`
6. `viewDidAppear(_:)`
7. ……

### 过早加载视图的问题

在视图控制器的 `init()` 方法中访问 `self.view` 是一个错误，因为它会过早地启动视图生命周期，调用 `loadView()` 和 `viewDidLoad()`。这对性能非常不利，因为主线程此时正在为那些甚至不在屏幕上的内容构建整个视图层级结构（view hierarchy）。由于 `viewDidLoad()` 通常是发起各种重要任务（例如订阅通知、发送网络请求或从磁盘加载数据）的地方，性能可能会进一步下降。根据你 `viewDidLoad()` 实现的复杂程度，这种行为可能非常有害。

你可能在想，如果我们马上就要呈现这个视图控制器，那这又有什么关系呢？嗯，情况并非总是如此！有很多场景是你可能初始化了一个视图控制器的集合——但**不会立即呈现**它们。最常见的场景是使用容器视图控制器（Container View Controller），例如 `UITabBarController` 或 `UINavigationController`。以 `UITabBarController` 为例，所有的视图控制器都会被初始化，但只有第一个选中的标签页中的控制器，其视图才会被**呈现**。其余的视图控制器会在用户首次导航到那些标签页时才第一次呈现。在此之前，它们的视图不会被加载。导航叠放（navigation stack）也是如此：你可能会为了深层链接（deep-linking）而配置一个栈的视图控制器。只有最顶部的视图控制器会加载其视图。

如果你在 `UITabBarController` 或 `UINavigationController` 持有的所有视图控制器的 `init()` 中都访问了 `self.view`，那么所有这些视图控制器都会在初始化期间加载它们的视图，触发 `viewDidLoad()`，从而可能触发对通知的响应、发送网络请求、从磁盘加载数据等操作。结果就是，当那些网络请求完成或那些订阅开始触发时，你可能会观察到一些奇怪且出乎意料的行为——因为你在响应这些事件并更新一个甚至不在屏幕上的视图。这会产生不必要的工作，消耗宝贵的资源，并浪费主线程的宝贵时间。

在庞大、复杂的代码库中，像这样的小问题会随着时间推移而增长和倍增。意外加载单个视图控制器的行为可能不会被注意到。但如果你有十几个或更多呢？

### 发现并修复这个 Bug

手动检查代码库中的每一个视图控制器是不可行的。根据你 App 的规模，很可能有成百上千个。符号断点（Symbolic Breakpoint）是解决这个问题的完美工具。我们可以为 `-[UIViewController viewDidLoad]` 创建一个符号断点。然后，我们需要添加几个操作（Actions），以便能够看到发生了什么——一个“记录消息”（Log Message）操作，使用 `%B` 来打印断点名称；以及一个“调试器命令”（Debugger Command）操作，使用 `po $arg1` 来打印视图控制器的实例（instance）。最后，我们需要告诉调试器在执行这些操作后继续执行。

![在 viewDidLoad() 上设置符号断点](https://www.jessesquires.com/img/blog/viewdidload-breakpoint.jpg)

<sub>在 viewDidLoad() 上设置符号断点</sub>

现在，我们可以构建并运行 App。完全不要与 App 交互，只需让它完全启动。控制台日志将会像这样：

```
-[UIViewController viewDidLoad]
<MyFirstViewController: 0x7f9d52886c00>

-[UIViewController viewDidLoad]
<MySecondViewController: 0x7f9d42858800>

-[UIViewController viewDidLoad]
<MyThirdViewController: 0x7f9d43095740>

-[UIViewController viewDidLoad]
<MyFourthViewController: 0x7f9d431de9d0>
```

这显示的是在 App 启动期间加载的每一个视图控制器——多么方便！我们获得了在 App 启动期间 `viewDidLoad()` 被调用的所有视图控制器的列表。剩下要做的就是检查这些视图控制器中的每一个，并验证它们是否应该被加载。它们是否被呈现且对用户可见？还是它们过早地访问了 `self.view`？

我在此项目中发现，许多情况下是在 `init()` 方法中执行了 `self.view.backgroundColor = UIColor.customColor`。将这一行移动到 `viewDidLoad()` 中就解决了问题。不幸的是，还有一些更复杂的情况也触发了过早的 `viewDidLoad()`。在某些情况下，是另一个组件访问了视图控制器的 `view` 属性（property）。在另一些情况下，`self.view` 是通过从 `init()` 开始的一系列函数调用链被访问的。因此，请注意，解决这些 Bug 可能并不总是那么显而易见。
