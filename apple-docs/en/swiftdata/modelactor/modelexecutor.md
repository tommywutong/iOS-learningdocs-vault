---
title: modelExecutor
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelactor/modelexecutor
source_url: 'https://developer.apple.com/documentation/swiftdata/modelactor/modelexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelactor/modelexecutor.json'
content_hash: 'sha256:d7a5dd1889e8892e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelActor](../modelactor.md)

# modelExecutor

<sub>Instance Property</sub>

The executor that coordinates access to the model actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var modelExecutor: any ModelExecutor { get }
```

## Discussion

> [!important] Important
> Don’t use the executor to access the model context. Instead, use the [modelContext](modelcontext.md) property.

## See Also

### Accessing the executors

- [unownedExecutor](unownedexecutor.md) — The optimized, unonwned reference to the model actor’s executor.
