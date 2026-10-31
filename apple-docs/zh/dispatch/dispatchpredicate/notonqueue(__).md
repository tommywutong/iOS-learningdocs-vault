---
title: 不在队列上的谓词 notOnQueue(_:)
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchpredicate/notonqueue(_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchpredicate/notonqueue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchpredicate/notonqueue%28_%3A%29.json'
content_hash: 'sha256:cdbcf20f98deb7e5'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchPredicate](../dispatchpredicate.md)

# DispatchPredicate.notOnQueue(_:)

<sub>Case</sub>

指示所评估的上下文不是关联 dispatch queue 的谓词。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case notOnQueue(DispatchQueue)
```

## 另请参阅

### 谓词

- [DispatchPredicate.onQueue(_:)](<onqueue(__).md>) — 指示所评估的上下文是关联 dispatch queue 的谓词。
- [DispatchPredicate.onQueueAsBarrier(_:)](<onqueueasbarrier(__).md>) — 指示所评估的上下文作为屏障操作的一部分是关联 dispatch queue 的谓词。
