---
title: managedObjectModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/managedobjectmodel
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/managedobjectmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/managedobjectmodel.json'
content_hash: 'sha256:ef72186f72828951'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# managedObjectModel

<sub>Instance Property</sub>

The managed object model with which the receiver is associated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }
```

## See Also

### Related Documentation

- [- setEntities:forConfiguration:](<../nsmanagedobjectmodel/setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.
- [entities](../nsmanagedobjectmodel/entities.md) — The entities in the model.

### Getting descriptive information

- [name](name.md) — The entity name of the receiver.
- [managedObjectClassName](managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
- [abstract](isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
