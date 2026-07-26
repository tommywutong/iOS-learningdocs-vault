---
title: 'DispatchPredicate.onQueueAsBarrier(_:)'
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchpredicate/onqueueasbarrier(_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchpredicate/onqueueasbarrier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchpredicate/onqueueasbarrier%28_%3A%29.json'
content_hash: 'sha256:e28ccfe07f13aa63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchPredicate](../dispatchpredicate.md)

# DispatchPredicate.onQueueAsBarrier(_:)

<sub>Case</sub>

A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case onQueueAsBarrier(DispatchQueue)
```

## Discussion

For more information about barrier operations, see `[barrier](../dispatchworkitemflags/barrier.md)`.

## See Also

### Predicates

- [DispatchPredicate.onQueue(_:)](<onqueue(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.notOnQueue(_:)](<notonqueue(__).md>) — A predicate that indicates the evaluated context is not the associated dispatch queue.
