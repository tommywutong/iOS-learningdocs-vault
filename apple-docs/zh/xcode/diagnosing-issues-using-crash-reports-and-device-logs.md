---
title: 使用崩溃报告和设备日志诊断问题
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs
source_url: 'https://developer.apple.com/documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs.json'
content_hash: 'sha256:50dcfc7ebaf9d8a8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md)

# 使用崩溃报告和设备日志诊断问题

使用崩溃报告和设备日志来调试 App 问题。

## 概述

用户期望 App 稳定、没有 bug，并高效地使用系统资源。操作系统通过收集不同类型的日志来帮助你满足这些期望，你可以使用这些日志来诊断你的 App 中的问题：

- 崩溃报告描述了你的 App 是如何终止的，并记录了崩溃发生时每个线程上正在运行的代码。
- Jetsam 事件报告描述了操作系统终止某个 App 时的系统内存状况。
- 设备控制台日志包含操作系统和各个 App 中发生的操作的详细信息。

你的 App 的分发版本，例如用于 App Store、企业环境或测试团队的版本，需要你使用崩溃报告和设备日志来诊断用户遇到的问题。分发版本不包含在 Xcode 中调试所需的 entitlement。

### 使用崩溃报告解决稳定性问题

崩溃报告是你在诊断问题时最常用的日志类型。当收到 App 的崩溃报告时，使用它们来了解该 App 存在的稳定性问题。崩溃报告描述了你的 App 是如何终止的，还包含每个线程的完整回溯，显示了崩溃发生时正在运行的代码。

要使用崩溃报告调试问题：

1. [使用符号信息构建你的 App](building-your-app-to-include-debugging-information.md#Build-your-app-with-symbol-information)，并在分发该 App 之前保留 Xcode 归档。
2. 获取问题的崩溃报告。有关获取崩溃报告的不同方式，请参阅 [Acquiring crash reports and diagnostic logs](acquiring-crash-reports-and-diagnostic-logs.md)。
3. 将十六进制地址转换为你的 App 的符号名称，如 [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md) 中所述。
4. 确定该崩溃是否符合 [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md) 中的任何一种模式。请参阅 [Analyzing a crash report](analyzing-a-crash-report.md) 和 [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md) 以获得对该问题的更多见解。
5. 更新你的代码以修复该问题。
6. 使用 [XCTest](../xctest.md) 框架添加测试，以确保该问题今后不会再次出现。

### 使用 jetsam 事件报告发现内存低效问题

确保你的 App 高效地使用内存。当 iOS、iPadOS、tvOS、visionOS 或 watchOS 上的某个 App 低效地使用内存时，其他 App 在后台保持驻留内存所能使用的内存就会减少。这种较低的可用内存会限制用户在 App 之间切换的速度，因为这些 App 无法从内存恢复，而必须先完成一次完整的 App 启动。

当操作系统遇到低内存状况，且所需内存超过当前的可用内存时，设备的操作系统可以终止一些 App 以回收它们正在使用的内存。Jetsam 事件报告描述了操作系统终止某个 App 时的系统内存状况。有关如何访问这些日志的方法，请参阅 [Locate crash reports and memory logs on the device](acquiring-crash-reports-and-diagnostic-logs.md#Locate-crash-reports-and-memory-logs-on-the-device)；有关解读 jetsam 事件报告的信息，请参阅 [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md)。

Jetsam 事件报告不包含 App 中正在执行的线程的栈回溯，但它们确实包含有关内存使用的额外系统信息。当你的 App 由于内存压力而崩溃时，请参阅 [Gathering information about memory use](gathering-information-about-memory-use.md) 来了解你的 App 的内存使用模式，并参阅 [Responding to low-memory warnings](responding-to-low-memory-warnings.md) 来了解何时应降低你的内存使用。

### 使用设备控制台日志诊断问题

Apple 设备会在内存中持续维护操作系统和各个 App 中操作的记录。这些日志可以在问题发生后进行查看。有些问题，例如安装 App 时出现的问题，可以通过在 macOS 上使用控制台 App 查看操作系统日志来诊断。有关访问设备控制台日志的说明，请参阅 [Access device console logs](acquiring-crash-reports-and-diagnostic-logs.md#Access-device-console-logs)。

使用 [Logging](../os/logging.md) 框架将你的 App 的日志消息添加到操作系统的日志中。你提供的日志可以包含额外的分组和标记信息，以帮助从最初的用户操作开始追踪问题。这些信息对于诊断复杂的交互很有用，例如调试你的 App 与其某个 App 扩展之间的交互。

> [!important] 重要
> 不要在你的日志中包含涉及隐私的敏感信息。

## 主题

### 基础

- [Acquiring crash reports and diagnostic logs](acquiring-crash-reports-and-diagnostic-logs.md) — 从 App Store、TestFlight 以及直接从设备收集崩溃报告和设备日志。

### 崩溃报告

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md) — 用与你的 App 代码对应的函数名和行号替换崩溃报告中的十六进制地址。
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中找到能识别常见问题的模式，并根据该模式调查问题。
- [Analyzing a crash report](analyzing-a-crash-report.md) — 找出崩溃报告中有助于你诊断问题的线索。
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md) — 了解崩溃报告的结构以及每个字段包含的信息。
- [Interpreting the JSON format of a crash report](interpreting-the-json-format-of-a-crash-report.md) — 了解系统包含在崩溃报告 JSON 中的对象的结构和属性。
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md) — 了解异常类型能告诉你哪些关于你的 App 崩溃原因的信息。

### 设备日志

- [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md) — 发现当可用内存不足时操作系统终止你的 App 的原因。
- [Logging](../os/logging.md) — 使用统一日志系统从你的 App 捕获遥测数据，用于调试和性能分析。

## 另请参阅

### 报告

- [Building your app to include debugging information](building-your-app-to-include-debugging-information.md) — 配置 Xcode 以生成用于调试和崩溃报告的符号信息。
