---
title: affectedStores
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorerequest/affectedstores
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorerequest/affectedstores'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorerequest/affectedstores.json'
content_hash: 'sha256:1302cc09ab680039'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreRequest](../nspersistentstorerequest.md)

# affectedStores

<sub>Instance Property</sub>

The stores the request should be sent to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var affectedStores: [NSPersistentStore]? { get set }
```

## Discussion

The array contains instances of [NSPersistentStore](../nspersistentstore.md).

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)

### Configuring a Request

- [requestType](requesttype.md) — The type of the fetch request.
- [NSPersistentStoreRequestType](../nspersistentstorerequesttype.md) — Constants that specify the types of fetch requests.
