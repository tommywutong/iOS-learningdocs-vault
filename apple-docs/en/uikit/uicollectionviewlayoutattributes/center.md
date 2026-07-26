---
title: center
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/center
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/center.json'
content_hash: 'sha256:e9d2b02ab0bd3f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# center

<sub>Instance Property</sub>

The center point of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var center: CGPoint { get set }
```

## Discussion

The center point is specified in the coordinate system of the collection view. Setting the value of this property also updates the origin of the rectangle in the [frame](frame.md) property.

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [bounds](bounds.md) — The bounds of the item.
- [size](size.md) — The size of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
