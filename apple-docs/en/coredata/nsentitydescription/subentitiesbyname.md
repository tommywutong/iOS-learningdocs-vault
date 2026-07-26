---
title: subentitiesByName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/subentitiesbyname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/subentitiesbyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/subentitiesbyname.json'
content_hash: 'sha256:5b23794fd96fe84c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# subentitiesByName

<sub>Instance Property</sub>

A dictionary containing the receiver’s sub-entities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subentitiesByName: [String : NSEntityDescription] { get }
```

## Return Value

The keys in the dictionary are the sub-entity names, the corresponding values are instances of `NSEntityDescription`.

## See Also

### Managing inheritance

- [subentities](subentities.md) — An array containing the sub-entities of the receiver.
- [superentity](superentity.md) — The super-entity of the receiver.
- [- isKindOfEntity:](<iskindof(entity_).md>) — Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.
