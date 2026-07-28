---
title: 查找你的 Metal App 的 GPU 占用率
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/finding-your-metal-apps-gpu-occupancy
source_url: 'https://developer.apple.com/documentation/xcode/finding-your-metal-apps-gpu-occupancy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/finding-your-metal-apps-gpu-occupancy.json'
content_hash: 'sha256:e21e83dc4ea36d2c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流](metal-developer-workflows.md)

# 查找你的 Metal App 的 GPU 占用率

<sub>文章</sub>

通过占用率来了解执行着色器时的 GPU 使用情况。

## 概述

GPU 有一个它可以同时执行的最大线程数。占用率（Occupancy）衡量的是 GPU 使用了多少该容量。当有命令包含更多要调度的线程并且内部资源足够时，GPU 会创建新的线程。通常，当 App 高效使用 GPU 时，较高的占用率更为有利。

- **计算占用率（Compute occupancy）** — 衡量 GPU 用于执行计算命令的线程占总线程容量的百分比。
- **顶点占用率（Vertex occupancy）** — 衡量 GPU 用于执行顶点线程的线程占总线程容量的百分比。
- **片段占用率（Fragment occupancy）** — 衡量 GPU 用于执行片段线程的线程占总线程容量的百分比。

这些百分比的总和就是 GPU 正在使用的总容量百分比。

你可以在 Instruments 和 Metal 调试器的“性能时间线（Performance timeline）”中获取着色器占用率计数器。更多信息，请参阅[分析你的 Metal App 的性能](analyzing-the-performance-of-your-metal-app.md)和[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)。

### 确定你的 App 的 GPU 占用率是否偏低

当整体占用率测量值未接近 100% 时，你的 App 可能出现低占用率。每个着色器都有一个最大理论占用率，这取决于它在设备上消耗的内部资源量。你可以在“性能时间线”中为每个着色器获取此信息。

占用率高或低本身并不自动意味着存在问题。例如，如果片段着色器正在以高占用率并发运行，那么较低的顶点着色器占用率可能是可以接受的。最终，你需要将占用率测量值与其他计数器或其他 Metal 工具的测量值关联起来，以确定问题。

当整体占用率偏低时，可能意味着存在以下情况之一：

- 你的着色器已经耗尽了一些内部资源，例如线程、线程组或图像块内存（imageblock memory），阻止了 GPU 创建更多线程。
- 你的着色器过于简单，线程执行完毕的速度快于 GPU 创建新线程的速度。
- 你的 App 正在渲染目标中的一个小区域进行渲染，或调度非常小的计算网格，导致 GPU 用完可创建的线程。

关于“性能时间线”的更多信息，请参阅[使用可视化时间线分析 Apple GPU 性能](analyzing-apple-gpu-performance-using-a-visual-timeline.md)。

### 确定对你的 App 的影响

如果你看到整体占用率偏低，下一步是确定它是否对你的 App 产生了负面影响。如果对限制器计数器（limiter counter）的检查也显示低数值，则说明 GPU 正在执行的工作非常少。

当整体占用率偏高时，GPU 正在执行许多线程以隐藏指令延迟。高占用率通常是有益的，因为你希望充分利用 GPU 的潜力。然而，也有可能你的着色器没有高效地使用 GPU。优化它们可以使 GPU 的更多容量可用于其他 GPU 命令。

在极少数情况下，当整体占用率非常高时，GPU 可能无法良好地执行其工作负载，因为线程正在竞争 GPU 内存缓存中的空间（也称为缓存抖动（cache thrashing））。在这种情况下，你可能需要缩减发送给 GPU 的工作量，或更改其访问（读取或写入）内存的方式。例如，你可以尝试以下方法：

- 减少内存访问次数。
- 减少访问的内存量。
- 更改访问内存时使用的时间或空间访问模式。

内存读取或写入限制器计数器可能提供更多关于你的 App 是否存在问题的见解。更多信息，请参阅[减少着色器瓶颈](reducing-shader-bottlenecks.md)。此外，使用其他计数器来确定你使用 GPU 的效率以及 GPU 花费最多时间的地方。

## 另请参阅

### 计数器

- [减少着色器瓶颈](reducing-shader-bottlenecks.md) — 通过检查 GPU 的限制器与利用率计数器，识别并减少其子系统中的拥塞点。
- [测量 GPU 对内存带宽的使用](measuring-the-gpus-use-of-memory-bandwidth.md) — 通过测量 GPU 的内存带宽，检查你的 Metal App 是否正确读取和写入内存。
