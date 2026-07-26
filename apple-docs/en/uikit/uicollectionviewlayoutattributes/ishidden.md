---
title: isHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/ishidden
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/ishidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/ishidden.json'
content_hash: 'sha256:b29c3920dcc3f0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# isHidden

<sub>Instance Property</sub>

Determines whether the item is currently displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHidden: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). As an optimization, the collection view might not create the corresponding view if this property is set to [true](../../swift/true.md).

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [bounds](bounds.md) — The bounds of the item.
- [center](center.md) — The center point of the item.
- [size](size.md) — The size of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
