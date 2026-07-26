---
title: subentities
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/subentities
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/subentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/subentities.json'
content_hash: 'sha256:53789da8ec4f5fc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# subentities

<sub>Instance Property</sub>

An array containing the sub-entities of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subentities: [NSEntityDescription] { get set }
```

## Discussion

The sub-entities are instances of `NSEntityDescription`.

### Special Considerations

Setting the sub-entities raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Managing inheritance

- [subentitiesByName](subentitiesbyname.md) — A dictionary containing the receiver’s sub-entities.
- [superentity](superentity.md) — The super-entity of the receiver.
- [- isKindOfEntity:](<iskindof(entity_).md>) — Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.
