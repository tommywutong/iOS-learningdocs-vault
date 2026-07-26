---
title: 'fetchIdentifiers(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/datastore/fetchidentifiers(_:)-6p9oh'
source_url: 'https://developer.apple.com/documentation/swiftdata/datastore/fetchidentifiers(_:)-6p9oh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastore/fetchidentifiers%28_%3A%29-6p9oh.json'
content_hash: 'sha256:cefab8daabcf61c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [DataStore](../datastore.md)

# fetchIdentifiers(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchIdentifiers<T>(_ request: DataStoreFetchRequest<T>) throws -> [PersistentIdentifier] where T : PersistentModel
```
