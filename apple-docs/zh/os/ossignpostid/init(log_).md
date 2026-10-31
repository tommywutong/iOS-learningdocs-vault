---
title: 'init(log:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/ossignpostid/init(log:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(log:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28log%3A%29.json'
content_hash: 'sha256:fca87e507ab2e3bc'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(log:)

<sub>初始化方法</sub>

为指定日志创建 signpost ID。

> [!warning] 已废弃
> 请改用 [makeSignpostID()](<../ossignposter/makesignpostid().md>)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(log: OSLog)
```

## 参数

- `log` — 你要将带 signpost 标记的事件写入的日志。

## 另请参阅

### 创建 Signpost 标识符

- [init(_:)](<init(__).md>) — 用任意 64 位整数值创建 signpost ID。
- [init(log:object:)](<init(log_object_).md>) — 创建一个 signpost ID，并将其与指定对象关联。 _(已废弃)_
