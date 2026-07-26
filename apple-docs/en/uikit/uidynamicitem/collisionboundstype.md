---
title: collisionBoundsType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitem/collisionboundstype
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitem/collisionboundstype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitem/collisionboundstype.json'
content_hash: 'sha256:e92968fa0105d8c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItem](../uidynamicitem.md)

# collisionBoundsType

<sub>Instance Property</sub>

The type of collision bounds associated with the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var collisionBoundsType: UIDynamicItemCollisionBoundsType { get }
```

## Discussion

The dynamics system uses this property to determine how to evaluate collisions with the dynamic item. Rectangular and elliptical bounds are defined by the [bounds](bounds.md) property of the item. For custom collision bounds, the shape of the bounds are in the [collisionBoundingPath](collisionboundingpath.md) property.

If you implement this property in your dynamic item and set its value to [UIDynamicItemCollisionBoundsTypePath](../uidynamicitemcollisionboundstype/path.md), you must also implement the [collisionBoundingPath](collisionboundingpath.md) property and provide a valid path. Failure to do so is a programmer error.

The default value of this property is [UIDynamicItemCollisionBoundsTypeRectangle](../uidynamicitemcollisionboundstype/rectangle.md).

## See Also

### Participating in dynamic animation

- [bounds](bounds.md) — Called when a dynamic animator needs the bounds of the dynamic item.
- [center](center.md) — The center point of the dynamic item.
- [transform](transform.md) — The rotation of the dynamic item.
- [collisionBoundingPath](collisionboundingpath.md) — The path-based shape to use for the collision bounds.
