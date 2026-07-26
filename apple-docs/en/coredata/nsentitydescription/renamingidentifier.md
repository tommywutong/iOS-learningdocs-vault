---
title: renamingIdentifier
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/renamingidentifier
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/renamingidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/renamingidentifier.json'
content_hash: 'sha256:ba925327ccc5883c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# renamingIdentifier

<sub>Instance Property</sub>

The renaming identifier for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renamingIdentifier: String? { get set }
```

## Discussion

The renaming identifier is used to resolve naming conflicts between models. When creating a mapping model between two managed object models, a source entity and a destination entity that share the same identifier indicate that an entity mapping should be configured to migrate from the source to the destination.

If you do not set this value, the identifier will return the entity’s name.

## See Also

### Getting descriptive information

- [name](name.md) — The entity name of the receiver.
- [managedObjectModel](managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [managedObjectClassName](managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [abstract](isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
