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
doc_path: /documentation/coredata/nspropertydescription/userinfo
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/userinfo.json'
content_hash: 'sha256:55a24e76828fe95b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# userInfo

<sub>Instance Property</sub>

The user info dictionary of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

Setting the user info raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property

- [entity](entity.md) — The entity description of the receiver.
- [indexed](isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [optional](isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [transient](istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [name](name.md) — The name of the receiver.
