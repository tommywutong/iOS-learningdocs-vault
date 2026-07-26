---
title: DataStore
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastore
source_url: 'https://developer.apple.com/documentation/swiftdata/datastore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastore.json'
content_hash: 'sha256:39c3e2844ce95dff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStore

<sub>Protocol</sub>

An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DataStore : AnyObject
```

## Relationships

- **Inherited By**: [DataStoreBatching](datastorebatching.md)

- **Conforming Types**: [DefaultStore](defaultstore.md)

## Topics

### Creating a data store

- [init(_:migrationPlan:)](<datastore/init(__migrationplan_).md>)

### Accessing store information

- [configuration](datastore/configuration-swift.property.md)
- [Configuration](datastore/configuration-swift.associatedtype.md)
- [DataStoreConfiguration](datastoreconfiguration.md)
- [identifier](datastore/identifier.md)
- [schema](datastore/schema.md)

### Processing fetch requests

- [fetch(_:)](<datastore/fetch(__).md>)
- [DataStoreFetchRequest](datastorefetchrequest.md)
- [DataStoreFetchResult](datastorefetchresult.md)
- [Snapshot](datastore/snapshot.md)
- [DataStoreSnapshot](datastoresnapshot.md)
- [DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [fetchCount(_:)](<datastore/fetchcount(__).md>)
- [fetchIdentifiers(_:)](<datastore/fetchidentifiers(__).md>)

### Persisting model data

- [save(_:)](<datastore/save(__).md>)
- [DataStoreSaveChangesRequest](datastoresavechangesrequest.md)
- [DataStoreSaveChangesResult](datastoresavechangesresult.md)

### Removing all persisted model data

- [erase()](<datastore/erase().md>)

### Sharing cached data between model contexts

- [initializeState(for:)](<datastore/initializestate(for_).md>)
- [EditingState](editingstate.md)
- [cachedSnapshots(for:editingState:)](<datastore/cachedsnapshots(for_editingstate_).md>)
- [invalidateState(for:)](<datastore/invalidatestate(for_).md>)

## See Also

### Model storage

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DefaultStore](defaultstore.md) — A data store that uses Core Data as its undelying storage mechanism.
- [DataStoreBatching](datastorebatching.md) — An interface that enables a custom data store to support batch requests.
- [HistoryProviding](historyproviding.md) — An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
- [ModelDocument](modeldocument.md) — A document type that uses SwiftData to manage its storage.
