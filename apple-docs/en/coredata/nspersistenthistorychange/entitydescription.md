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
doc_path: /documentation/coredata/nspersistenthistorychange/entitydescription
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange/entitydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange/entitydescription.json'
content_hash: 'sha256:9f715fd77c5b66ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChange](../nspersistenthistorychange.md)

# entityDescription

<sub>Type Property</sub>

The entity description of the persistent history change entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var entityDescription: NSEntityDescription? { get }
```

## Discussion

The entity description of a [NSPersistentHistoryChange](../nspersistenthistorychange.md), includes its properties, which can be useful for filtering your persistent history change request.

## See Also

### Inspecting Change Metadata

- [fetchRequest](fetchrequest.md) — A fetch request that has the persistent history change as the entity.
- [+ entityDescriptionWithContext:](<entitydescription(with_).md>) — Requests an entity description for the managed object type affected by the change using the provided context.
