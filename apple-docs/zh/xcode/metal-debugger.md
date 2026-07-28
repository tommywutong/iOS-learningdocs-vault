---
title: Metal 调试器
framework: updates
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/metal-debugger
source_url: 'https://developer.apple.com/documentation/xcode/metal-debugger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/metal-debugger.json'
content_hash: 'sha256:b613249a5f58f9f2'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md)

# Metal 调试器

通过 GPU 追踪来调试和分析你的 Metal 工作负载。

## 概述

Metal 调试器包含一套用于调试和分析你的 Metal App 的工具。

与在运行时于断点暂停不同，你可以跨多个帧捕获你的 Metal 工作负载，然后在时间轴上前后跳转，探索捕获下来的工作。Metal 调试器让你能够探索各个渲染通道（Pass）之间的依赖关系，并为优化你的 App 的性能提供见解。你还可以在绘制命令和计算分派中调试你的着色器，从而修复产生视觉瑕疵的根源（请参阅[调查视觉瑕疵](investigating-visual-artifacts.md)）。

此外，Metal 调试器会在分析时间线上显示你的 Metal 工作负载，并提供详细的统计数据，例如性能计数器和逐行着色器分析数据。这些工具可以帮助你识别并消除你的 App 中的性能瓶颈（请参阅[优化 GPU 性能](optimizing-gpu-performance.md)）。

如需从命令行调查 GPU 追踪，请使用 `gpudebug`，一个基于终端的交互式调试器。由于其界面基于文本且支持自我发现，AI 智能体可以自主运行它来浏览追踪、检查状态以及获取资源，从而无需人工介入即可诊断渲染问题。更多信息，请参阅[使用 AI 智能体调查 GPU 问题](investigating-gpu-issues-with-ai-agents.md)。

![Metal 调试器的屏幕截图，显示了某个绘制命令的已绑定资源和附件。](../../../attachments/a7cba2f6c40a790c84564b5ed827fa13/gputools-metal-debugger-hero@2x.png)

有关 Metal 调试器的更多信息，请参阅以下视频讲座：

- [Metal 着色器调试与性能分析](https://developer.apple.com/videos/play/wwdc2018/608/)
- [借助 Xcode 12 深入洞察你的 Metal App](https://developer.apple.com/videos/play/wwdc2020/10605/)
- [使用 GPU 计数器优化 Metal App 和游戏](https://developer.apple.com/videos/play/wwdc2020/10603/)
- [探索 Metal 调试、性能分析和资源创建工具](https://developer.apple.com/videos/play/wwdc2021/10157/)
- [分析并优化你的游戏内存](https://developer.apple.com/videos/play/wwdc2022/10106/)

## 主题

### 基础

- [在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md) — 通过配置项目以使用 Metal 调试器来分析你的 App 的性能。
- [以编程方式捕获 Metal 工作负载](capturing-a-metal-workload-programmatically.md) — 通过调用 Metal 的帧捕获来分析你的 App 的性能。
- [重放 GPU 追踪文件](replaying-a-gpu-trace-file.md) — 使用 Metal 调试器中的 GPU 追踪文件来调试和分析你的 App 的性能。
- [调查视觉瑕疵](investigating-visual-artifacts.md) — 使用 Metal 调试器发现、诊断并修复你的 App 中的视觉瑕疵。
- [优化 GPU 性能](optimizing-gpu-performance.md) — 使用 Metal 调试器查找并解决性能瓶颈。
- [使用交互式命令行工具进行调试](debugging-with-interactive-command-line-tools.md) — 无需离开终端即可调查 GPU 追踪中的渲染问题。
- [使用 AI 智能体调查 GPU 问题](investigating-gpu-issues-with-ai-agents.md) — 通过将追踪交给 AI 智能体进行自主调查，找到大型 GPU 追踪中问题的根本原因。

### Metal 工作负载分析

- [分析你的 Metal 工作负载](analyzing-your-metal-workload.md) — 使用 Metal 调试器调查你的 App 的工作负载、依赖关系、性能和内存影响。
- [分析资源依赖关系](analyzing-resource-dependencies.md) — 通过理解资源之间的关系，避免你的 Metal App 中出现不必要的工作。
- [分析内存使用情况](analyzing-memory-usage.md) — 通过检查你的 Metal App 的资源来管理其内存使用。
- [使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md) — 使用性能时间线定位性能问题。
- [使用计数器统计信息分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-counter-statistics.md) — 通过检查各个通道和命令的计数器来优化性能。
- [使用性能热力图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md) — 通过检查源代码执行情况来深入了解 SIMD 组的性能。
- [使用着色器成本图分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md) — 通过检查管线状态（pipeline states）来发现潜在的着色器性能问题。
- [使用计数器统计信息分析非 Apple GPU 性能](analyzing-non-apple-gpu-performance-using-counter-statistics.md) — 通过检查各个通道和命令的计数器来优化性能。

### Metal 资源检查

- [检查加速结构](inspecting-acceleration-structures.md) — 通过检查你的加速结构来揭示光线相交瓶颈。
- [检查缓冲区](inspecting-buffers.md) — 通过检查缓冲区的内容来确认缓冲区格式。
- [检查管线状态](inspecting-pipeline-states.md) — 通过检查渲染和计算通道的属性来确定它们的行为方式。
- [检查采样器状态](inspecting-sampler-states.md) — 通过检查采样器状态配置的属性来验证它们。
- [检查着色器](inspecting-shaders.md) — 通过检查和编辑着色器来提升你的 App 的着色器性能。
- [检查纹理](inspecting-textures.md) — 通过检查纹理的内容来发现问题。

### Metal 命令分析

- [检查命令的已绑定资源](inspecting-the-bound-resources-for-a-command.md) — 通过检查编码器中任意点的已绑定资源来发现问题。
- [检查绘制命令的几何体](inspecting-the-geometry-of-a-draw-command.md) — 通过检查当前几何体来查找你的 App 的顶点、对象或网格函数中的问题。
- [检查绘制命令的附件](inspecting-the-attachments-of-a-draw-command.md) — 通过检查单个像素和样本来发现附件问题。
- [调试绘制命令或计算分派中的着色器](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) — 使用着色器调试器识别并修复你的 App 中有问题的着色器。
- [使用 GPU 计数器分析绘制命令和计算分派的性能](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) — 通过检查性能计数器来识别帧捕获中的问题。
- [使用管线统计数据分析绘制命令和计算分派的性能](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) — 通过检查管线统计数据来识别帧捕获中的问题。

## 另请参阅

### 图形

- [Metal 开发者工作流程](metal-developer-workflows.md) — 定位并修复与你的 App 使用 Metal API 和 GPU 函数相关的问题。
