---
title: fetchRequest
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction/fetchrequest.json'
content_hash: 'sha256:609b0e2f495e56f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md)

# fetchRequest

<sub>Type Property</sub>

A fetch request that has the persistent history transaction as the entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get }
```

## See Also

### Customizing History Fetch Requests

- [entityDescription](entitydescription.md) — The entity description of the persistent history transaction entity.
- [+ entityDescriptionWithContext:](<entitydescription(with_).md>) — Requests an entity description using the provided context for the managed object type affected by the transaction.
