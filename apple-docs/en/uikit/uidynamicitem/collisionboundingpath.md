---
title: collisionBoundingPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitem/collisionboundingpath
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitem/collisionboundingpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitem/collisionboundingpath.json'
content_hash: 'sha256:a77d6980ce5c8de0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItem](../uidynamicitem.md)

# collisionBoundingPath

<sub>Instance Property</sub>

The path-based shape to use for the collision bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var collisionBoundingPath: UIBezierPath { get }
```

## Discussion

When the [collisionBoundsType](collisionboundstype.md) property is [UIDynamicItemCollisionBoundsTypePath](../uidynamicitemcollisionboundstype/path.md), the object in this property is used as the collision bounds. If your dynamic item implements the [collisionBoundsType](collisionboundstype.md) property, you must also implement this property.

The path object you create must represent a convex polygon with counter-clockwise or clockwise winding, and the path must not intersect itself. The (0, 0) point of the path must be located at the [center](center.md) point of the corresponding dynamic item. If the center point does not match the path’s origin, collision behaviors may not work as expected.

## See Also

### Participating in dynamic animation

- [bounds](bounds.md) — Called when a dynamic animator needs the bounds of the dynamic item.
- [center](center.md) — The center point of the dynamic item.
- [transform](transform.md) — The rotation of the dynamic item.
- [collisionBoundsType](collisionboundstype.md) — The type of collision bounds associated with the item.
