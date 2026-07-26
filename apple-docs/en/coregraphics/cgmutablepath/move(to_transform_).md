---
title: 'move(to:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgmutablepath/move(to:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmutablepath/move(to:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmutablepath/move%28to%3Atransform%3A%29.json'
content_hash: 'sha256:6eda1a40b1526651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGMutablePath](../cgmutablepath.md)

# move(to:transform:)

<sub>Instance Method</sub>

Begins a new subpath at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func move(to point: CGPoint, transform: CGAffineTransform = .identity)
```

## Parameters

- `point` — The point, in user space coordinates, at which to start a new subpath.

- `transform` — An affine transform to apply to the point before adding to the path. Defaults to the identity transform if not specified.

## Discussion

The specified point becomes the start point of a new subpath. The current point is set to this start point.

## See Also

### Constructing a Graphics Path

- [addLine(to:transform:)](<addline(to_transform_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:transform:)](<addlines(between_transform_).md>) — Adds a sequence of connected straight-line segments to the path.
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addEllipse(in:transform:)](<addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addRoundedRect(in:cornerWidth:cornerHeight:transform:)](<addroundedrect(in_cornerwidth_cornerheight_transform_).md>) — Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](<addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addCurve(to:control1:control2:transform:)](<addcurve(to_control1_control2_transform_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addQuadCurve(to:control:transform:)](<addquadcurve(to_control_transform_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path object to the path.
- [CGPathCloseSubpath](<closesubpath().md>) — Closes and completes a subpath in a mutable graphics path.
