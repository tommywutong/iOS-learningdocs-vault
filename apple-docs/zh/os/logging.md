---
title: 日志记录
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/logging
source_url: 'https://developer.apple.com/documentation/os/logging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logging.json'
content_hash: 'sha256:b39f3ee27d50a94e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# 日志记录

<sub>API 集合</sub>

使用统一日志系统从你的 App 中获取遥测数据，用于调试和性能分析。

## 概述

在调试 App 中的问题时，记录发生过的确切事件序列，以及这些事件的补充数据，会很有帮助。日志消息提供了 App 运行时行为的连续记录，让你更容易发现那些用其他手段不易捕捉到的问题。具体来说，你可能会在以下情况使用日志消息：

- 无法给 App 附加调试器时，例如你正在诊断用户设备上的问题。
- 问题是间歇性的，难以在调试器里捕获。
- 想大致了解 App 的行为——例如，想知道某些任务何时开始、何时结束。

统一日志系统提供了一套全面且高性能的 API，可以捕获系统各个层级的遥测数据。该系统把日志数据集中存储在内存和磁盘上，而不是写入基于文本的日志文件。你可以用 Console App、`log` 命令行工具或 Xcode 调试控制台查看日志消息，也可以用 [OSLog](../oslog.md) 框架以编程方式访问日志消息。

> [!important] 重要
> 统一日志系统适用于 iOS 10.0 及更高版本、macOS 10.12 及更高版本、tvOS 10.0 及更高版本、watchOS 3.0 及更高版本。该系统取代了 Apple System Logger (ASL) 和 Syslog API。

## 主题

### 基础

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md) — 记录有用的调试与分析信息，并在消息中包含动态内容。
- [Viewing Log Messages](viewing-log-messages.md) — 使用各种工具获取日志信息。
- [Customizing Logging Behavior While Debugging](customizing-logging-behavior-while-debugging.md) — 控制记录哪些日志事件。

### 日志消息

- [Logger](logger.md) — 用于向统一日志系统写入插值字符串消息的对象。
- [Message Argument Formatters](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [OSSignposter](ossignposter.md) — 用于借助统一日志系统测量任务性能的对象。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。
