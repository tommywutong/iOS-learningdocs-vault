---
title: isAbstract
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/isabstract
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/isabstract'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/isabstract.json'
content_hash: 'sha256:f81a9aefeb297126'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# isAbstract

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver represents an abstract entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isAbstract: Bool { get set }
```

## Return Value

[true](../../swift/true.md) if the receiver represents an abstract entity, otherwise [false](../../swift/false.md).

## Discussion

[true](../../swift/true.md) if the receiver represents an abstract entity, otherwise [false](../../swift/false.md). An abstract entity might be Shape, with concrete sub-entities such as Rectangle, Triangle, and Circle.

### Special Considerations

Setting whether an entity is abstract raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Getting descriptive information

- [name](name.md) — The entity name of the receiver.
- [managedObjectModel](managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [managedObjectClassName](managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
