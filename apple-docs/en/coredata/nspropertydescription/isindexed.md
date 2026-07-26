---
title: isIndexed
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（11.0 起废弃）, iPadOS 3.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspropertydescription/isindexed
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/isindexed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/isindexed.json'
content_hash: 'sha256:8b6d58124e0abaaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# isIndexed

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver should be indexed for searching.

> [!warning] Deprecated
> Use NSEntityDescription.indexes instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIndexed: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver should be indexed for searching, otherwise [false](../../swift/false.md). Object stores can optionally use this information upon store creation for operations such as defining indexes.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property

- [entity](entity.md) — The entity description of the receiver.
- [optional](isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [transient](istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [name](name.md) — The name of the receiver.
- [userInfo](userinfo.md) — The user info dictionary of the receiver.
