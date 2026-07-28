---
title: 分析堆内存
session_id: 10173
collection: wwdc2024
year: 2024
duration: '33:03'
topics: [Swift, Developer Tools]
group: B · 内存管理与内存性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10173/'
content_hash: 'sha256:e12efb73b4ee3cbd'
translated: true
---

# 分析堆内存

<sub>WWDC2024 · 33:03 · Swift、Developer Tools</sub>

深入了解 App 动态内存的基础：堆内存（heap）！探索如何使用 Instruments 和 Xcode 来测量、分析和修复常见问题……

> [!note] 归档理由
> 堆内存分析的现代工具链与判读方法

## 章节

- [引言](/videos/play/wwdc2024/10173/?time=0)
- [堆内存概述](/videos/play/wwdc2024/10173/?time=65)
- [检查堆内存问题的工具](/videos/play/wwdc2024/10173/?time=225)
- [瞬时内存增长概述](/videos/play/wwdc2024/10173/?time=460)
- [在 Swift 中管理自动释放池的增长](/videos/play/wwdc2024/10173/?time=634)
- [持久内存增长概述](/videos/play/wwdc2024/10173/?time=837)
- [Xcode 内存图调试器的工作原理](/videos/play/wwdc2024/10173/?time=960)
- [可达性与确保内存被正确释放](/videos/play/wwdc2024/10173/?time=1215)
- [解决 Swift 闭包上下文（closure context）的泄漏](/videos/play/wwdc2024/10173/?time=1314)
- [泄漏常见问题解答](/videos/play/wwdc2024/10173/?time=1453)
- [比较 weak 与 unowned 的性能](/videos/play/wwdc2024/10173/?time=1611)
- [减少引用计数（reference counting）开销](/videos/play/wwdc2024/10173/?time=1844)
- [测量的成本](/videos/play/wwdc2024/10173/?time=1926)
- [总结](/videos/play/wwdc2024/10173/?time=1950)

## 相关资源

- [引言](https://developer.apple.com/videos/play/wwdc2024/10173/?time=0)
- [堆内存概述](https://developer.apple.com/videos/play/wwdc2024/10173/?time=65)
- [检查堆内存问题的工具](https://developer.apple.com/videos/play/wwdc2024/10173/?time=225)
- [瞬时内存增长概述](https://developer.apple.com/videos/play/wwdc2024/10173/?time=460)
- [在 Swift 中管理自动释放池的增长](https://developer.apple.com/videos/play/wwdc2024/10173/?time=634)
- [持久内存增长概述](https://developer.apple.com/videos/play/wwdc2024/10173/?time=837)
- [Xcode 内存图调试器的工作原理](https://developer.apple.com/videos/play/wwdc2024/10173/?time=960)
- [可达性与确保内存被正确释放](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1215)
- [解决 Swift 闭包上下文的泄漏](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1314)
- [泄漏常见问题解答](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1453)
- [比较 weak 与 unowned 的性能](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1611)
- [减少引用计数开销](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1844)
- [测量的成本](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1926)
- [总结](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1950)
- [The Swift Programming Language: 自动引用计数](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/)
- [论坛: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10173/4/5ADD00F7-AAD5-4C66-A3ED-9FC7E27C7720/downloads/wwdc2024-10173_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10173/4/5ADD00F7-AAD5-4C66-A3ED-9FC7E27C7720/downloads/wwdc2024-10173_sd.mp4?dl=1)
- [在 Swift 中使用不可拷贝类型](https://developer.apple.com/videos/play/wwdc2024/10170)
- [探索 Swift 性能](https://developer.apple.com/videos/play/wwdc2024/10217)
- [分析和优化游戏的内存](https://developer.apple.com/videos/play/wwdc2022/10106)
- [检测和诊断内存问题](https://developer.apple.com/videos/play/wwdc2021/10180)
- [iOS 内存深入剖析](https://developer.apple.com/videos/play/wwdc2018/416)
- [ThumbnailLoader.makeThumbnail(from:) 实现](https://developer.apple.com/videos/play/wwdc2024/10173/?time=601)
- [ThumbnailLoader.loadThumbnails(with:)，包含自动释放池增长问题](https://developer.apple.com/videos/play/wwdc2024/10173/?time=623)
- [简单的自动释放示例](https://developer.apple.com/videos/play/wwdc2024/10173/?time=633)
- [循环中的自动释放池增长](https://developer.apple.com/videos/play/wwdc2024/10173/?time=668)
- [循环中的自动释放池增长，由嵌套池管理](https://developer.apple.com/videos/play/wwdc2024/10173/?time=710)
- [ThumbnailLoader.loadThumbnails(with:)，修复了嵌套自动释放池增长问题](https://developer.apple.com/videos/play/wwdc2024/10173/?time=736)
- [带虚方法的 C++ 类](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1047)
- [不带虚方法的 C++ 类](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1060)
- [ThumbnailRenderer.faultThumbnail(from:)，错误地缓存缩略图](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1121)
- [ThumbnailRenderer.faultThumbnail(from:)，正确地缓存缩略图](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1168)
- [使用闭包上下文创建引用循环的代码](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1339)
- [PhotosView 图像加载代码，存在泄漏](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1391)
- [PhotosView 图像加载代码，泄漏已修复](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1420)
- [手动管理分配的有意泄漏](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1464)
- [循环手动管理分配的有意泄漏](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1512)
- [不返回函数（nonreturning function）可能报告局部变量拥有的分配泄漏](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1571)
- [对不返回函数中报告的泄漏的修复](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1582)
- [弱引用示例](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1641)
- [无主引用示例](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1663)
- [方法隐式使用 self 导致引用循环](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1747)
- [使用 weak 打破由方法隐式使用 self 导致的引用循环](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1765)
- [使用 unowned 打破由方法隐式使用 self 导致的引用循环](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1781)
- [带非平凡 init/copy/deinit 的结构体](https://developer.apple.com/videos/play/wwdc2024/10173/?time=1874)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎观看《分析堆内存》！这位是 Ben，这位是 Daniel！今天我们将讨论堆内存（heap memory）和你 App 之间的关系。堆内存会被 App 直接或间接地使用，作为开发者，你可以控制和优化它。你的 App 的引用类型（reference types）就存储在这里，这一点之所以重要，是因为它通常会被写入和变为脏页，这会占用你 App 的内存限制。因此，本次讲座的重点将是测量和减少堆内存。

如果你有兴趣了解更多关于其他类型内存（如图形内存或内存限制）的信息，还有另外一些精彩的讲座会详细讨论这些内容。

那么，无论你的 App 是使用了过多内存，还是像我一样只是好奇，想窥探一下内部运作，让我们开始吧！今天我们将涵盖五个主题：测量你的堆内存、处理瞬时增长、追踪持久增长、修复内存泄漏以及改善运行时性能。让我们从提出问题开始！什么是堆内存，我们可以使用哪些工具来测量 App 使用了多少堆内存？要理解堆内存，我们需要看看它在 App 的整体虚拟内存（virtual memory）上下文中所处的位置。当 App 启动时，它会获得自己独立的虚拟内存空地址空间。

当 App 启动时，系统会加载它的主可执行文件、链接的库和框架，并从磁盘映射只读资源（read-only resources）的区域。运行时，App 还会为每个线程的局部变量（local variables）和临时变量使用栈区域（stack areas），而动态和长期存在的内存则会被放置在统称为堆内存的内存区域中。今天，我们将重点关注这一部分。让我们放大来看！堆内存不仅仅是一个内存块，它同样由多个虚拟内存区域组成。

再放大到区域级别，每个区域都被分解为单独的堆内存分配（heap allocations）。在底层，每个区域由操作系统提供的 16KB 内存页（memory pages）组成，但每个分配可以更大或更小。这些内存页可以处于三种状态之一：干净（Clean）、脏页（Dirty）或已交换（Swapped）。干净页是尚未被写入的内存。这可能是已分配但未使用的空间，或者是代表从磁盘映射的只读文件的页面。这些页面开销很低，因为系统可以随时丢弃并重新加载这些页面。

脏页是最近被应用程序写入过的内存。当脏页一段时间未被使用时，它们不能被丢弃。如果出现内存压力，系统可以对它们进行交换，压缩它们或将其写入磁盘。这样，当它们再次被需要时，内存可以从磁盘解压或加载回来。

在这三种状态中，只有脏页和已交换才会计入应用程序的内存占用空间（memory footprint），并且在大多数应用程序中，堆内存将负责其中的大部分。

堆区域是使用 malloc 函数或类似的分配原语（如 calloc 或 realloc）创建的内存。在许多情况下，你不会直接调用这些函数，但编译器和运行时会大量使用它们，例如，当你创建 Swift 或 Objective-C 类的实例时。Malloc 让你的 App 能够动态分配长期存在的内存。分配会保持存活，直到它们被显式释放，这意味着它们的生命周期可以超出创建它们的代码的作用域。这些函数强制执行一些规则，例如，它们的最小分配大小和对齐是 16 字节，这意味着如果你请求 4 个字节，你的请求会被向上取整到 16。此外，作为一种安全特性，大多数小尺寸分配在释放时会被清零。语言运行时使用堆来分配长期存在的内存。例如，Swift 会展开类初始化器，调用一系列 Swift 运行时函数，这些函数最终会调用 malloc。

Malloc 也有一些调试功能。其中之一是 MallocStackLogging，它会记录每次分配的调用栈（call stacks）和时间戳。启用 MallocStackLogging 使得追踪内存分配的地点和时间变得容易得多。

在 Xcode 中，你可以在 Scheme 诊断选项卡中通过勾选复选框来启用 MallocStackLogging。我们今天就为所有演示启用了这样的 malloc 栈日志记录。

对于追踪内存使用情况，我们第一个可用的工具是 Xcode 内存报告，它显示应用程序的占用空间随时间的变化。应用程序的占用空间不仅仅由其堆组成，但内存报告可以显示较大的内存问题和一些近期历史记录。不幸的是，它无法告诉你内存使用为什么在增长。我们需要其他工具来帮助我们理解这一点。

我们今天将涵盖的另一个工具也是 Xcode 的一部分。内存图调试器（Memory Graph Debugger）可以捕获内存图，它是所有分配以及它们之间引用的快照（snapshot）。

启用 MallocStackLogging 后，这包括每次分配的回溯（backtraces）。

如果你需要关注某个特定的分配，这是一个很好的工具，并且可以直接从 Xcode 的调试栏（debug bar）访问。

Xcode 还包含一些用于内存分析的强大命令行工具。Leaks、heap、vmmap 和 malloc_history 可以直接分析 macOS 和模拟器进程，或使用已捕获的内存图来调查问题。我建议查看这些工具的手册页以了解它们的更多高级功能。

对于分析随时间变化的内存使用情况，Instruments 应用程序提供了几个可用的模板。

Allocations 仪器会记录所有分配和释放事件随时间变化的历史，聚合统计信息和调用树，以帮助将这些事件回溯到你的代码。Leaks 仪器会定期拍摄 App 内存的快照，以检测内存泄漏。让我们看看如何使用 Allocations 来调查我们的 DestinationVideo 示例应用程序中的问题。

我正在处理我和 Daniel 为 DestinationVideo 应用程序开发的一个新功能，遇到了内存问题。它允许用户为视频选择一个新的背景图像。

我打开和关闭背景图像画廊几次，然后看到 App 因为使用了太多内存而崩溃。

每次我打开画廊时，Xcode 内存报告都显示内存使用再次飙升，达到近 1GB。我们可以使用 Allocations 仪器来分析这个问题。我会在我的设备上测试。

要在 Instruments 中进行性能分析，我使用“Product”菜单下的“Profile”菜单项。这将执行 App 的发布构建，并打开 Instruments，同时选择 App 作为目标。当 Instruments 打开时，它会要求我们选择一个用于性能分析的模板。在这种情况下，我们想要分析 App 的堆内存，所以我选择 Allocations。Allocations 模板包括两个仪器：Allocations 和 VM Tracker。Allocations 实时记录堆和 VM 事件，帮助我们在实时中看到活动。VM Tracker 可以定期快照以测量所有虚拟内存。我今天不会启用它，因为我特别关注堆内存。我将通过点击轨迹文档左上角的“Record”按钮开始追踪。

当追踪开始时，关于我们 App 的数据开始流入。

轨迹视图显示，App 的内存使用在加载后保持稳定。我将打开和关闭画廊视图，看看内存使用飙升时发生了什么。

这比上次慢了一点，但这在预期之中。

我得到了每次 malloc 和 free 的栈回溯。这些数据马上就会变得非常有用。

我将通过点击左上角的“Stop”按钮停止追踪。在 Allocations 轨迹中，我们清楚地看到了重复出现的峰值模式。现在我已经有了一个追踪文件，我可以把它发送给喜欢处理内存错误的搭档。我将使用“File”菜单下的“Save”菜单项保存追踪，现在，这成了 Daniel 的问题。

Daniel，你想谈谈如何诊断瞬时内存增长（transient memory growth）吗？当然，Ben！让我们更深入地看看 Ben 记录的内存峰值，看看我们是否能做些什么。App 中的内存峰值是瞬时内存增长的一种类型，这种增长之所以有害，有三个原因。

内存峰值会导致内存压力，系统会做出反应。它会交换和压缩脏内存、丢弃只读内存，甚至终止后台任务。在最坏的情况下，这些峰值也可能意味着你的 App 被终止。内存峰值的长期影响也很糟糕，因为它会在堆内存区域中导致碎片化或空洞。

有两种方法可以追踪它。我们可以查看特定的峰值，找到从低点到高点“已创建且仍存活（Created & Still Living）”的分配。或者，我们可以聚合选择一个大范围，找到在该范围内“已创建且已销毁（Created & Destroyed）”的所有分配。现在让我们用 Ben 发给我的追踪试试。

我将通过在轨迹视图中从低点点击并拖动到峰值的顶部来选择时间线上的一个峰值间隔，下方的统计详情应该会显示一些关于导致它的原因的信息。让我按总字节数对这些行排序，并寻找最主要的贡献者。尽管我们在本次讲座中关注的是堆内存，但最靠前的类别看起来是 IOSurface 虚拟内存。这是一个很好的提示，表明我们临时内存问题可能与处理背景图像的方式有关。如果我按持久化（persistent）排序，在本例中，是到达峰值的对象，其中一个节点引起了我的注意：@autoreleasepool content。这里有数百个被创建，对于自动释放池来说这个数量是很大的。我稍后会回到这一点。另一种查找临时内存问题的方法是找出负责在更大范围内创建和销毁对象的代码。在窗口底部，我将生命周期筛选器（Lifespan filter）改为“已创建且已销毁”。在时间线上，我选择所有三个峰值。

现在我可以使用中间的跳转栏将详情视图切换到调用树（call tree）。调用树是一种按回溯分解分配的好方法，这让我能够看到分配最多内存的代码。

看看总量，有 8GB 的临时分配？哇。这些是从哪里来的？右侧最重的栈回溯给了我一个关于去哪里查看的好线索。让我把它拉宽一些。

来自我的代码的帧被高亮显示，查看这个列表，makeThumbnail() 代码看起来是一个不错的起点。我可以单击一次以快速展开调用树，或者双击以查看源代码。

哦，是的，这是我们正在应用的图像滤镜，有一行显示了大量的内存，几千兆字节，被创建和销毁。这应该是临时内存，但我们看到它在增长，直到峰值顶部，然后所有内存一次性被释放。让我先通过在跳转栏中点击返回调用树来向上查看几个帧。向上看几个帧，这次我想去 ThumbnailLoader 的 loadThumbnails 代码。

它在一个循环中加载缩略图，内存随着循环运行而增长，然后在结束时下降。结合之前的自动释放池（autorelease pool）线索，我想我知道发生了什么。

尽管我使用的是具有自动引用计数（automatic reference counting，ARC）的 Swift，但自动释放池是导致临时内存增长的常见原因。Objective-C 使用这些池来延长函数返回值的对象生命周期。自动释放池通过将 release 延迟到稍后时间来保持这些返回值的存活。但这同时也意味着，当 Swift 调用使用或暴露 Objective-C API 的框架时，它也可能会产生自动释放的对象。这个简单的例子打印了当前日期，但它也创建了一个自动释放的字符串。该字符串将一直存在于堆上，直到当前自动释放作用域结束，这可能需要一段时间。

线程通常有一个顶级的自动释放池，但它并不经常被清理。当代码用对象填满池子时，这一点就变得非常重要，这在循环中很容易发生。

每次迭代，对象都被自动释放到同一个池中，它们的生命周期可能会比必要的时间长。在这种情况下，一直等到循环全部完成。在内部，自动释放池会分配内容页面来引用这些对象。由于这些在 Allocations 仪器中可见，因此它是发现此类问题的一个好方法。稍后当自动释放池被排空时，池会发送延迟的 release，并且许多对象可以同时被释放。

对此的修复通常是定义一个嵌套的局部自动释放池作用域来缩小这些生命周期。在这个例子中，自动释放的对象由内部的每个循环的池持有，并在每次迭代时被释放。这意味着累积的对象更少，并且跟踪引用所需的内容页面也更少。

让我们跳回去，看看是否能解决我们的问题。

从 Instruments 中，我将使用源视图右上角的菜单在 Xcode 中打开这个文件。

为了解决这个问题，让我们在循环体内部添加一个自动释放池作用域，它会在每次迭代后排空对象。

让我们看看这样效果如何。

哦，不，我没有带我的开发手机。嘿，Ben，我可以用你的手机测试我的修复吗？不行！这是我的手机。你为什么不用模拟器呢？好吧，说得对。对于大多数性能分析来说，在真实设备上运行发布构建以获得准确的时间非常重要。然而，对于堆分析来说，模拟器环境在行为上要接近得多，并且用于内存性能分析是可以的。我会在尝试 Ben 展示的功能时切换回内存仪表。

在模拟器中，我将打开画廊一次然后关闭它。

仪表看起来好多了，内存上升了，但这次没有巨大的峰值。

第二次也一样，但我现在开始看到另一个我不喜欢的模式。

在调出表单（sheet）三次后，我可以确认，内存峰值消失了！我们从未接近 1GB。但现在我们的问题是每次内存都像阶梯模式一样上升。这很奇怪，因为即使创建缩略图很昂贵，它也只应该在我第一次打开画廊时增长。我会稍后推送我的自动释放池修复，但我不想抢走所有乐趣。

从 Xcode 的调试栏中，我将暂停在内存图调试器中。这会捕获我应用程序堆中的每一次分配，如果我已经知道是什么类型导致了增长，我现在就可以搜索它。或者在右侧，我可以分享它。

虽然我可以直接在 Instruments 中导入这个内存图，但我想我更愿意通过隔空投送把它发给 Ben。

也许他会有一些在茫茫数据中找到目标的主意。祝你好运，Ben！想得美，Daniel，我才不会再次被耍！我会使用我自己的内存图来研究这个持久增长。持久内存（Persistent memory）是那些不会被释放的内存。持久增长通常看起来像这样。内存随时间增加。这种增长由多次分配组成。

Allocations 仪器中的标记代（Mark Generation）功能可以按时间段分解增长。当我点击“Mark Generation”按钮时。

Instruments 会为分配创建一个新组。这一代收集了在此时间点之前创建的所有分配，并且这些分配持续存在直到追踪结束。当我选择一个更晚的时间并再次点击“Mark Generation”时，Instruments 会创建一个新组。下一代收集了在前一代之后、新时间戳之前创建的所有持续存在的分配。我在 Xcode 中生成了我自己的内存图，并将其导入到 Instruments 中。

Instruments 在 Allocations、Leaks 和 VM Tracker 仪器中显示数据。我现在将关注 Allocations 轨迹。在轨迹视图中，我可以看到 Daniel 在 Xcode 内存报告中注意到的相同阶梯模式。我将使用代标记功能来隔离在增长间隔期间创建的持久分配。我将在增长期间选择几个时间点，然后按下“Mark Generation”按钮。

Instruments 现在显示了三代。代 B 和代 C 显示了由打开画廊引起的持久增长。我可以展开其中一代来查看其分配，并按增长大小排序，以查看哪些类型在最大的增长中占主导地位。看起来大部分增长来自 Data 的存储。我可以展开此类型的条目，查看单个分配及其地址。哈！我找到了目标！看起来，所有这些 Data 存储分配都是由我们的 ThumbnailLoader 代码创建的。那么是什么持有 Data 呢？我们可以从 Instruments 中取出其中一个地址，放入内存图调试器中，看看是什么引用了它，这应该能告诉我们为什么在画廊关闭后它仍然存在。我将从扩展详情视图中复制地址，并放入内存图调试器的筛选栏中，然后选择该分配。

为了更好地理解内存图调试器告诉我们什么，让我们谈谈它是如何工作的。

调查内存增长的核心就是问这个问题：为什么这个分配仍然存在？是什么在持有它？这正是内存图调试器帮助回答的问题。为了充分利用这个工具，我们需要谈谈类型信息（type information）和引用扫描（scanning for references）。有四种主要类型的引用：强引用（Strong references），它绝对是指针，位于由 ARC 管理并具有显式所有权保证的位置。弱引用（Weak）和无主引用（Unowned），它们也绝对是指针，位于具有显式非所有权保证的位置。非托管引用（Unmanaged references），它们是运行时知道但并不自动管理的位置中的指针。这些可能是手动拥有的引用，但也可能不是。以及不确定的（Uncertain）或保守的（Conservative）引用。当工具不知道它们正在扫描的内存类型，只是看到原始内存时，会记录这些引用。如果该值看起来像一个指针，也许它确实是，但如果没有类型信息，确实无法确定。当工具扫描你的进程的堆时，它们会为每次分配使用可用的最佳类型信息。

对于这个 Swift Swallow 例子，前两个字段是标准的，不包含任何对引用扫描重要的内容。之后，我们有一个要扫描的 coconut 引用！这个字段确实持有一个指向堆内存分配的指针，它是一个指向 Coconut 对象的强引用！Swift 和 Objective-C 的类型信息很好，但对于 C 和 C++，没有引用所有权信息，所以你只会看到保守引用。对于带有虚方法的 C++ 类型，工具最多只能查找名称。这个类的一个实例将被视为 Coconut。

对于没有虚方法的类型或其他分配，栈回溯可以帮助提供名称。使用 MallocStackLogging 数据，这个类的一个实例可能被标记为 PalmTree::growCoconut() 中的 malloc，这很好地提示了它可能是什么。

现在我们已经讨论了类型信息和引用，让我们回去查找为什么我们的数据存储会永久存在。

在内存图调试器中，我们可以看到我们选择的分配被一个 __DataStorage 对象持有。该对象被一个 PhotoThumbnail 持有。PhotoThumbnail 又被一个字典持有。一直往回看，看起来它被静态属性 ThumbnailLoader.globalImageCache 持有。因为我启用了 MallocStackLogging 运行，所以可以在右侧的检查器中看到分配的回溯。我将使用检查器导航到负责分配的源代码。

让我们选择持有数据的 PhotoThumbnail。

看起来我代码中的一个闭包负责分配这个。我将使用栈回溯跳转到那段代码。

看起来这个 faultThumbnail 方法正在缓存缩略图，并在缓存未命中时创建一个新的。我打赌它存储在刚才看到的那个 globalImageCache 中。

从注释来看，我们似乎正在基于 URL 和 creationDate 进行缓存，这看起来是合理的。但是有一个 bug！那显然不是文件的创建时间戳！那是当前时间。这意味着我们永远无法在缓存中找到任何东西，每次调用此方法时，我们都会缓存一个新的 PhotoThumbnail。这就解释了为什么我们看到缩略图的持久增长！让我们修复它，改为基于文件的创建日期进行缓存。我将删除使用错误时间戳的代码，现在我需要获取文件的创建时间戳。不错，Xcode 建议了我想要的代码。我按 Tab 键接受它。

我将再次运行 App，以验证修复了我们的问题，确保阶梯模式不会出现在 Xcode 的内存报告中。

让我们再试试那个功能。

好的，我们已经生成了缩略图，现在让我们再试一次。

不错，没有增长。我再试一次以确保。

让我们在内存图调试器中暂停，只是确保没有其他问题。

我看到发现了一些内存泄漏，是旁边带有黄色三角形图标的分配。

Daniel，你又在我们的代码中制造泄漏了吗？是的，是我！我想这是件好事，泄漏内存是我们列表上的下一个议题。要理解和修复泄漏内存，我们首先需要谈谈可达性（reachability）。

程序中的所有内存都应该通过非弱引用从某个地方可达，以便将来使用。你的堆上有三种内存。

首先，可用内存（useful memory），它是程序可达的，并且将来会再次使用。

其次，遗弃内存（abandoned memory），它是可达的并且可以使用，但实际上永远不会再被使用。这部分内存会计入 App 的占用空间，并且完全是浪费。这很容易发生，例如过于激进地缓存或在单例上持有大量数据。你的 App 中的第三种内存是泄漏内存（leaked），即永远无法再次使用的不可达内存。这通常发生在最后一个指针丢失时，要么是手动管理的分配，要么是对象的引用循环（reference cycle）。

对于大多数泄漏，我们的目标是找到并修复循环中的一个引用。这可能意味着移除一个意外的引用，或者将所有权限定符从 strong 改为 weak 或 unowned。为了更轻松地调查这些泄漏，我将使用筛选栏中的“仅显示泄漏的分配”按钮，它也有三角形图标。

导航器显示按 App 中不同二进制文件分组的类型。你的代码可能会泄漏系统二进制文件的类型，但泄漏通常直接由项目中的问题引起。我将通过点击另一个筛选栏按钮，仅筛选我的项目类型。这更易于处理了！ThumbnailLoader 类有 3 处泄漏，ThumbnailRenderer 也有 3 处。我将选择其中一个。这看起来像是 ThumbnailRenderer、ThumbnailLoader 和一个闭包上下文之间的一个小型引用循环。但是闭包上下文是做什么的？让我们花点时间谈谈。

当 Swift 闭包需要捕获值时，它们会在堆上分配内存来存储捕获值。内存图调试器将这些分配标记为闭包上下文（closure contexts）。你 App 堆中的每个闭包上下文都与一个存活的闭包一一对应。

闭包默认强捕获引用，这使得创建引用循环成为可能。你可以改用 weak 或 unowned 捕获来打破这些循环。

假设我有一个带有完成处理程序（completion handler）的 Swallow 对象，当 swallow 送来椰子时会调用它。如果不小心，这会通过强捕获 Swallow 自身来创建一个引用循环。内存图调试器会将引用显示为强捕获，但闭包元数据不包含变量名。来自闭包上下文的所有引用都简单地标记为捕获（capture）。让我们回去看看是否能解决我们的泄漏。

我将打开检查器并点击这些引用中的几个。

ThumbnailRenderer 有一个指向加载器的 cacheProvider 引用。加载器有一个指向闭包上下文的 completionHandler 引用。如果我选择回到渲染器的捕获，检查器会向我显示引用是强引用。

要打破这个引用循环，我们需要找到创建闭包的代码。

从闭包上下文的栈回溯，我将跳转到我的 PhotosView 代码。

这段代码正在创建一个 ThumbnailLoader 对象，为其分配一个完成处理程序，然后告诉它开始加载。

但我们刚才看到的问题是，闭包强捕获了 ThumbnailRenderer，这导致了引用循环。那么修复方法是什么？嗯，我们可能应该更改这段代码以使用 Swift 并发（Swift Concurrency）而不是完成闭包。但就目前而言，我们可以指定一个捕获列表。无论是 weak 还是 unowned 都能打破循环。

我将把 renderer 的捕获改为 weak，由于我们现在有一个可选的弱引用，我添加了这个 guard let 来确保在使用 renderer 时目标仍然存在。

我刚才做的修复是针对一个 3 节点循环的，但像这样的小改动可能会产生大影响。在我们再次尝试功能并在内存图调试器中暂停后，现在我没有看到任何我的类型泄漏。如果我关闭类型筛选器，还有另一个惊喜——其他的泄漏也被解决了！那些其他类型被我们刚刚修复的泄漏所引用，现在它们也被释放了。在这个例子中，发现并修复泄漏相当容易。然而，代码泄漏的方式有很多种，而发现泄漏可能是问题最多的地方。让我们讨论其中的几个，从“为什么泄漏检查不能发现所有问题”开始。假设我故意创建一个泄漏。为什么工具不总能找到它？有很多内存工具没有类型信息，像 C 这样的语言允许非托管指针。这意味着工具必须允许那些看起来可能是指针但实际可能不是的东西。

当工具进行保守扫描（conservatively scan）时，它们会逐字节地寻找指针，查找看起来像引用的值，然后对照分配列表进行检查。如果值匹配，那么工具会记录一个不确定的、保守的引用指向该块。但请记住，该值可能是一个数值、标志位，或者只是看起来像有效指针的随机字节。

所以回答这个问题，由于保守引用，可能会遗漏真正的泄漏。如果我想创建一个有意的泄漏并希望它被发现，把它放进一个执行 100 次的循环中也没什么坏处。在真实的 App 中，泄漏的代码通常会运行多次，所以即使工具没有发现每一个泄漏，它们仍然会抓住导致泄漏的错误。另一个相关的问题是，报告的泄漏数量为何会随时间上下波动？Bug 会随着时间的推移导致更多的泄漏，但堆可能非常嘈杂和随机。这种噪声使得保守引用变得不确定，因此它们可能出现或消失。所以即使你的程序在启动时泄漏了 5 个对象，工具最初可能发现 5 个，稍后只找到 4 个。

另一个常见的问题是，为什么不返回函数（nonreturning functions）有时看起来会泄漏内存。这可能是指具有 noreturn 特性的 C 函数或返回 Never 类型的 Swift 函数。因为这些函数永远不会返回，编译器可以优化掉它们通常必须做的清理工作，包括释放它们创建的局部分配或引用。当这类函数用于致命断言时，没问题——程序反正就要崩溃了！但有时它们被用来永久挂起某个线程。如果你曾经看到局部状态被报告为从对不返回函数的调用中泄漏，例如本例中的 Server 对象，一种解决方案是将其显式存储到一个全局变量中。

通过将对象存储在局部函数作用域之外，引用最终会出现在工具可以看到的地方。并且由于工具可以看到它，该对象将被视为可达而不是泄漏，即使局部变量没有被编译器以其他方式保留。现在我们已经涵盖了泄漏，我想把时间交还给 Ben，让他谈谈运行时速度和椰子。谢谢，Daniel！减少内存可以极大地提高 App 的性能，还有一些运行时细节需要记住，可以进一步提升性能。

weak 和 unowned 是你在 Swift 中用来避免创建强引用循环的两种常见工具。

让我们谈谈它们的区别以及何时使用它们。

弱引用始终是可选的类型，并且在它们的目标被反初始化后变为 nil。无论源和目标的生存期如何，你总是可以使用弱引用。考虑一下 swallow 和 coconut 的情况。一个 coconut 可以被 swallow 携带，但它并不拥有 swallow。

如果我们希望 coconut 引用 swallow，我们不应该使用强引用。我们可以改用弱引用。

不过，这有开销。为了实现弱引用，Swift 会在目标对象第一次被弱引用时为其分配一个 Swift 弱引用存储（weak reference storage）。这个分配位于 Swallow 和它的所有传入弱引用之间。它允许在 Swallow 消失后将弱引用惰性地设为 nil。

与弱引用不同，无主引用直接持有它们的目标。这意味着它们不使用任何额外的内存，并且访问所需时间比弱引用更少。它们甚至可以是非可选的，也可以是常量。然而，并非总是可以使用无主引用。假设我们让 Coconut 的 'holder' 引用变成 unowned 而不是 weak。如果在我们的引用之前 Swallow 消失了会发生什么？Swallow 会被反初始化，但不会被释放。这就是使无主引用安全的原因。无主引用必须指向某个东西，所以运行时会保持那只 ex-parrot 或 swallow——我在这里混淆了比喻。此时，如果我尝试使用 Coconut 的无主引用来访问 Swallow，我会得到一个确定性的崩溃。这样看来，无主引用很像强制解包弱引用。即使我不访问无主引用，让它存在也是不好的。只要无主引用存在，它的目标就不能被释放并浪费内存。如果你不知道目标将存活多久，那么弱引用的小开销是值得的。

如果你没有在你的内存图中看到 weak 或 unowned 引用的报告，你可能需要检查项目中 Xcode 的 Reflection Metadata Level 构建设置。我们建议尽可能使用默认的 All 级别。此设置包含工具所需的所有元数据，并使工具能够为 Swift 提供更好的准确性。

让我们看一个具体的例子。

这个 ByteProducer 类有一个 generator 属性，该属性是一个闭包，一开始被赋值给它的 defaultAction 方法。

问题是，这创建了一个强引用循环，因为 defaultAction 方法隐式使用了 self。将方法用作闭包时要非常小心。

要解决这个问题，我们可以定义一个调用 defaultAction() 的闭包。它仍然会捕获 self，但现在捕获是显式的，我们可以使用捕获列表来防止它是强引用。

我们需要指定一个引用限定符，并且 weak 在这里作为一个好的默认值肯定是可行的。

Unowned 在这种情况下也是可以的，因为 generator 闭包与其目标 ByteProducer 实例具有相同的生存期。

该闭包并未被提供（vend）给其他代码或以异步方式派发，因此它不可能超出被捕获的 self 的生命周期。

这些选择之间的性能差异有时会累积起来。如果我分配一百万个 ByteProducer，并导出一个内存图，heap 命令行工具可以快速总结成本。每个 ByteProducer 都有一个弱引用存储分配，它们使用的内存几乎和 ByteProducer 本身一样多！而使用 unowned，则不需要这部分内存。

重点是，弱引用是一个好的默认选择，而当你能够保证引用不会超出其目标的生命周期时，无主引用可以节省内存和时间。

要找出引入 CPU 开销的地方，可以进行分析并查找对运行时函数（如 swift_weakLoadStrong()）的调用。

你可以在“Swift 编程语言”的“自动引用计数”章节中了解更多关于 Swift 引用计数的信息。

除了 weak 和 unowned，有时自动的 retain 和 release 调用也可能成为性能分析的热点。尽管可能很诱人，但不要绕过 ARC。有比使用非托管指针或将性能敏感的代码迁移到内存不安全的语言更好的解决方案。

确保启用了 -whole-module-optimization，因为它可以通过允许更多的内联来减少开销。此外，进行分析并查找可能需要显式特化的泛型。

确保你最常复制的结构体拥有简单的字段也非常有帮助。性能分析可以帮助识别昂贵的结构体拷贝。对于这些结构体，尽量最小化对引用类型、写时复制类型以及 any 的使用。

有关更多 Swift 性能提示，请查看《探索 Swift 性能》和《在 Swift 中使用不可拷贝类型》。

对于 Objective-C 代码，也有几种方法可以减少 retain 和 release 的开销。

再次强调，不要绕过 ARC，因为手动引用计数导致的泄漏可能极难调试。

将方法标记为 objc_direct 以允许内联 Objective-C 方法调用，这有助于减少 retain 和 release 的流量。

对于无法内联的情况，objc_externally_retained 特性非常适合让编译器知道参数生命周期何时得到保证，从而消除 retain 和 release。

性能的一部分是要意识到观察成本。MallocStackLogging 和 Allocations 会追踪实时数据，这需要一些内存和 CPU 来记录每次分配的信息。Leaks、VM Tracker 和内存图是基于快照的，这需要在分析期间暂停目标 App。这可能导致你的 App 在快照过程中短暂卡顿或挂起。

总结一下，今天我们展示了如何使用 Instruments 来测量堆内存，并寻找瞬时和持久增长的模式。一旦你发现单个分配的问题，请使用 Xcode 的内存图调试器和 MallocStackLogging 来找出它们为何仍然存在于 App 的堆中。但最重要的是，请采取主动！分析和优化你 App 的堆内存。发现泄漏和持久增长将让用户能够更长时间地享受你的 App。再次感谢大家的参与！
