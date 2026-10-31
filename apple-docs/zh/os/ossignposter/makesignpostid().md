---
title: makeSignpostID()
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignposter/makesignpostid()
source_url: 'https://developer.apple.com/documentation/os/ossignposter/makesignpostid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/makesignpostid%28%29.json'
content_hash: 'sha256:5ef25e62b4173f86'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# makeSignpostID()

<sub>实例方法</sub>

返回在该 signposter 作用域内唯一的标识符。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSignpostID() -> OSSignpostID
```

## 返回值

用于匹配某个时间区间的各次 signpost 的 signpost ID。

## 讨论

signposter 使用 signpost ID 来配对带 signpost 标记的时间区间的开始与结束；这是必要的，因为具有相同配置和作用域的多个时间区间可以同时进行。

请使用此方法，而不要使用 [init(log:)](<../ossignpostid/init(log_).md>)。

## 另请参阅

### 生成 Signpost ID

- [makeSignpostID(from:)](<makesignpostid(from_).md>) — 返回由该 signposter 从指定对象派生出的标识符。
- [OSSignpostID](../ossignpostid.md) — 用于消除带 signpost 标记的时间区间之间歧义的标识符。
