---
title: unownedExecutor
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelactor/unownedexecutor
source_url: 'https://developer.apple.com/documentation/swiftdata/modelactor/unownedexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelactor/unownedexecutor.json'
content_hash: 'sha256:311f06a7b82997fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelActor](../modelactor.md)

# unownedExecutor

<sub>Instance Property</sub>

The optimized, unonwned reference to the model actor’s executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var unownedExecutor: UnownedSerialExecutor { get }
```

## See Also

### Accessing the executors

- [modelExecutor](modelexecutor.md) — The executor that coordinates access to the model actor.
