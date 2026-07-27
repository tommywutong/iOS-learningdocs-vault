---
title: 优化 GPU 性能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/optimizing-gpu-performance
source_url: 'https://developer.apple.com/documentation/xcode/optimizing-gpu-performance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/optimizing-gpu-performance.json'
content_hash: 'sha256:5a28112712e5793a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 优化 GPU 性能

<sub>文章</sub>

使用 Metal 调试器找到并解决性能瓶颈。

## 概述

Apple GPU 会尽可能并行运行顶点、片元和计算任务。Metal 调试器提供了检查存在重叠运行的通道的方法，你可以借此在受 GPU 限制的工作负载中找到造成瓶颈的任务。此外，性能分析器还会通过对你的着色器进行采样来测量性能统计数据，从而揭示热点所在。

如果你在运行 App 时注意到任何性能问题，可以使用 Metal 调试器来查找并调查瓶颈。首先，配置你的构建以包含着色器源代码（参阅[使用嵌入式着色器源代码构建你的项目](building-your-project-with-embedded-shader-sources.md)）。然后，当你注意到想要调试的视觉瑕疵时，对你的 App 进行一次帧捕获（参阅[在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md)）。

### 采集性能数据

当你启用 Profile after Replay 选项后，Metal 调试器会在回放工作负载之后自动开始采集性能数据。或者，你也可以点按 Summary 查看器上的 Profile 按钮来采集性能数据。

![](../../../attachments/7f8e55dc5d42f11bdbe1ec06c2bcccc4/gputools-metal-debugger-essentials-performance-gather-performance-data@2x.png)

<sub>展示 Metal 调试器 Summary 查看器的屏幕截图。图中高亮显示了 Profile 按钮和用于诱导 GPU 性能状态的按钮。</sub>

GPU 的性能状态在性能分析时很重要，因为它会影响系统执行工作负载的速度。影响性能状态的因素包括热量状况和系统设置。

默认情况下，Metal 调试器会以捕获时相同的 GPU 性能状态来对工作负载进行性能分析，因此其性能通常与你在设备上观察到的相似。不过，在 Metal 调试器中进行性能分析时，你可以点按调试栏中的 GPU Profiler 按钮，来诱导出特定的 GPU 性能状态。

有关 GPU 性能状态的更多信息，请参阅[探索 Metal 调试、性能分析和素材创建工具](https://developer.apple.com/videos/play/wwdc2021/10157/?time=476)。

![](../../../attachments/249c1791541c003bcfa85c9826060d89/gputools-metal-debugger-essentials-performance-profiler-button@2x.png)

<sub>Metal 调试器 Performance 时间线的屏幕截图，高亮显示了 GPU Profiler 弹出窗口，其中有两个菜单，分别对应 Performance State 和 GPU Execution Mode。这两个菜单分别显示 Medium 和 Concurrent。</sub>

你可以点按调试栏中的 GPU Profiler 按钮，在不同的 GPU 执行模式之间切换，包括 Concurrent 和 Serial。默认情况下，Metal 调试器会以 Concurrent 模式对工作负载进行性能分析。这样可以让 GPU 重叠执行顶点、片元和计算任务，以便尽快完成。在 Serial 模式下，Metal 调试器会强制每个通道只在上一个通道完成后才运行，这样每个通道在无重叠状态下的数据报告会更精确，但并不能代表运行时性能。

### 使用 Performance 时间线查找性能瓶颈

Metal 调试器中的 Performance 时间线可以帮助你在捕获的工作负载中找到开销较大的任务和性能瓶颈。点按 Debug 导航器中的 Performance 按钮，打开 Performance 时间线。

![Metal 调试器 Performance 时间线的屏幕截图，显示了 Vertex、Fragment、Compute 和 Counters 轨道。](../../../attachments/4749aeae32b4700f7c85608bf13790ad/gputools-metal-debugger-essentials-performance-gpu-timeline@2x.png)

窗口左侧的 Timeline 导航器列出了所有经过性能分析的通道、管线状态和 GPU 命令，以及它们的着色器性能分析器开销。

顶部区域是 Vertex、Fragment 和 Compute 这三条 GPU 轨道，它们显示了各个通道以重叠方式运行时的起始时间和持续时间。GPU 轨道下方是汇总各个着色器的聚合着色器轨道。展开聚合着色器轨道后，你可以以瀑布式的方式查看各个着色器的时间线。

底部区域有一条独立的 Counters 时间线，其中包含 Occupancy、Limiter 和 Bandwidth 等 GPU 计数器。这些计数器可以帮助你诊断性能瓶颈。你可以通过在不同的计数器标签页之间切换，来聚焦于某个计数器子集。有关更多信息，请参阅[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)。

### 获取通道和绘制调用的详细性能指标

你可以在 GPU 追踪中查看你 App 各个通道或命令的性能计数器统计数据。点按 Performance 时间线上方的 Counters 标签页，打开 Performance counters。

![Metal 调试器 Performance counters 的屏幕截图，列出了所有编码器及其计数器。](../../../attachments/bdb06bf0fe824b56c609b2d7b532e46c/gputools-metal-debugger-essentials-performance-counters-table@2x.png)

Metal 调试器通过在以重叠方式运行工作负载时追踪着色器指令，来推导出着色器性能分析器时间。在受着色器限制的工作负载中，按着色器性能分析器时间对表格排序，可以帮你找到总体开销最大的通道或绘制调用。此外，Metal 调试器还会单独测量每个通道或命令的详细计数器。你也可以在顶部栏中选择不同的计数器集合，以获得更聚焦的视图。有关更多信息，请参阅[使用计数器统计数据分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-counter-statistics.md)。

### 在 Debug 导航器中按管线状态对命令分组

要以不同的视角查看 Metal 命令，请点按 Debug 导航器中的 Outline 弹出菜单，并选择 Group by Pipeline State，以查看管线状态列表。

![](../../../attachments/2a8b3c201556151b6cd66de6fbd90c05/gputools-metal-debugger-essentials-performance-debug-navigator-pso@2x.png)

<sub>Xcode 中 Debug 导航器的屏幕截图，展示了捕获的工作负载中所有管线状态，按开销从高到低排序。</sub>

有了性能分析数据后，Debug 导航器会显示以重叠方式运行工作负载时，来自各个管线状态着色器的采样百分比。在受着色器限制的工作负载中，这份按管线状态排序的列表有助于识别开销最大的管线状态。展开某个管线状态，即可找到使用该状态的命令列表。

你还可以通过从列表中选择某个管线状态下的着色器，快速查看着色器源代码和逐行性能分析统计数据。

有关 Debug 导航器的更多信息，请参阅[分析你的 Metal 工作负载](analyzing-your-metal-workload.md)。

### 使用逐行着色器性能分析统计数据优化着色器

打开某个着色器后，你可以找到该着色器在管线状态中的时间细分。

![](../../../attachments/e08be55f5ba1584bcd41d73e1431f5c8/gputools-metal-debugger-essentials-performance-shader-profiler@2x.png)

<sub>Xcode 中 Shader 编辑器的屏幕截图，显示了 Debug 导航器中的调用树，以及源代码旁边的逐行着色器性能分析数据。</sub>

左侧边栏让你能够检查着色器源文件和性能分析调用树。借助调用树，你可以根据每一帧的权重找到性能热点。

在着色器源代码的装订线中，你可以在代码行旁边找到权重值。每个权重值右侧的饼图包含性能统计数据，帮助你改进着色器代码。

例如，当你发现某一行开销较大的代码在内存采样方面占比很高时，这可能是因为读取纹理数据耗费了时间。要缩短着色器耗时，如果计算某个值比从纹理中读取它开销更低，你可以修改代码，在着色器中直接计算该值。

对着色器源代码进行修改后，点按调试栏中的 Reload Shaders 按钮，以刷新性能分析统计数据。你可以通过观察 Performance 时间线中新的 GPU 总时间和各条轨道，来验证这些修改是否有助于提升整体性能。

> [!important] 重要
> 对着色器源代码的修改只存在于 Metal 调试器内部。你原始的着色器源代码不会发生变化。请确保将你的修改复制回原始的着色器源代码中。

有关如何解读逐行着色器性能分析统计数据的更多信息，请参阅[检查着色器](inspecting-shaders.md)。

### 使用着色器开销图检查着色器性能

> [!important] 重要
> 着色器开销图功能适用于搭载 A17 Pro 或更新芯片的 iOS 设备，以及搭载 M3 或更新芯片的 Mac 电脑。

你可以使用着色器开销图，快速查找并分类开销较大的管线状态和着色器。在 Timeline 导航器中选择某个管线状态，然后点按 Shaders 标签页。

![Metal 调试器着色器开销图的屏幕截图。](../../../attachments/44d89222dbe4d7c63b48c979985b4d67/gputools-metal-debugger-shader-cost-graph-overview@2x.png)

你可以借助顶部区域的火焰图，检查着色器函数调用的开销百分比，并选择函数调用以直接跳转到源代码。

有关更多信息，请参阅[使用着色器开销图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md)。

### 使用性能热力图了解 SIMD 组执行情况

> [!important] 重要
> 性能热力图功能适用于搭载 A17 Pro 或更新芯片的 iOS 设备，以及搭载 M3 或更新芯片的 Mac 电脑。

你可以使用性能热力图，快速查找并检查着色器源代码的执行情况。在 Timeline 导航器中选择某个编码器、管线状态或 GPU 命令，然后点按 Heat Maps 标签页。

![Metal 调试器性能热力图的屏幕截图。](../../../attachments/83ba0059fb79ce77761701f6f266e3d2/gputools-metal-debugger-heatmap-overview@2x.png)

顶部区域显示了各种热力图，以图形方式呈现有关 GPU 线程的统计信息，例如开销、分歧程度和指令数量。

底部区域在时间线上显示了 GPU 线程的着色器执行历史，包括函数调用栈和线程状态。

有关更多信息，请参阅[使用性能热力图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md)。

### 将性能数据保存到你的开发系统中

你可以通过选择 File \> Export，并在对话框中选中 Embed performance data 复选框，将你 App 的 Metal 工作负载性能数据保存为 GPU 追踪文件，以供日后分析。这样你就可以只查看性能数据，而不必在设备上回放 GPU 追踪。

![](../../../attachments/6aa2aeea7c3374e61a958e54a4ced338/gputools-metal-debugger-essentials-embed-performance-data@2x.png)

<sub>Xcode 中 Metal 调试器针对性能数据追踪文件的保存对话框的屏幕截图。对话框的 Export as 字段中填写了名称 Deferred Lighting，并有一个已被用户选中的复选框，标签为 Embed performance data。</sub>

你可以在任意一台 Mac 上打开 GPU 追踪文件——而不仅限于你的开发系统——因为回放该追踪文件并不需要兼容的设备。你也可以选择通过选定一台兼容的设备来回放该 GPU 追踪文件。

有关更多信息，请参阅[回放 GPU 追踪文件](replaying-a-gpu-trace-file.md)。

## 另请参阅

### 基础

- [在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md) — 通过配置你的项目使用 Metal 调试器，来分析你 App 的性能。
- [以编程方式捕获 Metal 工作负载](capturing-a-metal-workload-programmatically.md) — 通过调用 Metal 的帧捕获功能，来分析你 App 的性能。
- [回放 GPU 追踪文件](replaying-a-gpu-trace-file.md) — 在 Metal 调试器中使用 GPU 追踪文件，调试并分析你 App 的性能。
- [调查视觉瑕疵](investigating-visual-artifacts.md) — 使用 Metal 调试器发现、诊断并修复你 App 中的视觉瑕疵。
- [使用交互式命令行工具进行调试](debugging-with-interactive-command-line-tools.md) — 无需离开终端，即可调查 GPU 追踪文件中的渲染问题。
- [使用 AI 智能体调查 GPU 问题](investigating-gpu-issues-with-ai-agents.md) — 将大型 GPU 追踪文件交给 AI 智能体进行自主调查，以找出问题的根本原因。
