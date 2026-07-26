---
title: anchorPoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/anchorpoint
source_url: 'https://developer.apple.com/documentation/uikit/uiview/anchorpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/anchorpoint.json'
content_hash: 'sha256:1df9f8e4a513e8df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# anchorPoint

<sub>Instance Property</sub>

The anchor point of the view’s bounds rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var anchorPoint: CGPoint { get set }
```

## Discussion

You specify the value for this property using the unit coordinate space, where (`0`, `0`) is the bottom-left corner of the view’s [bounds](../../quartzcore/calayer/bounds.md) rectangle, and (`1`, `1`) is the top-right corner. The default value of this property is (`0.5`, `0.5`), which represents the center of the view’s [bounds](../../quartzcore/calayer/bounds.md) rectangle.

All geometric manipulations to the view occur about the specified point. For example, applying a rotation transform to a view with the default anchor point causes the view to rotate around its center. Changing the anchor point to a different location causes the view to rotate around that new point.

## See Also

### Configuring the bounds and frame rectangles

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [center](center.md) — The center point of the view’s frame rectangle.
- [transform](transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [transform3D](transform3d.md) — The three-dimensional transform to apply to the view.
