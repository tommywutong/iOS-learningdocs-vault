---
title: init()
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignposter/init()
source_url: 'https://developer.apple.com/documentation/os/ossignposter/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/init%28%29.json'
content_hash: 'sha256:f4375e84e4fd6791'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# init()

<sub>初始化方法</sub>

创建一个使用默认子系统的 signposter。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## 另请参阅

### 创建 Signposter

- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — 创建一个使用指定子系统和分类的 signposter。
- [init(subsystem:category:)](<init(subsystem_category_)-4vdri.md>) — 创建一个使用指定子系统和系统定义的日志分类的 signposter。
- [init(logger:)](<init(logger_).md>) — 创建一个使用现有 logger 的子系统和分类的 signposter。
- [init(logHandle:)](<init(loghandle_).md>) — 创建一个使用现有日志的子系统和分类的 signposter。
- [disabled](disabled.md) — 一个共享的 signposter，运行时不会发出 signpost。
