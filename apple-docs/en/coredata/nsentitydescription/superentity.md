---
title: superentity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/superentity
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/superentity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/superentity.json'
content_hash: 'sha256:09a9b19b1d6f2cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# superentity

<sub>Instance Property</sub>

The super-entity of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var superentity: NSEntityDescription? { get }
```

## Discussion

If the receiver has no super-entity, returns `nil`.

## See Also

### Managing inheritance

- [subentitiesByName](subentitiesbyname.md) — A dictionary containing the receiver’s sub-entities.
- [subentities](subentities.md) — An array containing the sub-entities of the receiver.
- [- isKindOfEntity:](<iskindof(entity_).md>) — Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.
