---
title: 'whenLocal(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactor/whenlocal(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/whenlocal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/whenlocal%28_%3A%29.json'
content_hash: 'sha256:9e606580cd8ab7eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# whenLocal(_:)

<sub>Instance Method</sub>

Executes the passed ‘body’ only when the distributed actor is local instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func whenLocal<T, E>(_ body: @Sendable (isolated Self) async throws(E) -> T) async throws(E) -> T? where T : Sendable, E : Error
```

## Discussion

The `Self` passed to the body closure is isolated, meaning that the closure can be used to call non-distributed functions, or even access actor state.

When the actor is remote, the closure won’t be executed and this function will return nil.
