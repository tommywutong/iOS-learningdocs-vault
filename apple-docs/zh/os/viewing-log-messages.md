---
title: 查看日志消息
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/viewing-log-messages
source_url: 'https://developer.apple.com/documentation/os/viewing-log-messages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/viewing-log-messages.json'
content_hash: 'sha256:c3e2514cfd9b2e59'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 查看日志消息

<sub>文章</sub>

使用各种工具获取日志信息。

## 概述

统一日志系统以二进制压缩格式存储日志消息，把将其转换为人类可读文本消息的大部分工作推迟处理。使用二进制格式让日志系统能存储更多消息，并降低了记录数据的开销。但这也意味着你不能直接读取和解析日志文件；你需要用工具把日志消息转换成可读格式。根据你使用的工具不同，这种转换可能在 App 运行期间进行，也可能在之后、App 已经退出时进行。

以下是一些可用于读取日志数据的工具：

- Console App 提供了一个图形用户界面，用于读取和整理日志数据。
- 使用 `log` 工具从命令行获取日志消息。
- 在 Xcode 里附加调试器运行 App 时，Xcode 会自动显示已记录的消息。同样，你也可以从 Xcode 内部启动 Instruments，来记录和分析 App 创建的 signpost。
- 使用 [OSLog](../oslog.md) 框架以编程方式访问已记录的消息。

## 另请参阅

### 基础

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md) — 记录有用的调试与分析信息，并在消息中包含动态内容。
- [Customizing Logging Behavior While Debugging](customizing-logging-behavior-while-debugging.md) — 控制记录哪些日志事件。
