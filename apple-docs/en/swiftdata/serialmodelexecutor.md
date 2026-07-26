---
title: SerialModelExecutor
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/serialmodelexecutor
source_url: 'https://developer.apple.com/documentation/swiftdata/serialmodelexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/serialmodelexecutor.json'
content_hash: 'sha256:e6b85afee4009342'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# SerialModelExecutor

<sub>Protocol</sub>

An interface for performing serial storage-related tasks using an isolated model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SerialModelExecutor : ModelExecutor, SerialExecutor
```

## Relationships

- **Inherits From**: [Executor](../swift/executor.md), [ModelExecutor](modelexecutor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SerialExecutor](../swift/serialexecutor.md)

- **Conforming Types**: [DefaultSerialModelExecutor](defaultserialmodelexecutor.md)

## See Also

### Model executors

- [DefaultSerialModelExecutor](defaultserialmodelexecutor.md) — An object that safely performs storage-related tasks using an isolated model context.
- [ModelExecutor](modelexecutor.md) — An interface for performing storage-related tasks using an isolated model context.
