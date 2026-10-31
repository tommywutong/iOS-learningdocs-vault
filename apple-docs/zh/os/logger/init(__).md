---
title: 'init(_:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/init(_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/init%28_%3A%29.json'
content_hash: 'sha256:d4333b02a05d6286'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# init(_:)

<sub>初始化方法</sub>

创建一个写入指定日志的 logger。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ logObj: OSLog)
```

## 参数

- `logObj` — 要将消息写入的日志。

## 另请参阅

### 创建 Logger

- [init()](<init().md>) — 创建一个写入默认子系统的 logger。
- [init(subsystem:category:)](<init(subsystem_category_).md>) — 使用指定的子系统和分类创建一个 logger。
- [OSLog](../oslog.md) — 相关日志消息的容器。
