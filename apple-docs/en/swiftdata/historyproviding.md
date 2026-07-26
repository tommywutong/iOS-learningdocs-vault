---
title: HistoryProviding
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historyproviding
source_url: 'https://developer.apple.com/documentation/swiftdata/historyproviding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyproviding.json'
content_hash: 'sha256:4dd88ff9a0a523ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryProviding

<sub>Protocol</sub>

An interface that enables a custom data store to provide the history of changes for its persisted models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol HistoryProviding
```

## Relationships

- **Conforming Types**: [DefaultStore](defaultstore.md)

## Topics

### Processing history fetch requests

- [fetchHistory(_:)](<historyproviding/fetchhistory(__).md>)

### Deleting history

- [deleteHistory(_:)](<historyproviding/deletehistory(__).md>)

### Getting the history transaction type

- [HistoryType](historyproviding/historytype-swift.associatedtype.md)

### Type Properties

- [historyType](historyproviding/historytype-swift.type.property.md)

## See Also

### Model storage

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DefaultStore](defaultstore.md) — A data store that uses Core Data as its undelying storage mechanism.
- [DataStore](datastore.md) — An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [DataStoreBatching](datastorebatching.md) — An interface that enables a custom data store to support batch requests.
- [Building a document-based app using SwiftData](../swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
- [ModelDocument](modeldocument.md) — A document type that uses SwiftData to manage its storage.
