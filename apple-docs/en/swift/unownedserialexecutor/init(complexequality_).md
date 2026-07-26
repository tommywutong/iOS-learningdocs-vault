---
title: 'init(complexEquality:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unownedserialexecutor/init(complexequality:)'
source_url: 'https://developer.apple.com/documentation/swift/unownedserialexecutor/init(complexequality:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedserialexecutor/init%28complexequality%3A%29.json'
content_hash: 'sha256:4916882fa4721ad6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedSerialExecutor](../unownedserialexecutor.md)

# init(complexEquality:)

<sub>Initializer</sub>

Opts the executor into complex “same exclusive execution context” equality checks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(complexEquality executor: E) where E : SerialExecutor
```

## Discussion

This means what when asserting or assuming executors, and the current and expected executor are not the same instance (by object equality), the runtime may invoke `isSameExclusiveExecutionContext` in order to compare the executors for equality.

Implementing such complex equality can be useful if multiple executor instances actually use the same underlying serialization context and can be therefore safely treated as the same serial exclusive execution context (e.g. multiple dispatch queues targeting the same serial queue).
