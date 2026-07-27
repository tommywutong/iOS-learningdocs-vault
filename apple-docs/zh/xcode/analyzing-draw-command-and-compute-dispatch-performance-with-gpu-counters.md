---
title: 使用 GPU 计数器分析绘制命令和计算调度性能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.json'
content_hash: 'sha256:4242d32fc2a25403'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 使用 GPU 计数器分析绘制命令和计算调度性能

<sub>文章</sub>

通过检查性能计数器来识别帧捕获中的问题。

## 概述

Performance Statistics 查看器会显示计数器，帮助你理解系统为热点和瓶颈自动生成的洞察，从而提升 GPU 性能。GPU 性能计数器是细粒度统计信息，与 App 在捕获帧中执行的特定渲染、计算或位块传输工作相关。

![Performance Statistics 查看器的截图，其中以表格形式显示 GPU 计数器。](../../../attachments/4a21de0331a63c45e37a896ccf281ac6/gputools-metal-debugger-pv-overview@2x.png)

### 显示性能计数器列

按住 Control 键点按列标题，可以显示或隐藏中位数、最大值和总值的计数器值列。你可以查看以下各列：

- **Draw** — 命令的统计信息。对于 Vertex Stage Time 等百分比，它衡量顶点阶段在该次绘制中所使用的样本百分比。
- **Encoder** — pass 的统计信息。对于 Vertex Stage Time 等百分比，它衡量顶点阶段在渲染 pass 的所有绘制中所使用的样本百分比。
- **Median** — GPU 跟踪中所有 pass 的计数器值中位数。
- **Max** — GPU 跟踪中所有 pass 的计数器最大值。
- **Total** — GPU 跟踪中所有 pass 的计数器值总和。

### 检查计数器数据中的异常

将指针移到计数器上以显示其说明。

![指针悬停在表格行上时显示计数器工具提示的截图。](../../../attachments/4c14715a3898060fa86acf3162d51422/gputools-metal-debugger-pv-tooltip@2x.png)

通过分析可能成为热点的值，计数器可以提示 App 性能问题的具体原因。例如，如果顶点数量是预期值的两倍，代码中可能存在重复的网格或渲染编码器绘制调用。

### 使用过滤条件限定范围

在表格底部的过滤栏中输入过滤词，以调整过滤条件。表格会显示名称与这些过滤词匹配的单个计数器和计数器组。

存在两个或更多过滤词时，可以点按过滤按钮，选择匹配任意一个还是全部过滤词。对于任意过滤词，可以点按它来选择包含或排除与该词匹配的计数器。

## 另请参阅

### Metal 命令分析

- [检查命令的绑定资源](inspecting-the-bound-resources-for-a-command.md) — 通过检查编码器中任意位置的绑定资源来发现问题。
- [检查绘制命令的几何体](inspecting-the-geometry-of-a-draw-command.md) — 通过检查当前几何体，找出 App 的顶点函数、对象函数或网格函数中的问题。
- [检查绘制命令的附件](inspecting-the-attachments-of-a-draw-command.md) — 通过检查单个像素和样本来发现附件问题。
- [调试绘制命令或计算调度中的着色器](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) — 使用着色器调试器识别并修复 App 中有问题的着色器。
- [使用管线统计信息分析绘制命令和计算调度性能](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) — 通过检查管线统计信息来识别帧捕获中的问题。
