---
title: 'addRoundedRect(in:cornerWidth:cornerHeight:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgmutablepath/addroundedrect(in:cornerwidth:cornerheight:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmutablepath/addroundedrect(in:cornerwidth:cornerheight:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmutablepath/addroundedrect%28in%3Acornerwidth%3Acornerheight%3Atransform%3A%29.json'
content_hash: 'sha256:c38d99303784443f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGMutablePath](../cgmutablepath.md)

# addRoundedRect(in:cornerWidth:cornerHeight:transform:)

<sub>Instance Method</sub>

Adds a subpath to the path, in the shape of a rectangle with rounded corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addRoundedRect(in rect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform = .identity)
```

## Parameters

- `rect` — The rectangle to add, specified in user space coordinates.

- `cornerWidth` — The horizontal size, in user space coordinates, for rounded corner sections.

- `cornerHeight` — The vertical size, in user space coordinates, for rounded corner sections.

- `transform` — An affine transform to apply to the rectangle before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This convenience method is equivalent to a move operation to start the subpath followed by a series of arc and line operations that construct the rounded rectangle. Each corner of the rounded rectangle is one-quarter of an ellipse with axes equal to the `cornerWidth` and `cornerHeight` parameters. The rounded rectangle forms a closed subpath oriented in the clockwise direction.

## See Also

### Constructing a Graphics Path

- [move(to:transform:)](<move(to_transform_).md>) — Begins a new subpath at the specified point.
- [addLine(to:transform:)](<addline(to_transform_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:transform:)](<addlines(between_transform_).md>) — Adds a sequence of connected straight-line segments to the path.
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addEllipse(in:transform:)](<addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](<addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addCurve(to:control1:control2:transform:)](<addcurve(to_control1_control2_transform_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addQuadCurve(to:control:transform:)](<addquadcurve(to_control_transform_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path object to the path.
- [CGPathCloseSubpath](<closesubpath().md>) — Closes and completes a subpath in a mutable graphics path.
