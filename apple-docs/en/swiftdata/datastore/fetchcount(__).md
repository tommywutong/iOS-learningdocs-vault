---
title: 'fetchCount(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/datastore/fetchcount(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/datastore/fetchcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastore/fetchcount%28_%3A%29.json'
content_hash: 'sha256:77176fa651254d9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [DataStore](../datastore.md)

# fetchCount(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchCount<T>(_ request: DataStoreFetchRequest<T>) throws -> Int where T : PersistentModel
```

## Default Implementations

### DataStore Implementations

- [fetchCount(_:)](<fetchcount(__)-91yf3.md>)

## See Also

### Processing fetch requests

- [fetch(_:)](<fetch(__).md>)
- [DataStoreFetchRequest](../datastorefetchrequest.md)
- [DataStoreFetchResult](../datastorefetchresult.md)
- [Snapshot](snapshot.md)
- [DataStoreSnapshot](../datastoresnapshot.md)
- [DataStoreSnapshotValue](../datastoresnapshotvalue.md)
- [fetchIdentifiers(_:)](<fetchidentifiers(__).md>)
