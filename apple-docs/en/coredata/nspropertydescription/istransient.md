---
title: isTransient
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/istransient
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/istransient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/istransient.json'
content_hash: 'sha256:97af98aa5a8f250a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# isTransient

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is transient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isTransient: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver is transient, otherwise [false](../../swift/false.md). The transient flag specifies whether or not a property’s value is ignored when an object is saved to a persistent store. Transient properties are not saved to the persistent store, but are still managed for undo, redo, validation, and so on.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property

- [entity](entity.md) — The entity description of the receiver.
- [indexed](isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [optional](isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [name](name.md) — The name of the receiver.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
