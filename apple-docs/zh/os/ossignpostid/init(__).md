---
title: 'init(_:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostid/init(_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28_%3A%29.json'
content_hash: 'sha256:4bf5085b74c72ddd'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(_:)

<sub>初始化方法</sub>

用任意 64 位整数值创建 signpost ID。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: UInt64)
```

## 参数

- `value` — 生成 signpost ID 时使用的值。

## 另请参阅

### 创建 Signpost 标识符

- [init(log:)](<init(log_).md>) — 为指定日志创建 signpost ID。 _(已废弃)_
- [init(log:object:)](<init(log_object_).md>) — 创建一个 signpost ID，并将其与指定对象关联。 _(已废弃)_
