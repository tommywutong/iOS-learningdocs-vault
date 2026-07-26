---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uiview/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/bounds.json'
content_hash: 'sha256:6acb300a7f9b1475'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# bounds

<sub>Instance Property</sub>

The bounds rectangle, which describes the view’s location and size in its own coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get set }
```

## Discussion

The default bounds origin is (0,0) and the size is the same as the size of the rectangle in the [frame](frame.md) property. Changing the size portion of this rectangle grows or shrinks the view relative to its center point. Changing the size also changes the size of the rectangle in the [frame](frame.md) property to match. The coordinates of the bounds rectangle are always specified in points.

Changing the bounds rectangle automatically redisplays the view without calling its [- drawRect:](<draw(__).md>) method. If you want UIKit to call the [- drawRect:](<draw(__).md>) method, set the [contentMode](contentmode-swift.property.md) property to [UIViewContentModeRedraw](contentmode-swift.enum/redraw.md).

Changes to this property can be animated.

## See Also

### Configuring the bounds and frame rectangles

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [center](center.md) — The center point of the view’s frame rectangle.
- [transform](transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [transform3D](transform3d.md) — The three-dimensional transform to apply to the view.
- [anchorPoint](anchorpoint.md) — The anchor point of the view’s bounds rectangle.
