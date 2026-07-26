---
title: 'delete(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/datastorebatching/delete(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/datastorebatching/delete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/datastorebatching/delete%28_%3A%29.json'
content_hash: 'sha256:39fd488767455f36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [DataStoreBatching](../datastorebatching.md)

# delete(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delete<T>(_ request: DataStoreBatchDeleteRequest<T>) throws where T : PersistentModel
```

## See Also

### Deleting persisted model data

- [DataStoreBatchDeleteRequest](../datastorebatchdeleterequest.md)
