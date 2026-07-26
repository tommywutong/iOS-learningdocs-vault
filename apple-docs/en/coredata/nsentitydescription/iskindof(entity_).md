---
title: 'isKindOf(entity:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitydescription/iskindof(entity:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/iskindof(entity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/iskindof%28entity%3A%29.json'
content_hash: 'sha256:38520278aa7bf6cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# isKindOf(entity:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isKindOf(entity: NSEntityDescription) -> Bool
```

## Parameters

- `entity` — An entity.

## Return Value

[true](../../swift/true.md) if the receiver is a sub-entity of `entity`, otherwise [false](../../swift/false.md).

## See Also

### Managing inheritance

- [subentitiesByName](subentitiesbyname.md) — A dictionary containing the receiver’s sub-entities.
- [subentities](subentities.md) — An array containing the sub-entities of the receiver.
- [superentity](superentity.md) — The super-entity of the receiver.
