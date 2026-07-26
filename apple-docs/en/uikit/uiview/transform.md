---
title: transform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/transform
source_url: 'https://developer.apple.com/documentation/uikit/uiview/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/transform.json'
content_hash: 'sha256:5c45b2f6aca4b03d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# transform

<sub>Instance Property</sub>

Specifies the transform applied to the view, relative to the center of its bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transform: CGAffineTransform { get set }
```

## Discussion

Use this property to scale or rotate the view’s frame rectangle within its superview’s coordinate system. (To change the position of the view, modify the [center](center.md) property instead.) The default value of this property is `CGAffineTransformIdentity`.

Transformations occur relative to the view’s anchor point. By default, the anchor point is equal to the center point of the frame rectangle. To change the anchor point, modify the [anchorPoint](../../quartzcore/calayer/anchorpoint.md) property of the view’s underlying [CALayer](../../quartzcore/calayer.md) object.

Changes to this property can be animated.

In iOS 8.0 and later, the `transform` property does not affect Auto Layout. Auto layout calculates a view’s alignment rectangle based on its untransformed frame.

> [!warning] Warning
> When the value of this property is anything other than the identity transform, the value in the [frame](frame.md) property is undefined and should be ignored.

## See Also

### Configuring the bounds and frame rectangles

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [center](center.md) — The center point of the view’s frame rectangle.
- [transform3D](transform3d.md) — The three-dimensional transform to apply to the view.
- [anchorPoint](anchorpoint.md) — The anchor point of the view’s bounds rectangle.
