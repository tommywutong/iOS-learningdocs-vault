---
title: '剖析并优化游戏内存'
session_id: 10106
collection: wwdc2022
year: 2022
duration: '38:26'
topics: ['Graphics & Games']
group: B · 内存管理与内存性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/10106/'
content_hash: 'sha256:61c32f3c9daad2ef'
translated: true
---

# 剖析并优化游戏内存

<sub>WWDC2022 · 38:26 · Graphics & Games</sub>

了解 Apple 平台如何为你的游戏计算和分配内存。我们将向你展示如何使用 Instruments 和 Game Memory 模板……

> [!note] 归档理由
> 游戏视角的内存剖析，讲到分配器与常驻内存

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10106/5/56A1A2BE-7EF5-4AA0-AE93-1F93BD885019/downloads/wwdc2022-10106_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10106/5/56A1A2BE-7EF5-4AA0-AE93-1F93BD885019/downloads/wwdc2022-10106_sd.mp4?dl=1)
- [Optimize app power and performance for spatial computing](https://developer.apple.com/videos/play/wwdc2023/10100)
- [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101)
- [Icebreaker: Graphics and Games](https://developer.apple.com/videos/play/wwdc2022/110670)
- [Q&A: Games technologies](https://developer.apple.com/videos/play/wwdc2022/110663)
- [Q&A: Games technologies](https://developer.apple.com/videos/play/wwdc2022/110664)
- [Q&A: Metal](https://developer.apple.com/videos/play/wwdc2022/110666)
- [Q&A: Metal](https://developer.apple.com/videos/play/wwdc2022/110667)
- [Detect and diagnose memory issues](https://developer.apple.com/videos/play/wwdc2021/10180)
- [Discover Metal debugging, profiling, and asset creation tools](https://developer.apple.com/videos/play/wwdc2021/10157)
- [Available memory for the process](https://developer.apple.com/videos/play/wwdc2022/10106/?time=413)
- [Current and peak footprint](https://developer.apple.com/videos/play/wwdc2022/10106/?time=427)
- [Record an Instruments trace](https://developer.apple.com/videos/play/wwdc2022/10106/?time=604)
- [Record an Instruments trace, on a selected device](https://developer.apple.com/videos/play/wwdc2022/10106/?time=614)
- [MallocStackLogging](https://developer.apple.com/videos/play/wwdc2022/10106/?time=1012)
- [Capture a memory graph](https://developer.apple.com/videos/play/wwdc2022/10106/?time=1087)
- [Tag mapped anonymous memory](https://developer.apple.com/videos/play/wwdc2022/10106/?time=1212)
- [Tag anonymous memory](https://developer.apple.com/videos/play/wwdc2022/10106/?time=1230)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 欢迎来到「剖析并优化游戏内存」。我是 Apple GPU Software 团队的 Jack Xu（许）。我的同事 Seth Lù（陆）也将加入。过去几年，我们的团队一直在与像你一样的游戏开发者合作，共同理解并改进游戏内存。今天，我们想分享我们的经验，以便你也能在调试游戏内存时先人一步，并打造拥有最佳玩家体验的精彩游戏。

我们将从 CPU 和 GPU 对象两方面拆解游戏中的内存使用。

另外，分析游戏中的分配、物理内存上的实际使用以及对象之间的引用。因为内存有多个方面，我们的开发者工具也会从不同角度揭示内存之谜。我们将进行一次引导式导览，体验如何使用所有这些工具，包括 Xcode、Instruments 以及 Terminal 中的命令行工具。在今天的引导式导览中，我们将从理解游戏内存的序曲开始。然后开始剖析内存和内存增长，Seth 将介绍 Instruments。在使用 Instruments 进行时间维度分析之后，我们将进一步探索，使用 Xcode 和 Terminal 中的工具分析游戏的内存图。这些工作流关注内存使用的当前状态，以及游戏总内存的分解。最后，Seth 将分享如何使用 Metal Debugger 优化 Metal 资源，这是游戏内存中一个相对独立但核心的领域。现在，让我们开始理解游戏内存。

当你从 Xcode 启动游戏时，例如 Modern Rendering with Metal 示例代码，你可以在 Xcode 的调试导航器中打开这个 Memory Report。这是你对游戏当前及近期内存使用及其对系统影响级别的第一视图。

仪表盘上的数字显示游戏的当前内存使用。内存调试的重要第一步是理解这个数字的含义。

用一句话来说，游戏中的实际内存使用与分配并不相同。实际内存使用发生在物理内存上。而分配是游戏在虚拟内存地址空间上请求的内存。不同种类的分配自然会被分别计算。

当你的游戏分配内存时，这些新分配不会立即或直接占用物理内存空间。相反，它们会在系统为每个进程提供的虚拟内存地址空间上预留一些空间。只有当程序稍后实际使用这个分配时，系统才会在物理内存上准备空间。

相同种类的分配会被分组为类别，并稀疏地占用虚拟地址空间。这些类别可能包括：程序的可执行二进制；所有库和框架；栈，为局部和临时变量以及部分函数参数提供存储；动态内存区域，也称为堆，包括类实例存储和程序手动分配的内存；从只读资源（如游戏资源文件）映射的区域；当然还有游戏中的 Metal 对象，如缓冲区、纹理和管线状态对象。这些类别由区域组成。在底层，内存操作以内存页为粒度进行，现代 Apple 设备上每页 16 KiB。这意味着每个区域占用一个或多个页，至少 16 KiB 大。

随着游戏继续运行，其内存状态不断演变；新对象被分配，旧条目被销毁，区域持续变化。但只有区域上被使用的页才会在物理内存上，系统会像对任何其他 App 一样，勤勉地把这些页计入你的游戏。

游戏中的内存页可以是三种之一：dirty、compressed 和 clean。让我们看看它们是什么。Dirty 内存页包括游戏写入过的内存。这包括堆中的内存分配，以及游戏修改那些变量或符号后框架中的内存。在 Apple silicon 设备上，被访问的 Metal 资源也属于这一类，这是因为 CPU 和 GPU 共享同一池快速统一内存。

然而，如果某些 dirty 页长时间未使用，系统可能会通过压缩这些页或把它们存储到闪存/磁盘（我们称之为交换）来减少它们在物理内存上的存在。这将允许设备运行更多 App 和服务。稍后，当你的游戏再次请求这些页时，系统会从磁盘解压或换入它们。注意，你的游戏仍会被按它们的未压缩大小计费。对于 clean 内存页，它们包括从磁盘映射的只读文件，如纹理或音频资源，以及加载到进程中的框架。系统可以随时清空或从磁盘重新加载它们，因此它们不计入游戏的内存占用空间。然而，它们可能驻留在内存中，过度使用会拖慢系统和你的游戏。通常最值得看的是前两部分，合起来我们称之为内存占用空间。系统用它来执行内存限制。

在某些术语中，人们说「dirty 内存」时指的就是内存占用空间，因为 dirty 是 clean 的反面。但别担心，当事情变得模糊时，我们会明确说明我们指的是哪一个。所以现在你知道内存如何工作，以及系统如何把它计入游戏。

除了这个 Xcode 内存仪表盘，你可以在系统许多地方找到内存占用空间，包括 Mac 上的 Activity Monitor App。一些 Apple 平台用它来设定 App 内存限制。你的游戏也可以使用这个指标来引导其内存使用。有有用的 API 来查询当前占用空间和可用内存。这里快速看一下。要获取 iOS、iPadOS 或 tvOS 游戏的可用系统内存，调用 os_proc_available_memory，它位于 os/proc.h 头文件。

而对于任何 Apple 平台的内存占用空间，你可以通过 proc_pid_rusage 获取，使用从「getpid」得到的进程 ID、「rusage_info_current」（目前是版本 6）以及数据存储。并检索其 physical footprint 或 lifetime max physical footprint 属性。

总结一下，在第一部分，我们回顾了一些关于内存的概念。游戏中的分配发生在虚拟内存地址空间上，一旦被游戏访问，它们会以 16 KiB 的页占用物理内存空间。内存占用空间是 Apple 平台上决定游戏实际内存使用的主要且通用的指标。内存占用空间包含 dirty、compressed 和 swapped 的页。它包括 Apple silicon 上的 CPU 和 GPU 对象。它用于内存限制执行。你的游戏可以调用系统 API 来获取其占用空间和可用内存。现在你了解了幕后内存如何工作，让我们看看它在你的游戏中长什么样。我交给 Seth，由他继续。Seth Lù: 谢谢，Jack。现在，让我们开始捕获游戏的内存增长。我将继续使用 Modern Renderer 示例项目。当你从 Xcode 运行游戏时，Memory Gauge 会显示内存占用空间随时间的变化。然而，你可以在 Instruments 中剖析游戏，获得内存使用更详细的视图。因为游戏在启动时常常分配大量内存，你可能希望从新的游戏启动开始剖析，而不是附加到现有运行。从 Xcode，要快速开始剖析游戏，按住运行按钮，然后选择「Profile」。这会自动把你带到 Instruments。

Instruments App 包含一组剖析工具，记录系统的不同方面，并在时间线上可视化记录的数据。今年新增的 Game Memory 模板可以帮助你更好地理解 Metal 游戏中的内存增长。

这个模板包含 Allocations 和 Metal Resource Events instruments，用于记录带历史的内存分配；VM Tracker，用于记录内存占用空间；Virtual Memory Trace，用于记录虚拟内存活动；以及 Metal Application 和 GPU，用于记录 Metal 相关事件。

在本演示中，我将突出前三个 instruments：Allocations、Metal Resource Events 和 VM Tracker。但首先，让我们为游戏录制一个 trace。你可以按这里的录制按钮开始录制。稍后，要停止录制，可以按同一按钮，或直接退出游戏。当 Instruments 正在录制 Modern Renderer 时，让我展示另一种录制 trace 的方式。xctrace 命令允许你以编程方式执行录制，这在自动化工作流中可能有用。

另外，你可以指定设备名称，选择 iPhone、iPad 或 Apple TV 作为目标。

现在我已经捕获了一个 Instruments trace，让我们先看看 Allocations。Allocations instrument 为你提供内存分配的详细视图、它们的大小以及对象引用计数。然而，它不包括私有 Metal 资源。Statistics 视图显示所有堆分配和匿名 VM。

All Heap Allocations 包括 malloc'ed 缓冲区，可能包含对象；All Anonymous VM 包括可能为 dirty 的有趣 VM 区域。我们马上会看到，一些 Metal 资源属于这一类。

现在，让我们看看 All Heap Allocations 内部。通常，较大的分配对优化更有趣。要找到单个最大分配，可以点击 Size 表格列，按大小排序分配。

对于一个分配，你可以点击这个箭头，查看 Swift 和 Objective-C 对象的引用计数变化。

选中列表中的这个大分配后，检查器里有分配历史的栈回溯。点击按钮可以隐藏系统库或框架。根据栈回溯，分配发生在 Modern Renderer 加载资源时。

双击帧也可以带你到源代码。现在，让我们回到并看看「All Anonymous VM」类别内部。

在 Metal 游戏中，你可能会在 IOAccelerator 和 IOSurface 类别中发现大量分配。IOAccelerator 中的分配对应 Metal 资源。

从栈回溯中，你可以看到这个分配发生在加载资源时。

IOSurface 中的分配对应 drawables。这里，栈回溯显示 MetalKit view 请求了 drawable。

Allocations instrument 默认可视化分配大小。但它也提供替代视图。你可以在 Allocations 轨道的箭头按钮上自定义显示模式，可视化 Allocation Density。这会更新图示，显示随时间执行的分配数量并揭示内存分配的峰值。这些峰值可能是内存增长的来源。所以 Allocations 中显示的数据相当底层。要更好地理解分配的 Metal 资源，让我们继续 Metal Resource Events。Metal Resource Events instrument 围绕 Metal 资源设计。在 Resource Events 视图中，你可以找到 Metal 资源分配与释放的历史。这里，你也可以通过 Metal API 以编程方式指定的标签来识别 Metal 资源。与 Allocations instrument 类似，你可以在检查器中找到分配历史的栈回溯。

这个 instrument 还在 Metal 设备下添加了 Allocation 和 Deallocations 轨道。它们帮助可视化事件的密度。到目前为止，Allocations 和 Metal Resource Events 可以帮助理解内存分配。然而，分配并不总是转化为内存占用空间。所以让我们继续 VM Tracker 来调查实际内存使用。

VM Tracker instrument 显示非压缩 dirty 与 compressed 或 swapped 的内存。Dirty Size 代表非压缩 dirty 内存。Swapped Size 代表 compressed 或 swapped 内存。在这次录制中，Modern Renderer 没有 compressed 或 swapped 内存使用。详细的 Summary 视图显示 VM 区域。在「mapped file」区域，你可能会找到一些内存映射资源，如游戏资源。这里，Modern Renderer 把 bistro 资源文件映射到内存中。这就是 Instruments 中 Allocations、Metal Resource Events 和 VM Tracker 的简要概览。要快速回顾如何剖析内存增长：首先，选择 Game Memory 模板，然后录制并分析 trace。有时，在复现或验证内存增长模式时，你可能需要重复这个过程几次。我们希望新的 Game Memory 模板能帮助你更好地理解游戏中的内存分配或占用空间增长。请查看这些其他视频以了解更多关于使用 Instruments 的内容。现在，回到 Jack。

Game Memory 模板看起来真的很酷，它将非常有用，帮助理解内存使用随时间的变化。另外，你可能还希望捕获游戏在给定时刻的内存状态，以便更深入地挖掘该内存状态，并通过不同视角检查它。为此，我们有内存图和一套工具。

内存图是一个文件，高效存储游戏内存状态的完整快照，包括对象创建历史、引用以及任何压缩或交换。

你可以随时拍摄快照，比如当问题发生时，或成对拍摄——在问题发生前后——以便比较。为了增添趣味，让我们用烹饪类比来说明如何用内存图分析内存。它包括食材和准备两部分。

就食材而言，你需要：你的游戏；叫做 Malloc Stack Logging 的东西；以及一个捕获的内存图。配置 Malloc Stack Logging 和捕获内存图很快。

Malloc Stack Logging 在游戏进程中记录分配信息。你可以在 Scheme 设置中找到它。选择 Run action，进入 Diagnostics，勾选 Malloc Stack Logging 复选框。

如果你想知道这两个选项是什么：All Allocation and Free History 会跟踪所有对象，即使它们被释放后。日志数据可能占用更多内存，但对调试碎片化等问题很有用。另一方面，Live Allocation Only 会从其历史中丢弃已释放的对象，因此更轻量。在本例中，我只调查引用，它们位于 live 对象上，所以我可以选择这个选项。事实上，大多数时候 Live Allocation Only 都是推荐选项。

或者，如果不从 Xcode 启动，你可以设置环境变量。查看 malloc 手册页以了解一些额外的录制模式。之后，还要准备一个内存图。只需点击调试区域中的调试内存图按钮。Xcode 会拍摄内存快照、处理它，并进入内存调试器。Xcode Memory Debugger 为游戏的内存使用提供直观的视角。让我们花一分钟探索视图。左侧，Debug Navigator 提供对象实例的层级列表。

右侧，File Inspector 提供有用信息，如内存占用空间、运行时长和捕获日期。

中间区域是内存图视图，你有从左侧选中的对象，以及引用如何连接到这个对象。我稍后会回到这个图。

File 菜单提供保存此内存图以便将来分析的选项，或便于与团队分享。

对于 Mac 游戏，你也可以使用 leaks 命令行程序，通过进程 ID 或名称捕获内存图。这意味着你可以在安全 shell 中远程执行，因此光标停留在游戏中——以防你的游戏全屏运行且需要保持焦点。这就是开始内存图分析所需的准备。

现在是时候使用 Xcode Memory Debugger，加上 Terminal 中一些多功能命令行工具，来检查这个内存图，找出分配、占用空间，甚至更多。第一步是按类别分解内存使用。footprint 程序正好做这个。

footprint 使用内存图中的信息来重建这个高层摘要。通常，你首先关注较大的类别。对于像这个来自 Modern Rendering 示例代码的游戏内存图，IOAccelerator 通常最大。正如 Seth 所说，它包括 Metal 资源。这里，堆分配进入几个 MALLOC_（前缀）类别，因为系统把堆分配分组到大小池以提高性能。这些对象可能来自许多地方，如第三方插件或库，你的游戏在那里进行音效或物理模拟。

这里是来自一款精彩的 Apple Arcade 游戏 Manifold Garden 的内存图，由 William "Cheer" Studio 创建。我很高兴他们允许我展示游戏的内存使用。如果你的游戏使用游戏引擎，如 Manifold Garden 使用 Unity，或在内存映射之上使用自定义分配器，那部分内存会像这样显示为 untagged VM_ALLOCATE。这里有一个专业提示：在 Apple 平台上，你的游戏最多可以使用 16 个 App 专用标签，因此在深入内存使用时可以获得更清晰的视图。只需一行更改即可。

首先，从 16 个选项中制作标签。然后在调用「em map」时，用这个新标签替换 -1 作为「file descriptor」。查看「em map」的手册页，了解标签和类别如何定义。

如果你使用「mach VM allocate」，在分配时在 flag 参数中包含相同标志。

在 footprint 程序的世界里，dirty 大小还包含 swap 和 compressed，所以把它看作每个类别的总收费。

这就是当前内存使用的组成简要介绍，以及它如何构成占用空间。部分内存使用较少，变得 compressed 或 swapped。它们可能是内存节省的来源。下一步是找出游戏使用了多少 compressed 或 swapped 内存，并进行优化。

为此，你可以用 vmmap 运行内存图。它给你 dirty 和 swapped 大小，而不是合并的两个。这个 dirty 列包括当前未 swapped 或 compressed 的常规 dirty 内存，而 swapped 列包括 compressed 或 swapped 内存的原始大小。系统把这两列相加来确定占用空间。但因为 swapped 大小列中的内容不那么常用，它是寻找优化游戏内存目标的良好指标。哦，顺便说一下，这里是分配大小，对应 virtual size 列。resident size 包括 clean 页，如可执行文件和内存映射文件。

方便的是，vmmap 用单独的表格显示堆分配。在其输出底部，vmmap 按区域分组堆内存。这些区域反映游戏中的使用或生命周期。因为我打开了 MallocStackLogging，堆上的分配在工具的区域中。否则，它们会基于分配大小位于两个默认区域：MallocHelperZone 和 DefaultMallocZone。通常你可以跳过较小的系统实用区域，如 QuartzCore 区域。

另外，如果你怀疑碎片化，表现为高碎片大小或百分比，比如几十或几百兆字节，WWDC 2021 的 session 介绍更多碎片化问题。

运行 vmmap 不带 --summary，或以标准模式使用 vmmap，会按行显示这些类别内的每个 vm 区域。就像我们早前讨论的虚拟地址空间的样子。所以使用 vmmap，你可以从活跃使用的内存中提炼出使用较少的 dirty 内存。通常，游戏中还有相当多的各种大小的动态分配，或 malloc'd 堆内存使用。它们需要特别关注。

heap 工具按类分组 malloc'd 资源，并按实例计数排序。这些类在 C++ 中由 VTable、Objective-C 或 Swift 确定。

我们使用 --quiet 参数来跳过关于一些元数据的头部。今年新增，heap 在识别对象类型方面更智能。它使用 Malloc Stack Logging 记录的信息来呈现调用者或负责的库，因此巨大的 non-object 已成往事。

这是 Manifold Garden 的内存图再次出现。在这个例子中，首次揭示了插件如 FMOD Studio 和游戏组件如 GameAssembly.dylib 占用了多少堆使用。所以现在你可以更了解内存如何分布。它还暗示了获取这些对象更多信息的方向。在这个例子中，开发者可以打开 FMOD Studio 来微调游戏中的配乐和音效，或去 Unity 寻找游戏代码优化，等等。

有时按类总大小而非类实例计数排序更有帮助。在 Modern Rendering 示例项目的内存图中，顶部贡献者是一个使用超过 2.58 亿字节的类。要继续在 Modern Rendering 示例中查找更大的对象，使用 heap 按类总大小排序（--sortBySize），并列出所有对象（--showSizes），而不是每个类的摘要。有一个 NSConcreteMutableData 对象在 Bytes Storage 中大小为 2.55 亿字节：这看起来值得一看。接下来，我想找出它是什么。我先要它的地址。我添加 --address 并输入模式 NSConcreteMutableData，后跟通配符– dot star，以及括号中的大小过滤器，只列出 10 MB 及以上的大对象。这就是对象的地址。我将在后续步骤中使用它进行更深入的分析。这就是 heap 工具，改进了实例的对象识别。到目前为止，你已经看到三个工具来理解游戏中什么对象在使用内存，它们都提供不同视图。我展示的只是其中一种工作流。根据你的游戏中的特定内存模式或使用的技术，你可以以任何适合你需求的方式使用它们。

对于那些我们不确定其存在性的对象的发现，下一步是获取其来源，即其分配调用栈。

对于 Modern Rendering 中的 2 亿字节对象，我使用 --callTree 模式并传入其地址给 malloc_history。配合额外的 invert 参数，我可以聚焦于最接近分配的函数。瞧。这就是分配的回溯。类似地，Xcode Memory Debugger 也在检查器中显示对象的分配历史。只需选择一个对象，点击 Memory Inspector，它就在那里。作为另一个例子，传入 VM_ALLOCATE 作为类模式而非地址，来检查游戏或插件中的匿名 VM 使用，比如调试自定义分配器。无论使用 Xcode 还是 malloc_history，你都可以知道分配回溯，并决定是否深入，包括在该行设置断点，作为开始。

最后，调查对象引用也很有帮助。即使由于各种原因未启用 MallocStackLogging，内存图也始终记录对象引用。我们之前用 leaks 来在 Xcode 外捕获内存图。leaks 做得更多。它检查内存图中的所有引用，这就是为什么它知道 leaks 和 retain cycles。leaks 使用 trace tree 参数和来自 heap 的对象地址来获得对象的引用树。然而，因为这个例子中的树相当大，Terminal 之外有更好的查看方式。

在 Xcode 14 中，我们重新设计了内存图视图，以显示选中对象的入边和出边。

它甚至有一个新的 neighbor selection popover，来选择你希望 Xcode 绘制的边。这将极大地提高在复杂游戏状态中理解对象引用的生产力。

探索一会儿后，我相当确定 texture manager 是访问这个对象的东西。对于你的游戏，考虑使用 leaks 工具和内存图视图来找到重要的对象引用关系，了解这些对象在游戏中的访问方式。这就是如何使用 leaks 或 Xcode 查看并找到对象的重要引用。请查看 leaks 的手册页和 Xcode 帮助，了解更多这些工具的用法。

在这个内存图分析食谱中，每一步使用一些特定工具。它们共同完成对内存图的分析。

总结一下，第一件事是：当你期望用内存图捕获和分析内存时，启用 MallocStackLogging。然后为游戏用 Xcode 捕获内存图，或替代地对 Mac 游戏使用 leaks 工具。接下来，找到大而麻烦的对象。footprint、vmmap 和 heap 工具提供内存分解，既有高层也有细节。通过 malloc_history，你可以找出对象在哪里被分配；leaks 可以分析对象使用或引用。这些之前的 session 包含更深入的演练以及这些工具更多用法的演示。直到现在，我们推迟了探测 Metal 资源。嗯，现在是时候了。更多内容，交给 Seth。大家好！在游戏里，Metal 资源可能使用大量内存。但有方法优化它们的内存使用。

这里我总结了一个列表，列出优化游戏 Metal 资源内存时可以使用的内存节省方法。我们将看看 Metal Debugger 如何帮助你审计资源，并学习一些进一步减少游戏内存的高级技术。

Metal Debugger 是调试 Metal 游戏的一站式商店。拍摄 GPU frame capture 后，你可以找到一个 summary 页面。它为你提供关于捕获工作负载的一些通用统计。

页面下半部分，有一个分为四类的 insights 列表。「Memory」类别中的 insights 建议游戏的内存节省。这次 trace 没有太多特定内存 insights；在处理这些 insights 后，我们只能节省几 MB 内存。

然而，可能还有更多针对你游戏的内存节省。要获得 Metal 资源使用的内存的更完整画面，你可以点击 Show Memory 按钮使用 Memory Viewer。

Memory Viewer 为你提供从游戏中捕获的完整资源列表。上半部分显示不同类别用于过滤。你可以快速用它查找资源，比如纹理。下半部分，表格只显示纹理。现在让我们移除过滤器。资源表格有一组列来帮助你优化游戏。我想突出几列，可能帮助你快速识别一些有趣的资源。

Insights 列类似于我们刚在 summary 页面看到的。按此列排序表格时，你可以快速查看所有带 insights 的资源。点击 insight 图标会揭示一个 popover，解释发现并提供可能的操作。紧挨这列的是 Allocated Size。你可以按此列排序，查看最大的资源。审计某些资源是否真正善用其内存大小可能有用。例如，一些纹理可能被调整到更小分辨率，一些加载到缓冲区的模型可能使用更低的多边形计数，只要这样做不影响游戏的视觉质量。还有我马上会提到的一些替代方法来节省纹理内存。另一列有趣的是 Time Since Last Bound。你可以按此列排序资源，找到最近未使用的资源。如果资源从未被使用，可能值得仔细检查是否值得加载该资源。对于一段时间未被绑定的资源，如果你认为将来不会再使用，可以考虑释放它。或者，你可以将其 purgeable 状态设为 volatile。Metal 资源可以处于三种 purgeable 状态之一：non-volatile、volatile 和 empty。默认情况下，资源是 non-volatile。把 purgeable 状态设为 volatile，Metal 可能在系统内存压力高时从内存中驱逐该资源。一旦资源为空，系统就不再把它计入游戏的占用空间。当你的游戏再次需要该资源时，检查内容是否还在，必要时重新加载。考虑仅对不常使用的资源使用 volatile，以免 purgeable 状态对你不利。

这些是所有资源的一些通用说明。现在，让我们更仔细地看纹理。

Memory Viewer 中并非所有列默认显示。在表格头部右键，可以显示和隐藏列，如纹理的 Pixel Format。你可以通过优化纹理的 pixel format 获得不同数量的节省。游戏中的许多纹理可以使用 16 位半精度 pixel format 来减少内存使用和带宽。在需要单 alpha 分量纹理的情况下，你可以避免多个颜色通道。最后，一些只读纹理可能受益于块压缩以降低内存使用。对于块压缩 pixel format，有 ASTC 和 BC 等选项。另外，自 A15 Bionic 起，你可以对纹理和 render target 使用有损压缩，在尽可能保留质量的同时节省内存。请查看这些之前的视频了解更多详情。

这些是你使用 Memory Viewer 可以快速发现的一些内存节省。但还有几项额外技术，你可能采取以进一步优化游戏。如果纹理仅被单个 pass 使用，你可以把其 storage mode 设为 memoryless 以节省内存和带宽。Memoryless 纹理适用于临时 render target，如深度、模板或多采样纹理。否则，如果纹理仅被 GPU 使用，你可以把 storage mode 设为 private，否则 shared 或 managed。提醒一下，在 Apple silicon Mac 上，managed 模式并不需要，就像 iPhone 和 iPad 一样。这里是一个例子。游戏有一个 Depth32Float_Stencil8 纹理。深度纹理跨 pass 使用，但模板纹理的内容被丢弃，帧后面不会再使用。所以游戏可以用两个纹理，并把模板纹理设为 memoryless，以节省内存和带宽。

最后，我想提另一项技术，可能对你在游戏内存中物尽其用有趣。如果你的游戏不同时使用它们，你可以从 heap 使用别名资源。它们可以共享由同一分配支持的内存。但在同步对这些资源的访问时要格外小心。你可以查看「Go bindless with Metal 3」演讲，了解更多关于使用从 heap 分配的资源。这就是我们的内存节省清单。我希望这个清单能帮助你审计游戏中的 Metal 资源。

要了解更多关于使用 Metal Debugger 优化游戏内存，请查看这些其他 WWDC 演讲。交回给你，Jack。

谢谢你，Seth。今天，我们进行了一次引导式导览，探索了许多你可以用来理解和改进游戏内存使用的东西。首先，内存占用空间是理解游戏内存使用的主要指标，它包括 dirty 加上 compressed 和 swapped 内存。然后，我们体验了强大的内存调试工具。Seth 向我们展示了 Instruments 如何通过有用的遥测轨道赋能内存剖析。新的 Game Memory 模板正是为此任务量身定制。之后，我介绍了内存图，用于存储游戏内存状态的快照。有灵活而强大的命令行程序来分析内存图中的对象、引用和分配历史。heap 工具的改进和重新设计的 Xcode Memory Debugger 将加速游戏内存分析。最后，Seth 分享了 Metal 资源的内存节省清单，以及 Metal Debugger 如何帮助回答游戏中的 Metal 资源使用问题。你也可以从其他 WWDC session、文档和手册页了解更多。

我们不断为你推进最好、最灵活的工具。所以为什么不试试呢？它们可能正是你在寻找的。

别犹豫，通过 Feedback Assistant 等任何渠道与我们分享你的任何反馈。在你的内存之旅中玩得开心，谢谢观看。♪ ♪
