---
title: disabled
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignposter/disabled
source_url: 'https://developer.apple.com/documentation/os/ossignposter/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/disabled.json'
content_hash: 'sha256:5d7ad894641df36e'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# disabled

<sub>类型属性</sub>

一个共享的 signposter，运行时不会发出 signpost。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var disabled: OSSignposter { get }
```

## 讨论

你可以使用此属性返回的 signposter，在生产构建中禁用 signpost，而无需重构代码，如下例所示：

```swift
let signposter: OSSignposter
#if DEBUG
signposter = OSSignposter()
#else
signposter = OSSignposter.disabled
#endif
```

要判断某个 signposter 是否可以发出 signpost，请使用 [isEnabled](isenabled.md) 属性。

## 另请参阅

### 创建 Signposter

- [init()](<init().md>) — 创建一个使用默认子系统的 signposter。
- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — 创建一个使用指定子系统和分类的 signposter。
- [init(subsystem:category:)](<init(subsystem_category_)-4vdri.md>) — 创建一个使用指定子系统和系统定义的日志分类的 signposter。
- [init(logger:)](<init(logger_).md>) — 创建一个使用现有 logger 的子系统和分类的 signposter。
- [init(logHandle:)](<init(loghandle_).md>) — 创建一个使用现有日志的子系统和分类的 signposter。
