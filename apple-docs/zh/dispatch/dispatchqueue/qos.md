---
title: qos
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/qos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/qos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/qos.json'
content_hash: 'sha256:e751eb22b0a0cbc0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# qos

<sub>实例属性</sub>

分配给该队列的服务质量级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var qos: DispatchQoS { get }
```

## 另请参阅

### 管理队列特性

- [label](label.md) — 你在创建时为该 dispatch queue 分配的标签。
- [dispatch_set_target_queue](<../dispatchobject/settarget(queue_).md>) — 指定在其上执行与当前对象关联的工作的 dispatch queue。
