---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/entity
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/entity.json'
content_hash: 'sha256:af2f648f6e9e336a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# entity

<sub>Instance Property</sub>

The entity description of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var entity: NSEntityDescription { get }
```

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [properties](../nsentitydescription/properties.md) — An array containing the properties of the receiver.

### Accessing Features of a Property

- [indexed](isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [optional](isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [transient](istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [name](name.md) — The name of the receiver.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
