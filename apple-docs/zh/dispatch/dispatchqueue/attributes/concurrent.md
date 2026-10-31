---
title: concurrent
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/attributes/concurrent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes/concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/attributes/concurrent.json'
content_hash: 'sha256:518ad3acef5487a0'
translated: true
---

> 导航： [技术](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [Attributes](../attributes.md)

# concurrent

<sub>类型属性</sub>

该队列并发调度任务。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let concurrent: DispatchQueue.Attributes
```

## 讨论

如果不存在此属性，队列会以先进先出 (FIFO) 顺序串行调度任务。

## 另请参阅

### 特性

- [initiallyInactive](initiallyinactive.md) — 新创建的队列处于未激活状态。
