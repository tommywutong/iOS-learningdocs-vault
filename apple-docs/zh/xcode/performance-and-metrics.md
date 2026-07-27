---
title: 性能与指标
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/performance-and-metrics
source_url: 'https://developer.apple.com/documentation/xcode/performance-and-metrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/performance-and-metrics.json'
content_hash: 'sha256:8809d3733ff5ebc6'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md)

# 性能与指标

使用 Instruments 和 Xcode Organizer 测量、调查并解决系统资源使用情况以及影响性能的问题。

## 主题

### 基础

- [提升你 App 的性能](improving-your-app-s-performance.md) — 通过持续改进的循环流程，为你的 App 建模、测量并提升其性能。
- [使用 Instruments 分析 App](../tutorials/instruments.md) — 使用 Instruments 分析你 App 的性能、资源使用情况和行为。学习如何提高响应速度、降低内存使用量，以及分析随时间变化的复杂行为。
- [分析你已发布 App 的性能](analyzing-the-performance-of-your-shipping-app.md) — 查看你通过 App Store 分发的 App 的功耗和性能指标。
- [为你的 visionOS App 创建性能计划](../visionos/creating-a-performance-plan-for-visionos-app.md) — 确定你 App 的性能与功耗目标，并制定计划来测量和评估它们。

### 响应速度

- [分析你已发布 App 中的响应速度问题](analyzing-responsiveness-issues-in-your-shipping-app.md) — 识别用户遇到的响应速度问题，并使用 Xcode Organizer 中的挂起和卡顿数据，确定哪些问题最需要优先修复。
- [提升 App 响应速度](improving-app-responsiveness.md) — 通过消除 App 中的挂起和卡顿，打造响应灵敏的用户体验。
- [了解用户界面响应速度](understanding-user-interface-responsiveness.md) — 通过检查事件处理和渲染循环，让你的 App 更具响应性。
- [了解并提升 SwiftUI 性能](understanding-and-improving-swiftui-performance.md) — 识别并解决耗时过长的视图更新，并降低更新频率。
- [了解你 App 中的挂起](understanding-hangs-in-your-app.md) — 通过检查主线程和主运行循环，确定用户交互延迟的原因。
- [了解你 App 中的卡顿](understanding-hitches-in-your-app.md) — 通过检查渲染循环，确定动作中断的原因。
- [及早诊断性能问题](diagnosing-performance-issues-early.md) — 在开发和测试期间，使用 Xcode 中的 Thread Performance Checker 工具，诊断你 App 中潜在的性能问题。
- [缩短你 App 的启动时间](reducing-your-app-s-launch-time.md) — 通过最大限度减少启动所花费的时间，为你的 App 打造更具响应性的体验。
- [减少你 App 中的终止次数](reduce-terminations-in-your-app.md) — 通过解决常见的终止原因，尽量降低系统停止你 App 的频率。

### 处理器使用情况

- [解决 CPU 瓶颈](addressing-cpu-bottlenecks.md) — 定位并修复流水线停顿、缓存未命中以及其他性能问题。
- [使用 Processor Trace instrument 分析 CPU 使用情况](analyzing-cpu-usage-with-processor-trace.md) — 找出你 App 中 CPU 使用效率低下的代码。
- [使用调用树视图分析 CPU 配置文件](analyzing-cpu-profiles-with-call-tree-views.md) — 使用调用树可视化功能，在 Instruments 中找出性能瓶颈。

### 内存与大小

- [减少你 App 的内存使用量](reducing-your-app-s-memory-use.md) — 通过分析内存使用指标并进行相应调整以最大限度提高内存使用效率，提升你 App 的性能。
- [减小你 App 的体积](reducing-your-app-s-size.md) — 测量你 App 的体积，优化其素材和设置，并采用有助于在移动网络连接下简化安装过程的技术。

### 图形

- [分析你 Metal App 的性能](analyzing-the-performance-of-your-metal-app.md) — 通过对你 App 的帧时间进行性能分析，确保渲染始终流畅一致。
- [分析你 Metal App 的内存使用情况](analyzing-the-memory-usage-of-your-metal-app.md) — 通过管理内存占用空间，让你的 App 在后台保持存活。

### 功耗

- [分析你 App 的电池使用情况](analyzing-your-app-s-battery-use.md) — 通过降低你 App 的功耗，延长单次电池充电下 App 的可用时间。
- [使用 Power Profiler 测量你 App 的功耗](measuring-your-app-s-power-use-with-power-profiler.md) — 无论你的设备是否连接到 Xcode，都能对你 App 的功耗影响进行性能分析。
- [降低你 App 的电池使用量](reducing-your-app-s-battery-use.md) — 采用相应的设计原则和推荐的 API，以降低功耗。

### 磁盘使用情况

- [减少磁盘写入](reducing-disk-writes.md) — 通过优化 App 向永久性存储写入数据的方式，提升 App 的响应速度。
- [减少你 App 的磁盘使用量](reducing-your-app-s-disk-usage.md) — 测量并最小化你 App 用于存储其文件所占用的空间。
- [监测你 App 的存储指标](monitoring-your-app-s-storage-metrics.md) — 使用 Xcode Organizer 随时间追踪你 App 的存储占用情况，以便及时发现“文稿与数据”及“App 大小”方面的衰退。

### 网络

- [使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md) — 测量你 App 基于 HTTP 的网络性能和使用情况。

### 自定 instrument

- [为智能 instrument 创建自定建模器](creating-custom-modelers-for-intelligent-instruments.md) — 使用 CLIPS 语言创建自定建模器，并了解内嵌规则引擎的工作原理。

## 另请参阅

### 调优与调试

- [Device Hub](device-hub.md) — 管理你用来测试 App 的模拟设备和实体设备。
- [调试](debugging.md) — 使用 Xcode 调试器、Xcode Organizer、Metal 调试器和 Instruments，识别并解决你 App 中的问题。
- [测试](testing.md) — 开发并运行测试，以检测逻辑错误、UI 问题和性能衰退。
