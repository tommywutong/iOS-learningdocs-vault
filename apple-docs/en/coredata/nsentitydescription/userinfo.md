---
title: userInfo
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/userinfo
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/userinfo.json'
content_hash: 'sha256:58ee9fe4aec34b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# userInfo

<sub>Instance Property</sub>

The user info dictionary of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

Setting the user info dictionary raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Getting descriptive information

- [name](name.md) — The entity name of the receiver.
- [managedObjectModel](managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [managedObjectClassName](managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
- [abstract](isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [coreSpotlightDisplayNameExpression](corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.
