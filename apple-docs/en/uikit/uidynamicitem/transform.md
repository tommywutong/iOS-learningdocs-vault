---
title: transform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitem/transform
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitem/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitem/transform.json'
content_hash: 'sha256:772cc3c2947f0be9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItem](../uidynamicitem.md)

# transform

<sub>Instance Property</sub>

The rotation of the dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transform: CGAffineTransform { get set }
```

## Discussion

UIKit Dynamics makes use only of the rotation value in this property.

The dynamic animator (that the item is associated with) calls this method when it has computed a new rotation value for the item.

## See Also

### Participating in dynamic animation

- [bounds](bounds.md) — Called when a dynamic animator needs the bounds of the dynamic item.
- [center](center.md) — The center point of the dynamic item.
- [collisionBoundsType](collisionboundstype.md) — The type of collision bounds associated with the item.
- [collisionBoundingPath](collisionboundingpath.md) — The path-based shape to use for the collision bounds.
