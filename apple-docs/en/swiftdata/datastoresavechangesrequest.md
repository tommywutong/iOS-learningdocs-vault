---
title: DataStoreSaveChangesRequest
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastoresavechangesrequest
source_url: 'https://developer.apple.com/documentation/swiftdata/datastoresavechangesrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastoresavechangesrequest.json'
content_hash: 'sha256:1646b0acafbb9fa1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreSaveChangesRequest

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DataStoreSaveChangesRequest<SnapshotType> where SnapshotType : DataStoreSnapshot
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [deleted](datastoresavechangesrequest/deleted.md)
- [editingState](datastoresavechangesrequest/editingstate.md)
- [inserted](datastoresavechangesrequest/inserted.md)
- [updated](datastoresavechangesrequest/updated.md)

## See Also

### Persisting model data

- [save(_:)](<datastore/save(__).md>)
- [DataStoreSaveChangesResult](datastoresavechangesresult.md)
