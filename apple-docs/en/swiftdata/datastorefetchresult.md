---
title: DataStoreFetchResult
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastorefetchresult
source_url: 'https://developer.apple.com/documentation/swiftdata/datastorefetchresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastorefetchresult.json'
content_hash: 'sha256:0f6ee7da216254b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreFetchResult

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DataStoreFetchResult<ModelType, SnapshotType> where ModelType : PersistentModel, SnapshotType : DataStoreSnapshot
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(descriptor:fetchedSnapshots:relatedSnapshots:)](<datastorefetchresult/init(descriptor_fetchedsnapshots_relatedsnapshots_).md>)

### Instance Properties

- [descriptor](datastorefetchresult/descriptor.md)
- [fetchedSnapshots](datastorefetchresult/fetchedsnapshots.md)
- [relatedSnapshots](datastorefetchresult/relatedsnapshots.md)

## See Also

### Processing fetch requests

- [fetch(_:)](<datastore/fetch(__).md>)
- [DataStoreFetchRequest](datastorefetchrequest.md)
- [Snapshot](datastore/snapshot.md)
- [DataStoreSnapshot](datastoresnapshot.md)
- [DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [fetchCount(_:)](<datastore/fetchcount(__).md>)
- [fetchIdentifiers(_:)](<datastore/fetchidentifiers(__).md>)
