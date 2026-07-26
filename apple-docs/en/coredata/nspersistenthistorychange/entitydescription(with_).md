---
title: 'entityDescription(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistenthistorychange/entitydescription(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange/entitydescription(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange/entitydescription%28with%3A%29.json'
content_hash: 'sha256:f6e4e24f0009fac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChange](../nspersistenthistorychange.md)

# entityDescription(with:)

<sub>Type Method</sub>

Requests an entity description for the managed object type affected by the change using the provided context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func entityDescription(with context: NSManagedObjectContext) -> NSEntityDescription?
```

## Parameters

- `context` — The managed object context for this request.

## Return Value

The entity description ([NSEntityDescription](../nsentitydescription.md)) of the persistent history transaction entity.

## See Also

### Inspecting Change Metadata

- [fetchRequest](fetchrequest.md) — A fetch request that has the persistent history change as the entity.
- [entityDescription](entitydescription.md) — The entity description of the persistent history change entity.
