---
title: propertiesToUpdate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequest/propertiestoupdate
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/propertiestoupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest/propertiestoupdate.json'
content_hash: 'sha256:82d1788e65b745a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateRequest](../nsbatchupdaterequest.md)

# propertiesToUpdate

<sub>Instance Property</sub>

A dictionary of property description pairs that describe the updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propertiesToUpdate: [AnyHashable : Any]? { get set }
```

## Discussion

The dictionary keys are either [NSPropertyDescription](../nspropertydescription.md) objects or strings that identify the property name.

The dictionary values are either a constant value or an [NSExpression](../../foundation/nsexpression.md) that evaluates to a scalar value.

## See Also

### Configuring a Request

- [entity](entity.md) — The managed entity to update data for.
- [entityName](entityname.md) — The name of the managed entity to update data for.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether to update subentities.
- [predicate](predicate.md) — A predicate that identifies the objects to update.
- [resultType](resulttype.md) — The type of result that Core Data returns from the request.
