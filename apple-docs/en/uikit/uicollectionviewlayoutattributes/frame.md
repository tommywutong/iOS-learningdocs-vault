---
title: frame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/frame
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/frame'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/frame.json'
content_hash: 'sha256:a592f3df7226503b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# frame

<sub>Instance Property</sub>

The frame rectangle of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frame: CGRect { get set }
```

## Discussion

The frame rectangle is measured in points and specified in the coordinate system of the collection view. Setting the value of this property also sets the values of the [center](center.md) and [size](size.md) properties.

## See Also

### Accessing the layout attributes

- [bounds](bounds.md) — The bounds of the item.
- [center](center.md) — The center point of the item.
- [size](size.md) — The size of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
