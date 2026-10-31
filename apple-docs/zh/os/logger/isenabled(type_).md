---
title: 'isEnabled(type:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/isenabled(type:)'
source_url: 'https://developer.apple.com/documentation/os/logger/isenabled(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/isenabled%28type%3A%29.json'
content_hash: 'sha256:f5441e7d6d6654ce'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# isEnabled(type:)

<sub>实例方法</sub>

检查 Logger 是否可以为给定的日志类型发出日志消息。这允许你根据日志级别对日志记录进行更精细的控制。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEnabled(type: OSLogType) -> Bool
```

## 参数

- `type` — 要检查的日志类型（例如 .default、.info、.debug、.error、.fault）

## 返回值

如果已为指定的日志类型启用日志记录，则为 true；否则为 false
