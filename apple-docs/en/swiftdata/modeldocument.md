---
title: ModelDocument
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modeldocument
source_url: 'https://developer.apple.com/documentation/swiftdata/modeldocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modeldocument.json'
content_hash: 'sha256:03cc4451e13e27fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelDocument

<sub>Structure</sub>

A document type that uses SwiftData to manage its storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct ModelDocument
```

## Overview

> [!important] Important
> Don’t create instances of this type. Instead, use one of the initializers on [DocumentGroup](../swiftui/documentgroup.md).

## See Also

### Model storage

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DefaultStore](defaultstore.md) — A data store that uses Core Data as its undelying storage mechanism.
- [DataStore](datastore.md) — An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [DataStoreBatching](datastorebatching.md) — An interface that enables a custom data store to support batch requests.
- [HistoryProviding](historyproviding.md) — An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
