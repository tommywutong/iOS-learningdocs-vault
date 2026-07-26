---
title: includesSubentities
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequest/includessubentities
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/includessubentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest/includessubentities.json'
content_hash: 'sha256:724fb8bd4ec45043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateRequest](../nsbatchupdaterequest.md)

# includesSubentities

<sub>Instance Property</sub>

A Boolean value that indicates whether to update subentities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesSubentities: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md).

## See Also

### Configuring a Request

- [entity](entity.md) — The managed entity to update data for.
- [entityName](entityname.md) — The name of the managed entity to update data for.
- [predicate](predicate.md) — A predicate that identifies the objects to update.
- [propertiesToUpdate](propertiestoupdate.md) — A dictionary of property description pairs that describe the updates.
- [resultType](resulttype.md) — The type of result that Core Data returns from the request.
