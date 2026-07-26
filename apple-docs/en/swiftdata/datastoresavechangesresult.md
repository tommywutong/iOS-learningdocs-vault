---
title: DataStoreSaveChangesResult
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/datastoresavechangesresult
source_url: 'https://developer.apple.com/documentation/swiftdata/datastoresavechangesresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastoresavechangesresult.json'
content_hash: 'sha256:5a1c5c350056482f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# DataStoreSaveChangesResult

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class DataStoreSaveChangesResult<T> where T : DataStoreSnapshot
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(for:remappedIdentifiers:snapshotsToReregister:)](<datastoresavechangesresult/init(for_remappedidentifiers_snapshotstoreregister_).md>)
- [init(for:remappedIdentifiers:snapshotsToReregister:historyToken:)](<datastoresavechangesresult/init(for_remappedidentifiers_snapshotstoreregister_historytoken_).md>)

### Instance Properties

- [historyToken](datastoresavechangesresult/historytoken.md)
- [remappedIdentifiers](datastoresavechangesresult/remappedidentifiers.md)
- [snapshotsToReregister](datastoresavechangesresult/snapshotstoreregister.md)
- [storeIdentifier](datastoresavechangesresult/storeidentifier.md)

## See Also

### Persisting model data

- [save(_:)](<datastore/save(__).md>)
- [DataStoreSaveChangesRequest](datastoresavechangesrequest.md)
