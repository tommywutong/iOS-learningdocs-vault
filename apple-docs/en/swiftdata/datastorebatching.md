---
title: DataStoreBatching
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastorebatching
source_url: 'https://developer.apple.com/documentation/swiftdata/datastorebatching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastorebatching.json'
content_hash: 'sha256:427d66f4e5a5e64b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreBatching

<sub>Protocol</sub>

An interface that enables a custom data store to support batch requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DataStoreBatching : DataStore
```

## Relationships

- **Inherits From**: [DataStore](datastore.md)

- **Conforming Types**: [DefaultStore](defaultstore.md)

## Topics

### Deleting persisted model data

- [delete(_:)](<datastorebatching/delete(__).md>)
- [DataStoreBatchDeleteRequest](datastorebatchdeleterequest.md)

## See Also

### Model storage

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DefaultStore](defaultstore.md) — A data store that uses Core Data as its undelying storage mechanism.
- [DataStore](datastore.md) — An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [HistoryProviding](historyproviding.md) — An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
- [ModelDocument](modeldocument.md) — A document type that uses SwiftData to manage its storage.
