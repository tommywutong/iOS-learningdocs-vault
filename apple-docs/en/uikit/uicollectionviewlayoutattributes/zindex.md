---
title: zIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/zindex
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/zindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/zindex.json'
content_hash: 'sha256:d267b5516eae49d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# zIndex

<sub>Instance Property</sub>

Specifies the item’s position on the z axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var zIndex: Int { get set }
```

## Discussion

This property is used to determine the front-to-back ordering of items during layout. Items with higher index values appear on top of items with lower values. Items with the same value have an undetermined order.

The default value of this property is 0.

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [bounds](bounds.md) — The bounds of the item.
- [center](center.md) — The center point of the item.
- [size](size.md) — The size of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
