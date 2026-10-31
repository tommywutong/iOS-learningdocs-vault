---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/init(subsystem:category:)'
source_url: 'https://developer.apple.com/documentation/os/logger/init(subsystem:category:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/init%28subsystem%3Acategory%3A%29.json'
content_hash: 'sha256:9eb2e624a575879f'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# init(subsystem:category:)

<sub>初始化方法</sub>

使用指定的子系统和分类创建一个 logger。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(subsystem: String, category: String)
```

## 参数

- `subsystem` — 标识发出 signpost 的子系统的字符串。通常使用与你的 App 的 _bundle ID_ 相同的值。更多信息参见 [CFBundleIdentifier](../../bundleresources/information-property-list/cfbundleidentifier.md)。

- `category` — 系统用于对发出的 signpost 进行分类的字符串。

## 另请参阅

### 创建 Logger

- [init()](<init().md>) — 创建一个写入默认子系统的 logger。
- [init(_:)](<init(__).md>) — 创建一个写入指定日志的 logger。
- [OSLog](../oslog.md) — 相关日志消息的容器。
