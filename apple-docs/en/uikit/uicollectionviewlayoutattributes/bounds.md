---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/bounds.json'
content_hash: 'sha256:83c63a591531057b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# bounds

<sub>Instance Property</sub>

The bounds of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get set }
```

## Discussion

When setting the bounds, the origin of the bounds rectangle must always be at (0, 0). Changing the bounds rectangle also changes the value in the [size](size.md) property to match the new bounds size.

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [center](center.md) — The center point of the item.
- [size](size.md) — The size of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
