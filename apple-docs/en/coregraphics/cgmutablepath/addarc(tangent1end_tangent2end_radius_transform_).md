---
title: 'addArc(tangent1End:tangent2End:radius:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgmutablepath/addarc(tangent1end:tangent2end:radius:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmutablepath/addarc(tangent1end:tangent2end:radius:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmutablepath/addarc%28tangent1end%3Atangent2end%3Aradius%3Atransform%3A%29.json'
content_hash: 'sha256:a175427a44a1af50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGMutablePath](../cgmutablepath.md)

# addArc(tangent1End:tangent2End:radius:transform:)

<sub>Instance Method</sub>

Adds an arc of a circle to the path, specified with a radius and two tangent lines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform = .identity)
```

## Parameters

- `tangent1End` — The end point, in user space coordinates, for the first tangent line to be used in constructing the arc. (The start point for this tangent line is the path’s current point.)

- `tangent2End` — The end point, in user space coordinates, for the second tangent line to be used in constructing the arc. (The start point for this tangent line is the `tangent1End` point.)

- `radius` — The radius of the arc, in user space coordinates.

- `transform` — An affine transform to apply to the arc before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This method calculates two tangent lines—the first from the current point to the `tangent1End` point, and the second from the `tangent1End` point to the `tangent2End` point—then calculates the start and end points for a circular arc of the specified radius such that the arc is tangent to both lines. Finally, this method approximates that arc with a sequence of cubic Bézier curves and appends those curves to the path.

If the starting point of the arc (that is, the point where a circle of the specified radius must meet the first tangent line in order to also be tangent to the second line) is not the current point, this method appends a straight line segment from the current point to the starting point of the arc.

The ending point of the arc (that is, the point where a circle of the specified radius must meet the second tangent line in order to also be tangent to the first line) becomes the new current point of the path.

## See Also

### Constructing a Graphics Path

- [move(to:transform:)](<move(to_transform_).md>) — Begins a new subpath at the specified point.
- [addLine(to:transform:)](<addline(to_transform_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:transform:)](<addlines(between_transform_).md>) — Adds a sequence of connected straight-line segments to the path.
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addEllipse(in:transform:)](<addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addRoundedRect(in:cornerWidth:cornerHeight:transform:)](<addroundedrect(in_cornerwidth_cornerheight_transform_).md>) — Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addCurve(to:control1:control2:transform:)](<addcurve(to_control1_control2_transform_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addQuadCurve(to:control:transform:)](<addquadcurve(to_control_transform_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path object to the path.
- [CGPathCloseSubpath](<closesubpath().md>) — Closes and completes a subpath in a mutable graphics path.
