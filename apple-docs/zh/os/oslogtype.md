---
title: OSLogType
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype
source_url: 'https://developer.apple.com/documentation/os/oslogtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype.json'
content_hash: 'sha256:9ced5f6b79f97cf4'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogType

<sub>结构体</sub>

统一日志系统提供的各种日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSLogType
```

## 概述

日志级别控制系统如何以及何时将消息写入统一日志系统。要使用特定日志级别写入消息，请创建 [Logger](logger.md) 并调用其 [log(level:_:)](<logger/log(level___).md>) 方法。或者，调用与所需日志级别对应的方法，例如 [debug(_:)](<logger/debug(__).md>) 或 [fault(_:)](<logger/fault(__).md>)。

## 关系

- **遵循**： [BitwiseCopyable](../swift/bitwisecopyable.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[RawRepresentable](../swift/rawrepresentable.md)、[Sendable](../swift/sendable.md)

## 主题

### 获取日志类型

- [debug](oslogtype/debug.md) — debug 日志级别。
- [info](oslogtype/info.md) — info 日志级别。
- [default](oslogtype/default.md) — default 日志级别。
- [error](oslogtype/error.md) — error 日志级别。
- [fault](oslogtype/fault.md) — fault 日志级别。

### 创建日志类型

- [init(_:)](<oslogtype/init(__).md>) — 根据指定值创建日志类型。
- [init(rawValue:)](<oslogtype/init(rawvalue_).md>) — 根据指定原始值创建日志类型。

### 获取原始值

- [rawValue](oslogtype/rawvalue.md) — 日志类型的原始值。

## 另请参阅

### 日志消息

- [Logger](logger.md) — 用于向统一日志系统写入插值字符串消息的对象。
- [消息参数格式化器](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
