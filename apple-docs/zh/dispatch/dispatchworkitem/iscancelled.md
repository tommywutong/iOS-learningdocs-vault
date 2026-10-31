---
title: isCancelled
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitem/iscancelled
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitem/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitem/iscancelled.json'
content_hash: 'sha256:815e00cf2e6b5399'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItem](../dispatchworkitem.md)

# isCancelled

<sub>实例属性</sub>

指示工作项是否已取消的 Boolean 值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## 讨论

如果工作项已被取消，此属性的值为 [true](../../swift/true.md)。

## 另请参阅

### 取消工作项

- [cancel()](<cancel().md>) — 异步取消当前工作项。
