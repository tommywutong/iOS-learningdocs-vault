---
title: isOptional
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/isoptional
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/isoptional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/isoptional.json'
content_hash: 'sha256:dccb2aa158ce835a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# isOptional

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is optional.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isOptional: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver is optional, otherwise [false](../../swift/false.md). The optionality flag specifies whether a property’s value can be `nil` before an object can be saved to a persistent store.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property

- [entity](entity.md) — The entity description of the receiver.
- [indexed](isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [transient](istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [name](name.md) — The name of the receiver.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
