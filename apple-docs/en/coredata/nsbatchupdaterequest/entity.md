---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequest/entity
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest/entity.json'
content_hash: 'sha256:ef0a96350ad745be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateRequest](../nsbatchupdaterequest.md)

# entity

<sub>Instance Property</sub>

The managed entity to update data for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entity: NSEntityDescription { get }
```

## See Also

### Configuring a Request

- [entityName](entityname.md) — The name of the managed entity to update data for.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether to update subentities.
- [predicate](predicate.md) — A predicate that identifies the objects to update.
- [propertiesToUpdate](propertiestoupdate.md) — A dictionary of property description pairs that describe the updates.
- [resultType](resulttype.md) — The type of result that Core Data returns from the request.
