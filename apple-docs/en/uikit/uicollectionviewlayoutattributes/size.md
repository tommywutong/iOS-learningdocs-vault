---
title: size
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/size
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/size.json'
content_hash: 'sha256:33dd8186dd764ae6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# size

<sub>Instance Property</sub>

The size of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var size: CGSize { get set }
```

## Discussion

Setting the value of this property also changes the size of the rectangle returned by the [frame](frame.md) and [bounds](bounds.md) properties.

## See Also

### Accessing the layout attributes

- [frame](frame.md) — The frame rectangle of the item.
- [bounds](bounds.md) — The bounds of the item.
- [center](center.md) — The center point of the item.
- [transform3D](transform3d.md) — The 3D transform of the item.
- [transform](transform.md) — The affine transform of the item.
- [alpha](alpha.md) — The transparency of the item.
- [zIndex](zindex.md) — Specifies the item’s position on the z axis.
- [hidden](ishidden.md) — Determines whether the item is currently displayed.
