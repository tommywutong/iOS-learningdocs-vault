---
title: 分析资源依赖关系
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-resource-dependencies
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-resource-dependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-resource-dependencies.json'
content_hash: 'sha256:ac49d7c2cb229ab3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 分析资源依赖关系

<sub>文章</sub>

通过了解资源之间的关系，避免在你的 Metal App 中产生不必要的工作。

## 概述

Dependencies 查看器以图形方式呈现你 GPU 跟踪记录的结构，让你能够查看资源与访问这些资源的编码器之间的关系。它还会突出显示你在各编码器之间使用的手动同步操作，并通过展示你这一帧中所有未使用的资源，指出任何不必要的工作。

![Dependencies 查看器的一张截图，其中包括依赖关系图视图、侧边栏和控制栏。](../../../attachments/9792256b993e2819ad485ff530e40b9d/gputools-metal-debugger-dv-overview@2x.png)

### 以不同的详细程度检视关系图

在最高层级，Dependencies 查看器展示你这一帧的整体结构。在这个层级，你可以看到命令缓冲区内命令编码器的关系图。你还可以看到这一帧中的所有 pass。每个 pass 都包含其工作内容的缩略预览，以及它所消耗或产生的资源数量。在这个层级，你可以看到数据是否在流动，以及各 pass 之间是否存在同步。

![Metal 调试器 Dependencies 查看器的一张截图，以较低的详细程度展示了依赖关系图。](../../../attachments/4764d72159e10ae6fbcf431ce96ac97d/gputools-metal-debugger-dv-lod-low@2x.png)

当你放大到下一个层级时，Dependencies 查看器会展开每个 pass 的资源。此外，每个资源上方和下方都可能带有图标，用以表示消耗和产生动作。对于渲染 pass 中的附件，这些图标指的是加载和存储动作；否则，它们指的是一般的资源读写操作。在这个层级，你还可以查看哪些资源在各 pass 之间引入了数据流动或同步。

![Metal 调试器 Dependencies 查看器的一张截图，以中等的详细程度展示了依赖关系图。](../../../attachments/48408c4be87ba4cc4eee729d4a9b6e9d/gputools-metal-debugger-dv-lod-mid@2x.png)

当你进一步放大时，Dependencies 查看器会显示更大的资源缩略图和元数据。

![Metal 调试器 Dependencies 查看器的一张截图，以较高的详细程度展示了依赖关系图。](../../../attachments/49049b73095e136bdd9de6722645206a/gputools-metal-debugger-dv-lod-high@2x.png)

### 查看某个资源的消耗和产生动作

某个资源上方和下方的消耗与产生动作，能帮助你快速了解给定 pass 中的资源访问情况。

对于渲染 pass 中的纹理，这些动作指的是每个附件的加载和存储动作。

对于多重采样渲染 pass，存储动作可能同时影响多重采样纹理和解析纹理的存储方式。使用 [MTLStoreAction.storeAndMultisampleResolve](../metal/mtlstoreaction/storeandmultisampleresolve.md) 时，多重采样纹理会显示一个存储动作，解析纹理也会显示一个存储动作。使用 [MTLStoreAction.multisampleResolve](../metal/mtlstoreaction/multisampleresolve.md) 时，多重采样纹理会显示一个「不关心」动作，解析纹理则显示一个存储动作。

除此之外，Dependencies 查看器会用通用的读写操作来标注这些动作。

### 分析数据流动与同步依赖关系

Dependencies 查看器会显示 pass 之间的两类依赖关系：

- 实线表示数据流动。前一个 pass 产生数据，后一个 pass 消耗该数据。
- 虚线表示同步。两个 pass 之间没有数据流动，但存在某种关系。

例如，某个计算 pass 读取前一个渲染编码器所写入的纹理，这两个 pass 之间就存在数据流动。

此外，某个在加载时清除附件的渲染 pass，与之前修改过该纹理的任何 pass 之间都没有数据依赖关系。然而，该渲染 pass 仍需等待之前的 pass 完成对该纹理的修改——这就是一种同步关系。

### 选择关系查看模式

你可以使用 Dependencies 查看器选择不同的可视化模式，每种模式展示不同的边的子集：

- All：显示来自同步原语、以及已跟踪和未跟踪资源的所有边。
- Synchronzation：显示来自同步原语和已跟踪资源的虚线同步边。
- Data Flow：显示来自已跟踪或未跟踪资源的实线数据流边。

### 从资源堆中固定资源

为保持关系图的紧凑，Dependencies 查看器会尝试只在图中显示少数几个值得关注的资源，其余的则隐藏在每个 pass 下方的一堆资源中。点按该资源堆即可打开一个资源弹出窗口。

![Dependencies 查看器中某个 pass 的 Resources 弹出窗口截图。](../../../attachments/40b0ab325d2c90ada3a97cc0734c37b1/gputools-metal-debugger-dv-popover@2x.png)

你可以点按每个资源右侧的按钮来固定或取消固定它。

### 获取有关某个 pass 的更多信息

在 Dependencies 查看器中点按任意 pass 即可选中它，并在侧边栏中显示有关该 pass 的附加信息。你还可以确定该 pass 消耗或产生了哪些资源：

- 对于该 pass 所消耗的资源，Dependencies 查看器会提示最近一次修改该资源的 pass。
- 对于该 pass 所产生的资源，Dependencies 查看器会提示之后会消耗该资源中数据的那些 pass。

### 获取有关某个资源的更多信息

在 Dependencies 查看器中点按任意资源即可选中它，并在侧边栏中显示有关该资源的附加信息。你还可以查看最近产生该资源数据、或之后将消耗该资源数据的那些 pass。

当你选中某个资源时，Dependencies 查看器会高亮显示与之相关的资源。例如，当你选中某个纹理视图时，它会高亮显示其父纹理；当你选中某个堆时，它会高亮显示来自该堆的资源。

### 使用 Insights 改进你的 Metal 工作负载

点按右下角的 Insights 按钮，即可打开 Dependencies 查看器中的建议弹出窗口。

![Dependencies 查看器中 Insights 弹出窗口的一张截图。](../../../attachments/a1153313baa692a1e418b19fa7234605/gputools-metal-debugger-dv-insights@2x.png)

### 使用过滤器限定范围

使用 Dependencies 查看器底部的过滤器字段调整关系图的过滤条件。在该字段中输入过滤词，Dependencies 查看器就会显示与过滤词匹配的相关 pass。此外，在按资源过滤时，你还可以找到消耗或产生该资源的各个 pass。

### 搜索特定元素

选择「Find」\> 「Find」，即可在 Dependencies 查看器上方显示搜索栏。你可以在搜索栏的文本字段中输入搜索词，以查找匹配的 pass 和资源。

对于任意搜索词，你都可以点按它，并选择包含或排除与该词匹配的元素。

文本字段右侧的两个箭头按钮，可让你在 Dependencies 查看器中移动到上一个或下一个匹配的元素。

## 另请参阅

### Metal 工作负载分析

- [分析你的 Metal 工作负载](analyzing-your-metal-workload.md) — 使用 Metal 调试器调查你 App 的工作负载、依赖关系、性能和内存影响。
- [分析内存使用情况](analyzing-memory-usage.md) — 通过检查资源来管理你 Metal App 的内存使用情况。
- [使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md) — 使用 Performance 时间线定位性能问题。
- [使用计数器统计信息分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-counter-statistics.md) — 通过检查各个 pass 和命令的计数器来优化性能。
- [使用性能热力图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md) — 通过检查源代码执行情况，深入了解 SIMD 组的性能。
- [使用着色器开销图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md) — 通过检查流水线状态，发现潜在的着色器性能问题。
- [使用计数器统计信息分析非 Apple GPU 性能](analyzing-non-apple-gpu-performance-using-counter-statistics.md) — 通过检查各个 pass 和命令的计数器来优化性能。
