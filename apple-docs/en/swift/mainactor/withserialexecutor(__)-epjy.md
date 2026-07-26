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
doc_path: '/documentation/swift/mainactor/withserialexecutor(_:)-epjy'
source_url: 'https://developer.apple.com/documentation/swift/mainactor/withserialexecutor(_:)-epjy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mainactor/withserialexecutor%28_%3A%29-epjy.json'
content_hash: 'sha256:73b7a2a76e17bcda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MainActor](../mainactor.md)

# withSerialExecutor(_:)

<sub>Instance Method</sub>

Perform an operation with the actor’s [SerialExecutor](../serialexecutor.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func withSerialExecutor<T, E>(_ operation: nonisolated(nonsending) (any SerialExecutor) async throws(E) -> T) async throws(E) -> T where E : Error, T : ~Copyable
```

## Discussion

This converts the actor’s [unownedExecutor](../actor/unownedexecutor.md) to a [SerialExecutor](../serialexecutor.md) while retaining the actor for the duration of the operation. This is to ensure the lifetime of the executor while performing the operation.
