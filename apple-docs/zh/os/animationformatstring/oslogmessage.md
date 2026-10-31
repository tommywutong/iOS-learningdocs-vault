---
title: AnimationFormatString.OSLogMessage
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/animationformatstring/oslogmessage
source_url: 'https://developer.apple.com/documentation/os/animationformatstring/oslogmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/animationformatstring/oslogmessage.json'
content_hash: 'sha256:85ea5ebd9836cbe6'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [AnimationFormatString](../animationformatstring.md)

# AnimationFormatString.OSLogMessage

<sub>结构体</sub>

一条包含动画标记的日志消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogMessage
```

## 概述

[OSLogMessage](oslogmessage.md) 结构体包含一条由字符串插值或字符串字面量构造的消息。此消息还带有一个额外的动画标记。不要直接创建此结构体。当你使用 [os_signpost(_:dso:log:name:signpostID:_:_:)](<../os_signpost(__dso_log_name_signpostid_____)-nez5.md>) 函数记录消息时，系统会自动创建它。

## 关系

- **遵循**：[BitwiseCopyable](../../swift/bitwisecopyable.md)、[Copyable](../../swift/copyable.md)、[ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md)、[ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md)、[ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md)

## 主题

### 创建格式化字符串

- [init(stringLiteral:)](<oslogmessage/init(stringliteral_).md>) — 使用字符串字面量创建一条日志消息。
