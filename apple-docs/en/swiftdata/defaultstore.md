---
title: DefaultStore
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/defaultstore
source_url: 'https://developer.apple.com/documentation/swiftdata/defaultstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/defaultstore.json'
content_hash: 'sha256:bb482d510de6dc0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DefaultStore

<sub>Class</sub>

A data store that uses Core Data as its undelying storage mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class DefaultStore
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [DataStore](datastore.md), [DataStoreBatching](datastorebatching.md), [Escapable](../swift/escapable.md), [HistoryProviding](historyproviding.md)

## Topics

### Accessing store information

- [name](defaultstore/name.md)

### Processing fetch requests

- [DefaultSnapshot](defaultsnapshot.md)

### Managing model change history

- [TokenType](defaultstore/tokentype.md)

## See Also

### Model storage

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DataStore](datastore.md) — An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [DataStoreBatching](datastorebatching.md) — An interface that enables a custom data store to support batch requests.
- [HistoryProviding](historyproviding.md) — An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
- [ModelDocument](modeldocument.md) — A document type that uses SwiftData to manage its storage.
