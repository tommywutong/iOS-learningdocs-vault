---
title: center
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitem/center
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitem/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitem/center.json'
content_hash: 'sha256:66c37dbf6549d848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItem](../uidynamicitem.md)

# center

<sub>Instance Property</sub>

The center point of the dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var center: CGPoint { get set }
```

## Discussion

The dynamic animator (that the item is associated with) calls this method when it has computed a new center point for the item.

## See Also

### Participating in dynamic animation

- [bounds](bounds.md) — Called when a dynamic animator needs the bounds of the dynamic item.
- [transform](transform.md) — The rotation of the dynamic item.
- [collisionBoundsType](collisionboundstype.md) — The type of collision bounds associated with the item.
- [collisionBoundingPath](collisionboundingpath.md) — The path-based shape to use for the collision bounds.
