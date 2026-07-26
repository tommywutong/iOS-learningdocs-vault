---
title: ModelExecutor
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelexecutor
source_url: 'https://developer.apple.com/documentation/swiftdata/modelexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelexecutor.json'
content_hash: 'sha256:a6702e3cce3074c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelExecutor

<sub>Protocol</sub>

An interface for performing storage-related tasks using an isolated model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ModelExecutor : Executor
```

## Relationships

- **Inherits From**: [Executor](../swift/executor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [SerialModelExecutor](serialmodelexecutor.md)

- **Conforming Types**: [DefaultSerialModelExecutor](defaultserialmodelexecutor.md)

## Topics

### Accessing the context

- [modelContext](modelexecutor/modelcontext.md)

## See Also

### Model executors

- [DefaultSerialModelExecutor](defaultserialmodelexecutor.md) — An object that safely performs storage-related tasks using an isolated model context.
- [SerialModelExecutor](serialmodelexecutor.md) — An interface for performing serial storage-related tasks using an isolated model context.
