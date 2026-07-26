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
doc_path: /documentation/coredata/nspropertydescription/name
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/name.json'
content_hash: 'sha256:eb1053a986d57e60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# name

<sub>Instance Property</sub>

The name of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String { get set }
```

## Discussion

A property name cannot be the same as any no-parameter method name of `NSObject` or `NSManagedObject`. Since there are hundreds of methods on `NSObject` which may conflict with property names, you should avoid very general words (like “font”, and “color”) and words or phrases that overlap with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

### Special Considerations

Setting the name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property

- [entity](entity.md) — The entity description of the receiver.
- [indexed](isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [optional](isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [transient](istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
