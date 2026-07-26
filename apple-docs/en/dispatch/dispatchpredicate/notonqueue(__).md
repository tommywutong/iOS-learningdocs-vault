---
title: 'DispatchPredicate.notOnQueue(_:)'
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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchPredicate](../dispatchpredicate.md)

# DispatchPredicate.notOnQueue(_:)

<sub>Case</sub>

A predicate that indicates the evaluated context is not the associated dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case notOnQueue(DispatchQueue)
```

## See Also

### Predicates

- [DispatchPredicate.onQueue(_:)](<onqueue(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.onQueueAsBarrier(_:)](<onqueueasbarrier(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
