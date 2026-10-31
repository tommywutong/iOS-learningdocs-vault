---
title: 'init(log:object:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/ossignpostid/init(log:object:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostid/init(log:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid/init%28log%3Aobject%3A%29.json'
content_hash: 'sha256:22801f7a8f09500e'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostID](../ossignpostid.md)

# init(log:object:)

<sub>初始化方法</sub>

创建一个 signpost ID，并将其与指定对象关联。

> [!warning] 已废弃
> 请改用 [makeSignpostID(from:)](<../ossignposter/makesignpostid(from_).md>)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(log: OSLog, object: AnyObject)
```

## 参数

- `log` — 你要将带 signpost 标记的事件写入的日志。

- `object` — 要与此 signpost ID 关联的对象。

## 讨论

> [!important] 重要
> 如果你的 signpost ID 会跨越进程边界，请不要使用此方法。

## 另请参阅

### 创建 Signpost 标识符

- [init(_:)](<init(__).md>) — 用任意 64 位整数值创建 signpost ID。
- [init(log:)](<init(log_).md>) — 为指定日志创建 signpost ID。 _(已废弃)_
