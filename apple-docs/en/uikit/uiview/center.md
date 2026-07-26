---
title: center
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/center
source_url: 'https://developer.apple.com/documentation/uikit/uiview/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/center.json'
content_hash: 'sha256:f1621e3d9e1da878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# center

<sub>Instance Property</sub>

The center point of the view’s frame rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var center: CGPoint { get set }
```

## Discussion

The center point is specified in points in the coordinate system of its superview. Setting this property updates the origin of the rectangle in the [frame](frame.md) property appropriately.

Use this property, instead of the [frame](frame.md) property, when you want to change the position of a view. The center point is always valid, even when scaling or rotation factors are applied to the view’s transform.   Changes to this property can be animated.

## See Also

### Configuring the bounds and frame rectangles

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [transform](transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [transform3D](transform3d.md) — The three-dimensional transform to apply to the view.
- [anchorPoint](anchorpoint.md) — The anchor point of the view’s bounds rectangle.
