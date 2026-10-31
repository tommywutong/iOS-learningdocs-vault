---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/init(subsystem:category:)-4vdri'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/init(subsystem:category:)-4vdri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/init%28subsystem%3Acategory%3A%29-4vdri.json'
content_hash: 'sha256:881b7c8587900c65'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# init(subsystem:category:)

<sub>初始化方法</sub>

创建一个使用指定子系统和系统定义的日志分类的 signposter。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(subsystem: String, category: OSLog.Category)
```

## 参数

- `subsystem` — 标识发出 signpost 的子系统的字符串。通常使用与你的 App 的 _bundle ID_ 相同的值。更多信息参见 [CFBundleIdentifier](../../bundleresources/information-property-list/cfbundleidentifier.md)。

- `category` — 系统定义的分类，系统用它来对发出的 signpost 进行分类。可能的值参见 [Category](../oslog/category.md)。

## 另请参阅

### 创建 Signposter

- [init()](<init().md>) — 创建一个使用默认子系统的 signposter。
- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — 创建一个使用指定子系统和分类的 signposter。
- [init(logger:)](<init(logger_).md>) — 创建一个使用现有 logger 的子系统和分类的 signposter。
- [init(logHandle:)](<init(loghandle_).md>) — 创建一个使用现有日志的子系统和分类的 signposter。
- [disabled](disabled.md) — 一个共享的 signposter，运行时不会发出 signpost。
