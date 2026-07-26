---
title: managedObjectClassName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/managedobjectclassname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/managedobjectclassname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/managedobjectclassname.json'
content_hash: 'sha256:3831a01b6c244080'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# managedObjectClassName

<sub>Instance Property</sub>

The name of the class that represents the receiver’s entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var managedObjectClassName: String! { get set }
```

## Discussion

The class specified by `name` must [NSManagedObject](../nsmanagedobject.md) or a subclass of [NSManagedObject](../nsmanagedobject.md).

### Special Considerations

Setting the class name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Getting descriptive information

- [name](name.md) — The entity name of the receiver.
- [managedObjectModel](managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
- [abstract](isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
