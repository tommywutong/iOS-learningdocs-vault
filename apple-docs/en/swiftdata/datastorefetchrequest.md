---
title: DataStoreFetchRequest
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastorefetchrequest
source_url: 'https://developer.apple.com/documentation/swiftdata/datastorefetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastorefetchrequest.json'
content_hash: 'sha256:4c5626b487ed8663'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreFetchRequest

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DataStoreFetchRequest<T> where T : PersistentModel
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [descriptor](datastorefetchrequest/descriptor.md)
- [editingState](datastorefetchrequest/editingstate.md)

## See Also

### Processing fetch requests

- [fetch(_:)](<datastore/fetch(__).md>)
- [DataStoreFetchResult](datastorefetchresult.md)
- [Snapshot](datastore/snapshot.md)
- [DataStoreSnapshot](datastoresnapshot.md)
- [DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [fetchCount(_:)](<datastore/fetchcount(__).md>)
- [fetchIdentifiers(_:)](<datastore/fetchidentifiers(__).md>)
