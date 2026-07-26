---
title: UIDynamicItemCollisionBoundsType.path
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitemcollisionboundstype/path
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitemcollisionboundstype/path.json'
content_hash: 'sha256:a3a2b0be37a1337a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemCollisionBoundsType](../uidynamicitemcollisionboundstype.md)

# UIDynamicItemCollisionBoundsType.path

<sub>Case</sub>

Path-based collision bounds. For this type, the shape is a [UIBezierPath](../uibezierpath.md) object stored in the item’s [collisionBoundingPath](../uidynamicitem/collisionboundingpath.md) property. See the description of that property for information about how to configure the path itself.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case path
```

## See Also

### Constants

- [UIDynamicItemCollisionBoundsTypeRectangle](rectangle.md) — Rectangular collision bounds.
- [UIDynamicItemCollisionBoundsTypeEllipse](ellipse.md) — Elliptical collision bounds. The shape of the ellipse is determined by the width and height of the item’s [bounds](../uidynamicitem/bounds.md) property.
