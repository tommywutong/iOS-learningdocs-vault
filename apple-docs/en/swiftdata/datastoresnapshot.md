---
title: DataStoreSnapshot
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastoresnapshot
source_url: 'https://developer.apple.com/documentation/swiftdata/datastoresnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastoresnapshot.json'
content_hash: 'sha256:4ae5561b69b5c863'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreSnapshot

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DataStoreSnapshot : Decodable, Encodable, Sendable
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DefaultSnapshot](defaultsnapshot.md)

## Topics

### Initializers

- [init(from:relatedBackingDatas:)](<datastoresnapshot/init(from_relatedbackingdatas_).md>)

### Instance Properties

- [persistentIdentifier](datastoresnapshot/persistentidentifier.md)

### Instance Methods

- [copy(persistentIdentifier:remappedIdentifiers:)](<datastoresnapshot/copy(persistentidentifier_remappedidentifiers_).md>)

## See Also

### Processing fetch requests

- [fetch(_:)](<datastore/fetch(__).md>)
- [DataStoreFetchRequest](datastorefetchrequest.md)
- [DataStoreFetchResult](datastorefetchresult.md)
- [Snapshot](datastore/snapshot.md)
- [DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [fetchCount(_:)](<datastore/fetchcount(__).md>)
- [fetchIdentifiers(_:)](<datastore/fetchidentifiers(__).md>)
