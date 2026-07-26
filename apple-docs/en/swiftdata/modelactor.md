---
title: ModelActor
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelactor
source_url: 'https://developer.apple.com/documentation/swiftdata/modelactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelactor.json'
content_hash: 'sha256:7d5237ab5a530b60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelActor

<sub>Protocol</sub>

An interface for providing mutually-exclusive access to the attributes of a conforming model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ModelActor : Actor
```

## Relationships

- **Inherits From**: [Actor](../swift/actor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the container and context

- [modelContainer](modelactor/modelcontainer.md) — The ModelContainer for the ModelActor The container that manages the app’s schema and model storage configuration
- [modelContext](modelactor/modelcontext.md) — The context that serializes any code running on the model actor.

### Accessing the executors

- [modelExecutor](modelactor/modelexecutor.md) — The executor that coordinates access to the model actor.
- [unownedExecutor](modelactor/unownedexecutor.md) — The optimized, unonwned reference to the model actor’s executor.

### Accessing specific models

- [subscript(_:as:)](<modelactor/subscript(__as_).md>) — Returns the model for the specified identifier, downcast to the appropriate class.

## See Also

### Model actors

- [ModelActor()](<modelactor().md>) — Converts a Swift actor into a model actor by generating boilerplate code that fulfills the requirements of the associated protocol.
