---
title: predicate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequest/predicate
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest/predicate.json'
content_hash: 'sha256:7cb352a26e7a0e70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateRequest](../nsbatchupdaterequest.md)

# predicate

<sub>Instance Property</sub>

A predicate that identifies the objects to update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var predicate: NSPredicate? { get set }
```

## See Also

### Configuring a Request

- [entity](entity.md) — The managed entity to update data for.
- [entityName](entityname.md) — The name of the managed entity to update data for.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether to update subentities.
- [propertiesToUpdate](propertiestoupdate.md) — A dictionary of property description pairs that describe the updates.
- [resultType](resulttype.md) — The type of result that Core Data returns from the request.
