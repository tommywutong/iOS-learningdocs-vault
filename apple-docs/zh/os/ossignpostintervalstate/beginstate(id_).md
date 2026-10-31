---
title: 'beginState(id:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/beginstate(id:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/beginstate(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/beginstate%28id%3A%29.json'
content_hash: 'sha256:435bcb72f24f0665'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# beginState(id:)

<sub>类型方法</sub>

根据指定的 signpost ID 重新创建时间区间状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func beginState(id: OSSignpostID) -> OSSignpostIntervalState
```

## 参数

- `id` — 你用来开始带 signpost 标记的时间区间的 signpost ID。

## 返回值

重新创建的时间区间状态。

## 讨论

> [!important] 重要
> 重新创建时间区间状态以结束带 signpost 标记的时间区间，会绕过检查该时间区间开始与结束是否一致的运行时断言。
