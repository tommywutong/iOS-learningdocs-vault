---
title: entityDescription
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction/entitydescription
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/entitydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction/entitydescription.json'
content_hash: 'sha256:c4e2e6a7de55b71f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md)

# entityDescription

<sub>Type Property</sub>

The entity description of the persistent history transaction entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var entityDescription: NSEntityDescription? { get }
```

## Discussion

The entity description of [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md) lists the properties of the persistent history change. This can be useful for filtering your request.

## See Also

### Customizing History Fetch Requests

- [fetchRequest](fetchrequest.md) — A fetch request that has the persistent history transaction as the entity.
- [+ entityDescriptionWithContext:](<entitydescription(with_).md>) — Requests an entity description using the provided context for the managed object type affected by the transaction.
