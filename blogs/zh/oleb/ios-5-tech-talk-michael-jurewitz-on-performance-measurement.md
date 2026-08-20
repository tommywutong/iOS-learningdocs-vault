---
title: 'iOS 5 Tech Talk：Michael Jurewitz 谈性能测量'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/ios5-tech-talk-michael-jurewitz-on-performance-measurement/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8291a2f246826d75'
translated: true
---

> 原文：[iOS 5 Tech Talk: Michael Jurewitz on Performance Measurement](https://oleb.net/blog/2011/11/ios5-tech-talk-michael-jurewitz-on-performance-measurement/)　·　Ole Begemann

# iOS 5 Tech Talk：Michael Jurewitz 谈性能测量

**2012 年 1 月 27 日更新：** Apple 最近在其开发者网站上发布了一些新视频。其中一则名为《使用 Instruments 优化 App 性能》的视频由 Michael 主讲，内容与他的 Tech Talk 演讲基本一致。值得观看，尤其是他做的一系列 Instruments 演示。关于如何找到这些视频，请参阅[我关于新视频的博客文章](https://oleb.net/blog/2012/01/new-videos-at-developer-apple-com/)。

我要在这里总结的最后一个 Tech Talk 场次是 [Michael Jurewitz](https://twitter.com/Jury) 的演讲，题为 **Your iOS App Performance Hitlist**：

> 最优秀的 iOS App 不仅外观精美、设计出色，它们还启动迅速、具备高度响应的界面，并且高效利用内存。掌握诊断和修复常见性能问题的技巧，让你的客户看到问题之前就解决它们。学习每款 App 在发布前都应做一遍的“性能检查清单”。

在这个演讲中，Michael 基于三种常见问题领域，手把手教我们如何使用 Instruments 识别性能问题。总的来说，我最喜欢这场演讲。我以前看过关于 Instruments 的讲座，但有时候你需要看两三次演示才能学进去。我确实觉得自己在这里学到了一些新技巧。

# 通用建议

> **测量性能的第一要义就是去实际测量。不要猜测！**

猜测几乎从来不是性能优化的正确方法。没有经过测量就去优化问题是很难的，所以测量必须是你的首要任务。Apple 提供了 Instruments 来量化你 App 的各个方面。

另一个重要因素是在**真实条件下**测试你的 App。如果你只用一个几乎不含测试数据的新鲜开发版本进行测试，很可能无法发现许多日后会困扰用户的严重性能和内存问题。你应该**始终确保测试使用实际规模的数据集**，并且也要**测试最恶劣情况**。毕竟，那些用你的 App 管理大量数据的用户通常是你最好的客户，你不想得罪他们。

在演讲的剩余部分，Michael 专注于以下三种性能特征：

1. 快速启动/避免阻塞操作
2. 最小化内存使用
3. 高效绘制

用他的话来说，如果你优化了这些，你的 App 在性能表现上很可能已经完成了一半以上的路程。

# 1. 快速启动

> **问问自己，这个操作对于加载最基本的 main UI 来说是否必不可少？如果不是，就推迟它。**

许多 iOS App 每次只使用几秒钟，并且（即使在多任务时代）也会被频繁重新启动。对于用户来说，每次启动 App 都要等待好几秒才能开始与之交互，几乎没有比这更令人沮丧的事了。

你的目标应该是让你的 App**尽可能快地准备好接受用户输入**。如果这意味着某些 UI 组件（例如图片或网页内容）还没有完全加载，那也没关系。比起强迫用户等待所有东西 100% 完成，先显示一个没有内容的 UI 要好得多。

为了最小化启动时间，尝试找出你的 App 在其 UI 准备就绪之前，所有可能被调用的方法中必须完成的最少量工作：

- `application:didFinishLaunchingWithOptions:`
- `applicationWillEnterForeground:`
- `applicationDidBecomeActive:`
- `application:openURL:sourceApplication:annotation:`
- `application:didReceiveRemoteNotification:`
- `application:didReceiveLocalNotification:`
- 你的根视图控制器（view controller）的 `init` 和 `awakeFromNib` 方法
- `viewDidLoad` 以及
- `viewWill/DidAppear:`，同样在你的根视图控制器中

你的主要关注点可能应该放在 `application:didFinishLaunchingWithOptions:` 和 `viewDidLoad` 上。

你应该留意的常见问题是**同步网络调用**和**大型数据集的同步加载或解析**，例如巨大的数据文件或图片。`dispatch_async()` 应该成为你最好的朋友。**你不应该在主线程上用同步操作阻塞它**，这些操作可能需要很长时间（超过零点几秒）才能完成，尤其是在 App 的启动阶段。尝试将这些操作推到后台队列，一旦操作完成，再从那里通知主队列。在此之前，在你的 UI 中显示一个进度指示符。

## Instruments：Time Profiler

[![Instruments 中的 Time Profiler 工具](https://oleb.net/media/instruments-time-profiler.png)](https://oleb.net/media/instruments-time-profiler.png)

<sub>Instruments 中的 Time Profiler 工具。</sub>

要使用 Instruments 识别这类问题，请使用 **Time Profiler** 工具。当你的 App 运行时，Instruments 会持续对进程进行采样，并记录代码在调用栈中的当前位置，从而找出你的 App 花费时间最多的方法。

当你收集到足够的数据后，停止录制。你的目标现在是在**调用树（Call Tree）**中找到最耗时的**方法**，并逐个尝试优化它们。以下是 Michael 的一些建议：

- 录制期间，在时间线上放置标记以标识诸如启动过程结束等事件。
- 在查看调用树之前，**始终定义一个检查范围（Inspection Range）**，使用工具栏中的按钮。使用录制期间放置的标记来标识你想要分析的代码段。
- **取消勾选“反转调用树（Invert Call Tree）”和“隐藏系统库（Hide System Libraries）”**选项。前者让你更容易理解调用树（尽管你可能需要多花一点时间点击到有问题的那个方法），而后者则会显示在系统框架中的耗时方法调用。如果你决定隐藏它们，可能会忽略一个位置不当的同步网络调用，这个调用可能会让你的启动时间增加好几秒。

  [![Time Profiler 选项](https://oleb.net/media/instruments-time-profiler-options.png)](https://oleb.net/media/instruments-time-profiler-options.png)

  <sub>Time Profiler 选项。</sub>
- 现在是时候**探索调用树**了。从 `main()` 开始，在树中逐层点击，直到到达你自己的代码（通常在树中超过十几层深），并尝试找出那些占总时间**百分比很大**的方法。打开**扩展详情视图（Extended Detail View）**以查看关于所选行的更多信息，或者双击你代码中的某个方法，直接从 Instruments 跳转到代码中。

  [![Time Profiler 调用树](https://oleb.net/media/instruments-timeprofiler-call-tree.png)](https://oleb.net/media/instruments-timeprofiler-call-tree.png)

  <sub>Time Profiler 调用树。</sub>
- **特别关注“自身（Self）”列**。它告诉你实际花费在该方法内部的时间，而不是它在堆栈深处调用的其他方法。**自身列的高百分比通常表明你的代码中存在问题**，例如长时间运行的循环。
- **经验法则：** 最好是，启动你的 App 不应超过 2-3 秒。如果你的代码占总启动时间的百分比超过 20-30%，这可能表明存在问题。

# 2. 最小化内存使用

优化内存使用从一开始就是 iOS 开发者面临的问题。由于 iOS 设备没有交换文件，系统可使用的内存有**硬性限制**。如果 App 需要的内存超过了可用量，操作系统别无选择，只能杀死一个或多个 App，从（但不限于）当前在后台的 App 开始。还有另一个激励我们尽可能少用内存的原因：你的 App 使用的内存越少，操作系统在后台保持其存活的时间就越长，这对你的用户来说意味着更好的体验。

> **在 iOS 5 中，如果你的 App 是前台 App，而我们向你发送了内存警告，这意味着你的脑袋已经搁在砧板上了。**

为了通知内存压力，操作系统可以向活动 App 发送内存警告。Michael 提到，他感觉自从 iOS 4 引入多任务以来，许多 App 在处理内存警告时变得有点懒散。毕竟，如果前台 App 没有释放任何内存来响应内存警告，操作系统仍然不会杀死它，因为通常有几个已冻结的后台 App 可以优先被杀死。而这确实是 iOS 4 中的行为。由于这些非预期的后果，Michael 强调 Apple 在 iOS 5 中做出了改变：在 iOS 5 中，如果你的 App 是前台 App，而我们向你发送了内存警告，这意味着你的脑袋已经搁在砧板上了。所以**你最好采取行动，响应这些内存警告！**

## Instruments：Allocations + Leaks + VM Tracker + Activity Monitor

Michael 构建了他自己的一套 Instruments 组合来测量 App 的内存使用情况，通过结合 **Allocations、Leaks、VM Tracker 和 Activity Monitor** 这四个工具。你可以自己轻松做到：创建一个空白工具，然后从库（Library）检查器面板中将这四个工具拖入主窗口。然后你可以将此工具保存为模板以便重复使用。

[![Michael Jurewitz 用于内存使用测量的内存工具集](https://oleb.net/media/instruments-memory-usage.png)](https://oleb.net/media/instruments-memory-usage.png)

<sub>Michael Jurewitz 用于内存使用测量的工具集。</sub>

**Activity Monitor** 可用于将你的 App 的资源使用率与当前在后台的其他 App 进行比较。例如，按“实际内存（Real Memory）”对 App 列表排序，并选中“跟踪检查头（Track inspection head）”选项。当你现在在刚录制的时间线上拖动检查头时，你会看到你的 App 根据其使用内存的多少，在其他后台 App 中上升（或下降）。

[![Activity Monitor 选项](https://oleb.net/media/instruments-activity-monitor-options.png)](https://oleb.net/media/instruments-activity-monitor-options.png)

<sub>Activity Monitor 选项。</sub>

**Allocations** 工具可能会产生误导，因为它并没有显示你 App 使用的所有内存（只显示了 `malloc` 类型的分配）。尽管如此，你应该警惕以下模式：

- 不断增长的分配图显然是一个不好的迹象。它通常表明存在一些**严重的内存泄漏**。如果你不解决这个问题，你的 App 迟早会因为耗尽内存而崩溃。
- 当你在 App 中重复执行相同操作时（例如，切换到另一个屏幕，然后返回到第一个屏幕），你的内存使用量**不应该增加**。在分配图上，你通常会在开始操作的那一刻看到增长（因为需要创建新视图），并在返回到起始位置后很快看到下降，特别是当你多次重复此操作时。

  如果你看到很少或只有部分内存被回收，这就是泄漏或**被遗弃内存**块的迹象，可能导致原因是一个**保留循环**。使用 Instruments 的 **Heapshot 分析（Heapshot Analysis）**来追踪这些问题。通过在重复相同操作之间点击“标记堆（Mark Heap）”，Instruments 可以精确地显示哪些对象没有被释放。查看列表通常可以让你走上正轨。

  [![Allocations 工具的 Heapshot 分析选项](https://oleb.net/media/instruments-allocations-options.png)](https://oleb.net/media/instruments-allocations-options.png)

  <sub>Allocations 工具的 Heapshot 分析选项。</sub>
- **大的内存峰值**会导致系统从内存中淘汰只读页面，因为 OS 知道以后可以从磁盘读回它们。由于你的 App 代码也属于这些可重新加载的只读页面的一部分，一个大的内存峰值（即使只持续几毫秒）可能会导致当系统淘汰后来又必须重新加载你的 App 代码时，你的 App 出现卡顿。如果可以的话，尽量避免它们。

> **VM Tracker 中的 Dirty/Resident Size（脏/驻留大小）提供了你 App 使用的实际内存的最精确视图。**

**VM Tracker** 工具很有用，因为它可以显示你的 App 使用的**实际内存量**。两个列，“驻留大小（Resident Size）”和“脏大小（Dirty Size）”分别显示了可以映射到磁盘或无法回收的内存量。根据 Michael 的说法，在 **Dirty** 行和 **Resident Size** 列中显示的数值，是在时间线上当前选定点你的 App 正在使用的内存的最精确视图。如果这与 Allocations 工具指示的值截然不同，不要感到惊讶。

# 3. 高效绘制/低效绘制

> **经验法则：如果屏幕区域超过 50% 由透明图层构成，滚动很可能会开始卡顿。**

**Core Animation** 工具可以帮助你识别绘制代码中的性能问题。通过对你 App UI 中的图层进行颜色编码，你可以快速一览当前情况。

[![Core Animation 工具选项](https://oleb.net/media/instruments-coreanimation-options.png)](https://oleb.net/media/instruments-coreanimation-options.png)

<sub>Core Animation 工具选项。</sub>

即使你的 App UI 只包含普通的 UIKit 控制，而你自己并不实际绘制任何内容，也可能犯下严重影响性能的错误，尤其是在滚动时。根据 Michael 的说法，你应该特别警惕：

- **过多的透明度：** 透明图层会使 GPU 的合成工作困难得多，因此你应该尽可能避免它们。当然，从投影到圆角，有很多漂亮效果都依赖于透明度，但归根结底，你的用户可能会更欣赏一个滚动流畅的 App，而不是一个看起来更漂亮但滚动不顺畅的 App。

  Michael 特别强调了自定义表格单元格（cell）中文本标签的构建。大多数标签可以保持不透明并带有固定的背景颜色，因为表格视图（table view）实际上会在选中单元格时负责切换背景颜色。而如果你确实需要透明度，至少确保**两个透明标签不要重叠**（这会成倍增加 GPU 的工作量）。

  Core Animation 工具将透明图层标记为**红色**（不好），将不透明图层标记为**绿色**（好）。
- **绘制缩放的内容：** 缩放图像会给图形系统带来额外的工作，这通常可以通过让你的 App 资源尺寸正确来避免。如果你的 App 从网络下载动态内容，在代码中将图像缩小到显示的确切尺寸通常是合理的。

  Core Animation 工具将缩放内容标记为**黄色**。不过，并非所有缩放都是不好的。Core Animation 工具也会将许多标准 UIKit 元素（如导航栏和标签栏）标记为黄色，因为它们使用**拉伸**图像作为背景。这是完全没问题的。
- **绘制像素未对齐的内容：** 尽管 Core Graphics 中的坐标系使用浮点数，但这些坐标在显示前必须映射到设备的固定像素网格。确保将你的内容绘制在**整数坐标**上，以避免图形系统进行抗锯齿处理，这既会消耗性能，也会让你的图形看起来模糊。Core Animation 工具将对齐不当的内容标记为**洋红色**。

另请参阅 [Cyril Godefroy 关于同场演讲的博客文章](http://cyrilgodefroy.com/blog/2011/11/Apple-tech-talk-was-cool/)，发布于伦敦 iOS Tech Talk。

**2011 年 11 月 18 日更新：** Benjamin Godard [也针对演讲的这一部分写了博客](http://www.cocoabyss.com/coding-practice/understanding-misaligned-images-in-instruments/)。查看 Benjamin 文章中的截图，了解需要注意什么。
