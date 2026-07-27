---
title: 使用管线统计信息分析绘制命令和计算调度性能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.json'
content_hash: 'sha256:82502b41c7d8d1a4'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 使用管线统计信息分析绘制命令和计算调度性能

<sub>文章</sub>

通过检查管线统计信息来识别帧捕获中的问题。

## 概述

Pipeline Statistics 查看器会显示管线状态中的每个着色器阶段、该阶段完成所用的时间，以及在此期间执行的 GPU 活动。

![](../../../attachments/d42b35a393e4f0397e85ee14ad025126/gputools-metal-debugger-psv-overview@2x.png)

<sub>Pipeline Statistics 查看器的截图，其中显示每个着色器的统计信息，以及使用该管线状态的各命令之间的时序对比。</sub>

### 解读 GPU 活动

各种 GPU 活动会以条形图形式显示编译器统计信息和运行时分析统计信息。

![](../../../attachments/aa185426f0e7bd6cce4350582f5296d5/gputools-metal-debugger-psv-pipeline-statistics@2x.png)

<sub>着色器统计信息的截图。上半部分按操作显示时序，下半部分按操作显示指令数量。</sub>

| GPU 活动 | 说明和建议 |
|---|---|
| ALU | GPU 在算术逻辑单元中花费的时间。在可行时将 float 改为 half-float，以减少 ALU 中的耗时。此外，请尽量减少使用 `sqrt`、`sin`、`cos` 和 `recip` 等复杂指令。 |
| Memory | GPU 等待访问 App 缓冲区或纹理内存所花费的时间。可以通过对纹理进行降采样来缩短耗时；如果内存耗时并不多，则可以改为提高纹理分辨率。 |
| Control flow | 由于着色器中的分支或循环，GPU 在条件、递增或跳转指令中花费的时间。对循环使用恒定迭代次数来尽量缩短控制流耗时，因为 Metal 编译器在这种情况下可以生成优化后的代码。 |
| Synchronization | GPU 在开始执行前等待所需资源或事件所花费的时间。同步类型说明如下。 |
| Synchronization (wait memory) | GPU 等待相关内存访问（例如纹理采样或缓冲区读写）所花费的时间。 |
| Synchronization (wait pixel) | GPU 等待底层像素释放资源所花费的时间。除颜色附件外，像素也可以来自深度缓冲区、模板缓冲区或用户定义资源。融合是造成像素等待的常见原因。使用光栅顺序组来缩短等待时间。 |
| Synchronization (barrier) | 当某个线程到达屏障，而 GPU 等待同组其余线程也到达屏障后再继续时所花费的时间。 |
| Synchronization (atomics) | GPU 在原子指令上花费的时间。 |

### 检查 pass 中各命令的 GPU 时间

Pipeline Statistics 查看器的下半部分会在 Total 列中显示 pass 内各命令的 GPU 时间，以便比较它们各自的耗时。

![使用该管线状态的各命令之间时序对比的截图。](../../../attachments/cfac835c6168984c2d4970b9d9aa5f08/gputools-metal-debugger-psv-commands@2x.png)

## 另请参阅

### Metal 命令分析

- [检查命令的绑定资源](inspecting-the-bound-resources-for-a-command.md) — 通过检查编码器中任意位置的绑定资源来发现问题。
- [检查绘制命令的几何体](inspecting-the-geometry-of-a-draw-command.md) — 通过检查当前几何体，找出 App 的顶点函数、对象函数或网格函数中的问题。
- [检查绘制命令的附件](inspecting-the-attachments-of-a-draw-command.md) — 通过检查单个像素和样本来发现附件问题。
- [调试绘制命令或计算调度中的着色器](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) — 使用着色器调试器识别并修复 App 中有问题的着色器。
- [使用 GPU 计数器分析绘制命令和计算调度性能](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) — 通过检查性能计数器来识别帧捕获中的问题。
