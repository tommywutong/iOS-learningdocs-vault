---
title: name
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/name
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/name.json'
content_hash: 'sha256:7197fcf2c983275a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# name

<sub>Instance Property</sub>

The entity name of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get set }
```

## Discussion

Setting the name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)

### Getting descriptive information

- [managedObjectModel](managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [managedObjectClassName](managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
- [abstract](isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
