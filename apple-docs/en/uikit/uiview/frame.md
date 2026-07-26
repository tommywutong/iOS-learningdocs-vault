---
title: frame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/frame
source_url: 'https://developer.apple.com/documentation/uikit/uiview/frame'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/frame.json'
content_hash: 'sha256:fd5644b855366fcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# frame

<sub>Instance Property</sub>

The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frame: CGRect { get set }
```

## Discussion

This rectangle defines the size and position of the view in its superview’s coordinate system. Use this rectangle during layout operations to set the size and position the view. Setting this property changes the point specified by the [center](center.md) property and changes the size in the [bounds](bounds.md) rectangle accordingly. The coordinates of the frame rectangle are always specified in points.

> [!warning] Warning
> If the [transform](transform.md) property is not the identity transform, the value of this property is undefined and therefore should be ignored.

Changing the frame rectangle automatically redisplays the view without calling its [- drawRect:](<draw(__).md>) method. If you want UIKit to call the [- drawRect:](<draw(__).md>) method when the frame rectangle changes, set the [contentMode](contentmode-swift.property.md) property to [UIViewContentModeRedraw](contentmode-swift.enum/redraw.md).

Changes to this property can be animated. However, if the [transform](transform.md) property contains a non-identity transform, the value of the [frame](frame.md) property is undefined and should not be modified. In that case, reposition the view using the [center](center.md) property and adjust the size using the [bounds](bounds.md) property instead.

## See Also

### Configuring the bounds and frame rectangles

- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [center](center.md) — The center point of the view’s frame rectangle.
- [transform](transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [transform3D](transform3d.md) — The three-dimensional transform to apply to the view.
- [anchorPoint](anchorpoint.md) — The anchor point of the view’s bounds rectangle.
