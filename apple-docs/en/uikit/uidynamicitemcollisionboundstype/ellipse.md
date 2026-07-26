---
title: UIDynamicItemCollisionBoundsType.ellipse
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitemcollisionboundstype/ellipse
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/ellipse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitemcollisionboundstype/ellipse.json'
content_hash: 'sha256:83e15f3b3fd51a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemCollisionBoundsType](../uidynamicitemcollisionboundstype.md)

# UIDynamicItemCollisionBoundsType.ellipse

<sub>Case</sub>

Elliptical collision bounds. The shape of the ellipse is determined by the width and height of the item’s [bounds](../uidynamicitem/bounds.md) property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case ellipse
```

## See Also

### Constants

- [UIDynamicItemCollisionBoundsTypeRectangle](rectangle.md) — Rectangular collision bounds.
- [UIDynamicItemCollisionBoundsTypePath](path.md) — Path-based collision bounds. For this type, the shape is a [UIBezierPath](../uibezierpath.md) object stored in the item’s [collisionBoundingPath](../uidynamicitem/collisionboundingpath.md) property. See the description of that property for information about how to configure the path itself.
