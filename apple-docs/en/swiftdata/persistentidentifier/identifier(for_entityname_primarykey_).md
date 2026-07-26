---
title: 'identifier(for:entityName:primaryKey:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/persistentidentifier/identifier(for:entityname:primarykey:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentidentifier/identifier(for:entityname:primarykey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentidentifier/identifier%28for%3Aentityname%3Aprimarykey%3A%29.json'
content_hash: 'sha256:34abbb9cec2a4150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [PersistentIdentifier](../persistentidentifier.md)

# identifier(for:entityName:primaryKey:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func identifier<T>(for storeIdentifier: String, entityName: String, primaryKey: T) throws -> PersistentIdentifier where T : Comparable, T : CustomStringConvertible, T : Decodable, T : Encodable, T : Hashable
```
