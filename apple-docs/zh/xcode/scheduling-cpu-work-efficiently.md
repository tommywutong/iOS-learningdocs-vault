---
title: 高效调度 CPU 工作
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/scheduling-cpu-work-efficiently
source_url: 'https://developer.apple.com/documentation/xcode/scheduling-cpu-work-efficiently'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/scheduling-cpu-work-efficiently.json'
content_hash: 'sha256:2a5ba3261a8ac510'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减少 App 的电池消耗](reducing-your-app-s-battery-use.md)

# 高效调度 CPU 工作

<sub>文章</sub>

使用并发编程并调整后台活动的优先级，以提升你的 App 的性能。

## 概述

通过采用以下策略，减少你的 App 执行的总计算量：

- 选择高效的算法。
- 将常用结果缓存到内存中，而不是在每次你的 App 需要使用结果时重新计算。
- 重用结构体和对象，以避免释放和重新分配实例的开销。
- 优先采用事件驱动设计，让你的 App 代码在需要执行工作时接收通知，而不是轮询可用任务。
- 使用高层系统框架来实现你的 App 的目标，因为这些框架经过优化，可降低功耗开销。例如，使用 [Core ML](../coreml.md) 处理机器学习模型，使用 [Core Video](../corevideo.md) 执行视频处理。

此外，通过避免 CPU 瓶颈（它会降低 CPU 效率），来减少你的 App 在 CPU 上进行计算所消耗的能量。更多信息，请参阅 [处理 CPU 瓶颈](addressing-cpu-bottlenecks.md)。

### 采用并发编程

使用并发编程技巧，例如 [Swift 并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) 或 [Dispatch](../dispatch.md)，在多个 CPU 核心上高效调度工作。采用并发编程还有助于通过将处理工作移至后台线程，避免你的 App 中出现挂起和卡顿（hitch）。更多信息，请参阅 [提高 App 响应能力](improving-app-responsiveness.md)。

为并发操作确定合适的粒度，以便在 CPU 可以调度到多个核心上执行多个操作，与每个操作执行足够工作以避免管理操作产生过多开销之间取得平衡。理想情况下，每个独立操作需要 10–100 毫秒完成。

为并发操作设置 [DispatchQoS](../dispatch/dispatchqos.md)（服务质量，QoS）级别，以确保系统能够响应式地调度 UI 相关任务，并使用高效的策略完成后台操作。通常，使用对你的任务来说合理的最低 QoS 值，因为系统对较低 QoS 的任务采用更节能的调度方式。更多关于为操作设置 QoS 的信息，请参阅 [为 Apple 芯片优化代码性能](../apple-silicon/tuning-your-code-s-performance-for-apple-silicon.md)。

如果从高 QoS 操作创建对低 QoS 操作的依赖，Xcode 中的线程性能检查器（Thread Performance Checker）会报告运行时问题。更多关于使用线程性能检查器的信息，请参阅 [尽早诊断性能问题](diagnosing-performance-issues-early.md)。

### 在后台调度工作

使用 [Background Tasks](../backgroundtasks.md) 在后台执行工作。系统会优化后台任务的调度——例如，将任务批量处理或在设备充电时运行任务。更多信息，请参阅 [为你的 App 选择后台策略](../backgroundtasks/choosing-background-strategies-for-your-app.md)。

### 合理地为实时活动设定优先级

当你发送包含你的 App 实时活动（Live Activity）更新的推送通知，且该更新不需要用户立即关注时，将 `apns-priority` HTTP 头部字段的值设置为 `5`。这会向 Apple 推送通知服务（APNs）服务器指示，它可以用节能的方式投递该推送通知。将 `apns-priority` 设置为 `5` 的通知不计入你的 App 的实时活动更新预算，因此将此值设置为 `5` 有助于降低你的 App 超出预算的可能性。如果 App 确实超出了预算，系统会降低投递通知的速率。更多信息，请参阅 [通过 ActivityKit 推送通知启动和更新实时活动](../activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications.md#Determine-the-update-frequency)。

## 另请参阅

### 基础

- [响应电源通知](responding-to-power-notifications.md) — 采用更节能的策略，延长设备的电池续航。
