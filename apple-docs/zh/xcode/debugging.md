---
title: 调试
framework: updates
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/debugging
source_url: 'https://developer.apple.com/documentation/xcode/debugging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/debugging.json'
content_hash: 'sha256:be9230904980c097'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md)

# 调试

使用 Xcode 调试器、Xcode Organizer、Metal 调试器和 Instruments 识别并解决你的 App 中的问题。

## 主题

### 基础

- [诊断并解决运行中 App 的错误](diagnosing-and-resolving-bugs-in-your-running-app.md) — 检查你的 App，以隔离错误、定位崩溃、识别过量的系统资源使用、直观呈现内存错误，并调查其外观问题。

### 调试策略

- [诊断运行中 App 的外观问题](diagnosing-issues-in-the-appearance-of-your-running-app.md) — 检查正在运行的 App，以调查其显示内容的外观和位置问题。
- [尽早诊断内存、线程与崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md) — 在测试期间使用 Xcode 的 sanitizer 工具识别 App 中的运行时崩溃和未定义行为。
- [使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md) — 测量 App 基于 HTTP 的网络性能和使用情况。
- [检测你的 App 何时联系可能构建用户画像的域](detecting-when-your-app-contacts-domains-that-may-be-profiling-users.md) — 使用 Instruments 评估你的 App 或其第三方 SDK 是否连接到可能构建用户画像的域。

### 图形

- [Metal 开发者工作流](metal-developer-workflows.md) — 定位并修复与你的 App 使用 Metal API 和 GPU 函数有关的问题。
- [Metal 调试器](metal-debugger.md) — 使用 GPU 跟踪来调试并分析你的 Metal 工作负载。

### 断点与变量

- [设置断点以暂停正在运行的 App](setting-breakpoints-to-pause-your-running-app.md) — 指定 App 在调试器中运行时暂停的位置，以调查错误。
- [逐步执行代码并检查变量以隔离错误](stepping-through-code-and-inspecting-variables-to-isolate-bugs.md) — 在调试器中逐步执行源代码时，通过观察变量的变化找出错误原因。

### 报告

- [构建 App 以包含调试信息](building-your-app-to-include-debugging-information.md) — 配置 Xcode，使其生成用于调试和崩溃报告的符号信息。
- [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) — 使用崩溃报告和设备日志调试 App 问题。

### Entitlements

- [诊断 entitlement 问题](../bundleresources/diagnosing-issues-with-entitlements.md) — 在开发的每个阶段验证 App 的 entitlement，以追查分发期间的错误。

## 另请参阅

### 调优与调试

- [Device Hub](device-hub.md) — 管理你用于测试 App 的模拟设备和实体设备。
- [性能与指标](performance-and-metrics.md) — 使用 Instruments 和 Xcode Organizer 测量、调查并解决系统资源使用情况以及影响性能的问题。
- [测试](testing.md) — 开发并运行测试，以检测逻辑故障、用户界面问题和性能衰退。
