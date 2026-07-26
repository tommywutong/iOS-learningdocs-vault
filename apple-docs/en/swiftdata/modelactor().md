---
title: ModelActor()
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelactor()
source_url: 'https://developer.apple.com/documentation/swiftdata/modelactor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelactor%28%29.json'
content_hash: 'sha256:111586a672f69109'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelActor()

<sub>Macro</sub>

Converts a Swift actor into a model actor by generating boilerplate code that fulfills the requirements of the associated protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(member, names: named(modelExecutor), named(modelContainer), named(init)) @attached(extension, conformances: ModelActor) macro ModelActor()
```

## See Also

### Model actors

- [ModelActor](modelactor.md) — An interface for providing mutually-exclusive access to the attributes of a conforming model.
