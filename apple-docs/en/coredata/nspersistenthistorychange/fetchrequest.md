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
doc_path: /documentation/coredata/nspersistenthistorychange/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychange/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychange/fetchrequest.json'
content_hash: 'sha256:85911defe355582a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChange](../nspersistenthistorychange.md)

# fetchRequest

<sub>Type Property</sub>

A fetch request that has the persistent history change as the entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get }
```

## See Also

### Inspecting Change Metadata

- [entityDescription](entitydescription.md) — The entity description of the persistent history change entity.
- [+ entityDescriptionWithContext:](<entitydescription(with_).md>) — Requests an entity description for the managed object type affected by the change using the provided context.
