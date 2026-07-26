---
title: transform3D
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/transform3d
source_url: 'https://developer.apple.com/documentation/uikit/uiview/transform3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/transform3d.json'
content_hash: 'sha256:4c711e85ab867a0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# transform3D

<sub>Instance Property</sub>

The three-dimensional transform to apply to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transform3D: CATransform3D { get set }
```

## Discussion

The default value of this property is [CATransform3DIdentity](../../quartzcore/catransform3didentity.md).

## See Also

### Configuring the bounds and frame rectangles

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [center](center.md) — The center point of the view’s frame rectangle.
- [transform](transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [anchorPoint](anchorpoint.md) — The anchor point of the view’s bounds rectangle.
