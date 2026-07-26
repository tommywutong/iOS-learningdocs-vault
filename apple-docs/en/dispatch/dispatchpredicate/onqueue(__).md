---
title: 'DispatchPredicate.onQueue(_:)'
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchpredicate/onqueue(_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchpredicate/onqueue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchpredicate/onqueue%28_%3A%29.json'
content_hash: 'sha256:ef3891754f6c1e77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchPredicate](../dispatchpredicate.md)

# DispatchPredicate.onQueue(_:)

<sub>Case</sub>

A predicate that indicates the evaluated context is the associated dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case onQueue(DispatchQueue)
```

## See Also

### Predicates

- [DispatchPredicate.onQueueAsBarrier(_:)](<onqueueasbarrier(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
- [DispatchPredicate.notOnQueue(_:)](<notonqueue(__).md>) — A predicate that indicates the evaluated context is not the associated dispatch queue.
