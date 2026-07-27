---
title: GPU 计数器与计数器采样缓冲区
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/gpu-counters-and-counter-sample-buffers
source_url: 'https://developer.apple.com/documentation/metal/gpu-counters-and-counter-sample-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/gpu-counters-and-counter-sample-buffers.json'
content_hash: 'sha256:2770c382450f5bb2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# GPU 计数器与计数器采样缓冲区

<sub>API 集合</sub>

通过对 GPU 设备的一个或多个计数器进行采样，从中获取运行时数据。

## 概述

GPU _计数器（counter）_（[MTLCounter](mtlcounter.md)）通常是一种硬件特性，用于跟踪某个特定的性能指标，例如某个重要渲染阶段前后的时间戳。_计数器集（counter set）_（[MTLCounterSet](mtlcounterset.md)）是一组相关计数器的集合。_计数器采样缓冲区（counter sample buffer）_（[MTLCounterSampleBuffer](mtlcountersamplebuffer.md)）表示 GPU 设备存储特定计数器集数据的内存。

你可以通过以下步骤获取并检查 GPU 计数器集中的数据：

1. 检查某个 GPU 设备支持哪些 GPU 计数器集（参见 [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)）。
2. 创建一个计数器采样缓冲区来存储数据（参见 [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)）。
3. 指示 GPU 在某个流程或即时模式命令期间将计数器集数据保存到该缓冲区中（参见 [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)）。
4. 将计数器集数据转换为标准类型（参见 [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)）。

如果你要从时间戳计数器集（[MTLCommonCounterSetTimestamp](mtlcommoncounterset/timestamp.md)）中采样数据，可能需要将时间戳从 GPU 的时钟转换为 CPU 的时钟。更多信息参见 [Converting GPU timestamps into CPU time](converting-gpu-timestamps-into-cpu-time.md)。

## 主题

### 计数器与计数器集

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md) — 检查某个 GPU 是否生成你想要采样的运行时性能数据。
- [MTLCounterSet](mtlcounterset.md) — 某个 GPU 设备针对某个计数器集所支持的一组独立计数器。
- [MTLCommonCounterSet](mtlcommoncounterset.md) — 某个 GPU 设备可以支持的特定计数器集的名称。
- [MTLCounter](mtlcounter.md) — 某个 GPU 设备在其某个计数器集中列出的一个独立计数器。
- [MTLCommonCounter](mtlcommoncounter.md) — 可以出现在某个 GPU 设备的计数器集中的特定计数器的名称。

### 计数器采样缓冲区

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) — 创建一个缓冲区，为 GPU 在运行某个流程时保存其运行时性能指标提供存放位置。
- [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) — 用于配置你借此创建的计数器采样缓冲区的一组属性。
- [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) — 一种存储 GPU 计数器集数据的专用内存缓冲区。
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) — 在 GPU 支持的时机获取该 GPU 的计数器数据。
- [MTLCounterDontSample](mtlcounterdontsample.md) — 一个哨兵值，指示编码器在 GPU 运行该编码器的流程时跳过对某个计数器的采样。

### 计数器采样数据输出

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) — 通过将 GPU 计数器采样缓冲区中的数据解析为标准格式，来检查并使用该数据。
- [MTLCounterResultTimestamp](mtlcounterresulttimestamp.md) — 用于存储你从时间戳计数器集解析出的数据的数据结构。
- [MTLCounterResultStatistic](mtlcounterresultstatistic.md) — 用于存储你从统计计数器集解析出的数据的数据结构。
- [MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md) — 用于存储你从阶段利用率计数器集解析出的数据的数据结构。
- [MTLCounterErrorValue](mtlcountererrorvalue.md) — 计数器采样缓冲区中某个条目的哨兵值，表示该条目的数据无效。

### 时间戳数据

- [Converting GPU timestamps into CPU time](converting-gpu-timestamps-into-cpu-time.md) — 通过计算 GPU 时间戳对应的 CPU 时间，将 GPU 事件与 CPU 时间线关联起来。
- [MTLTimestamp](mtltimestamp.md) — 表示绝对时间或 Mach 绝对时间中某个时间点的纳秒数。

### 计数器采样缓冲区错误

- [MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md) — 指示 GPU 驱动程序为何无法创建计数器采样缓冲区的错误代码。

## 另请参阅

### 开发者工具

- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md) — 在你的 Metal App 中配置替代渲染路径，使 App 能够在模拟器中运行。
- [Capturing Metal commands programmatically](capturing-metal-commands-programmatically.md) — 从你的 App 中调用 Metal 帧捕获，然后将生成的 GPU 跟踪信息保存到文件中或在 Xcode 中查看。
- [Logging shader debug messages](logging-shader-debug-messages.md) — 使用着色器日志记录功能打印着色器生成的调试消息。
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md) — 在模拟器中对你的 Metal App 进行原型设计和测试。
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md) — 使用强大的 Metal 开发工具套件修复性能问题，并为 Apple 平台上的流畅体验制定默认设置。
- [Metal debugger](../xcode/metal-debugger.md) — 使用 GPU 跟踪信息调试和分析你的 Metal 工作负载。
- [Metal developer workflows](../xcode/metal-developer-workflows.md) — 定位并修复与你的 App 使用 Metal API 和 GPU 函数相关的问题。
- [Metal debugging types](metal-debugging-types.md) — 创建捕获管理器和捕获范围，并在 GPU 设备运行完某个命令缓冲区后查看其日志。
