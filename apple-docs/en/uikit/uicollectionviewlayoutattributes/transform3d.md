---
title: transform3D
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/transform3d
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/transform3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/transform3d.json'
content_hash: 'sha256:71da51893ea26c52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# transform3D

<sub>Instance Property</sub>

The 3D transform of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transform3D: CATransform3D { get set }
```

## Discussion

Assigning a value to this property replaces the value in the [transform](transform.md) property with an affine version of the 3D transform you specify.

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [bounds](bounds.md) — The bounds of the item.
- [center](center.md) — The center point of the item.
- [size](size.md) — The size of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
