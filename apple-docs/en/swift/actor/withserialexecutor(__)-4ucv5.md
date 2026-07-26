---
title: 'withSerialExecutor(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/actor/withserialexecutor(_:)-4ucv5'
source_url: 'https://developer.apple.com/documentation/swift/actor/withserialexecutor(_:)-4ucv5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/actor/withserialexecutor%28_%3A%29-4ucv5.json'
content_hash: 'sha256:d05e7f73d44cc3b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Actor](../actor.md)

# withSerialExecutor(_:)

<sub>Instance Method</sub>

Perform an operation with the actor’s [SerialExecutor](../serialexecutor.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func withSerialExecutor<T, E>(_ operation: (any SerialExecutor) throws(E) -> T) throws(E) -> T where E : Error, T : ~Copyable
```

## Discussion

This converts the actor’s [unownedExecutor](unownedexecutor.md) to a [SerialExecutor](../serialexecutor.md) while retaining the actor for the duration of the operation. This is to ensure the lifetime of the executor while performing the operation.
