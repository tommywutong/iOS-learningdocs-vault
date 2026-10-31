---
title: OSLogMessage
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogmessage
source_url: 'https://developer.apple.com/documentation/os/oslogmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogmessage.json'
content_hash: 'sha256:a1464749fb3c2fe3'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogMessage

<sub>结构体</sub>

表示日志消息的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogMessage
```

## 概述

> [!important] 重要
> 不要直接创建 [OSLogMessage](oslogmessage.md) 的实例。相反，当你使用 [Logger](logger.md) 向统一日志系统写入消息时，系统会为你创建它们。

## 关系

- **遵循**：[ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)、[ExpressibleByStringInterpolation](../swift/expressiblebystringinterpolation.md)、[ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)、[ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)

## 主题

### 获取消息详情

- [bufferSize](oslogmessage/buffersize.md) — 日志系统接收到的缓冲区的字节大小。
- [interpolation](oslogmessage/interpolation.md) — 日志消息的字符串插值。
- [maxOSLogArgumentCount](maxoslogargumentcount.md) — 日志消息可包含的插值表达式的最大数量。

## 另请参阅

### 记录消息

- [log(_:)](<logger/log(__).md>) — 使用默认日志类型向日志写入一条消息。
- [log(level:_:)](<logger/log(level___).md>) — 使用指定的日志类型向日志写入一条消息。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
