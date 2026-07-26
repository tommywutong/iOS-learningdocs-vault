---
title: 'entity(for:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/schema/entity(for:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/entity(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/entity%28for%3A%29.json'
content_hash: 'sha256:a068db4cec33c95b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# entity(for:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func entity<T>(for type: T.Type) -> Schema.Entity? where T : PersistentModel
```
