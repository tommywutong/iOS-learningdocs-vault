---
title: 使用计数器统计数据分析非 Apple GPU 性能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-non-apple-gpu-performance-using-counter-statistics
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-non-apple-gpu-performance-using-counter-statistics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-non-apple-gpu-performance-using-counter-statistics.json'
content_hash: 'sha256:13b1ac38d84ec9ea'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 使用计数器统计数据分析非 Apple GPU 性能

<sub>文章</sub>

通过检查各个通道和命令的计数器来优化性能。

## 概述

> [!important] 重要
> Counters 查看器功能不适用于 Apple GPU。对于 Apple GPU，请参阅[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)和[使用计数器统计数据分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-counter-statistics.md)。

Counters 查看器会显示 GPU 追踪中 App 各个通道或命令的性能计数器。这些计数器测量 GPU 上与硬件有关的活动，范围涵盖内存带宽、顶点数量、光栅化片元数量，以及纹理筛选 limiter 和 utilization 百分比。

![Counters 查看器的屏幕截图，其中包含计数器时间线以及通道或命令的表格。](../../../attachments/080dc9cc88071641b45ac6b4fa49df86/gputools-metal-debugger-cg-overview@2x.png)

Metal 调试器会从无重叠运行的通道中收集数据，因此性能分析器测量性能时，设备上每次只运行一个通道。此外，它还包含不随时间变化的确定性计数器，例如渲染通道中的顶点数量。

### 查看通道或命令的不同计数器集合

在图表顶部，你可以点按 Encoder 或 Draw 标签页，选择按通道或命令粒度查看计数器。然后，可以选择要用于查看计数器集合的计数器组。

### 查找着色器 GPU 时间较高的通道

每个通道的橙色条高度表示其着色器 GPU 时间。最高的条对应完成耗时最长的通道。尽量缩短长时间运行通道的持续时间，以优化 App 性能。

![每个通道计数器时间线的屏幕截图，其中选择了着色器 GPU 时间最长的通道。](../../../attachments/f871c426a724014f50044dde3874e846/gputools-metal-debugger-cg-gpu-time@2x.png)

上面的屏幕截图中有三个渲染通道，其中 GBuffer Generation 通道的着色器 GPU 时间条最高。你可以将指针移到条上方查看时间和其他信息。在上面的屏幕截图中，GBuffer Generation 通道的着色器 GPU 时间为 657.69 微秒（μs）。

### 在辅助编辑器中查看性能计数器

辅助编辑器让你能够查看各个通道和命令的其他信息。点按 Adjust Editor Options 按钮并选择 Assistant 选项，即可启用辅助编辑器。

![Adjust Editor Options 菜单的屏幕截图，其中高亮显示 Assistant 菜单项。](../../../attachments/911dcbdabb78263180376f773de3943f/gputools-metal-debugger-cg-menu-enable-assistant-editor@2x.png)

选择通道或命令后，辅助编辑器会显示其性能计数器。如果看到的不是性能计数器，可以从编辑器左上角的下拉式菜单中选择 Performance。

![辅助编辑器下拉式菜单的屏幕截图，其中高亮显示 Performance 菜单项。](../../../attachments/5c40e29da58eb1abde53d13d6a0966d1/gputools-metal-debugger-ct-assistant-menu-performance@2x.png)

辅助编辑器中的性能计数器让你能够检查特定通道或命令的所有计数器。通过分析可能成为热点的值，计数器可以提示 App 性能问题的具体原因。例如，如果顶点数量是预期值的两倍，很可能是代码中存在重复网格或重复的渲染编码器绘制调用。

![Metal 调试器的屏幕截图，并排显示 Counters 查看器和 Performance Statistics 查看器。](../../../attachments/a5e835e74f9444d6f12808b75d075141/gputools-metal-debugger-cg-performance@2x.png)

有关更多信息，请参阅[使用 GPU 计数器分析绘制命令和计算调度性能](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md)。

### 查看命令的管线统计数据

选择命令后，你可以在辅助编辑器中查看其管线统计数据。你可以从 Assistant Editor 下拉式菜单中选择 Pipeline Statistics，以查看有关管线状态及其性能统计数据的信息。

![辅助编辑器下拉式菜单的屏幕截图，其中高亮显示 Pipeline Statistics 菜单项。](../../../attachments/d41466b27f19c9e62f834757a388492b/gputools-metal-debugger-ct-assistant-menu-pipeline-statistics@2x.png)

辅助编辑器中的管线统计数据让你能够查看编译器统计数据和运行时性能分析统计数据。辅助编辑器区域顶部以不同类别列出每个管线阶段的完成耗时。下方则列出使用相同管线阶段的命令及其着色器 GPU 时间。

![Metal 调试器的屏幕截图，并排显示 Counters 查看器和 Pipeline Statistics 查看器。](../../../attachments/6a9052cfd46b81ec845e0795c1631239/gputools-metal-debugger-cg-pipeline-statistics@2x.png)

有关更多信息，请参阅[使用管线统计数据分析绘制命令和计算调度性能](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md)。

有时，计数器数据可能只能提示问题所在，此时利用其他 Metal 工具会有所帮助。例如，如果片元着色器时间异常高，可以使用 Shader 编辑器来发现片元着色器中哪些具体代码行拖慢了执行速度。有关更多信息，请参阅[检查着色器](inspecting-shaders.md)。

## 另请参阅

### Metal 工作负载分析

- [分析 Metal 工作负载](analyzing-your-metal-workload.md) — 使用 Metal 调试器调查 App 的工作负载、依赖项、性能和内存影响。
- [分析资源依赖项](analyzing-resource-dependencies.md) — 通过了解资源之间的关系，避免 Metal App 中不必要的工作。
- [分析内存使用情况](analyzing-memory-usage.md) — 通过检查资源来管理 Metal App 的内存使用情况。
- [使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md) — 使用 Performance 时间线定位性能问题。
- [使用计数器统计数据分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-counter-statistics.md) — 通过检查各个通道和命令的计数器来优化性能。
- [使用性能热力图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md) — 通过检查源代码执行情况，深入了解 SIMD 组性能。
- [使用着色器开销图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md) — 通过检查管线状态，发现潜在的着色器性能问题。
