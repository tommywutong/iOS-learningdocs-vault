---
title: 'subscript(_:as:)'
framework: SwiftData
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelactor/subscript(_:as:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelactor/subscript(_:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelactor/subscript%28_%3Aas%3A%29.json'
content_hash: 'sha256:ca9c2c85e95518e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelActor](../modelactor.md)

# subscript(_:as:)

<sub>Instance Subscript</sub>

Returns the model for the specified identifier, downcast to the appropriate class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(id: PersistentIdentifier, as as: T.Type) -> T? where T : PersistentModel { get }
```
