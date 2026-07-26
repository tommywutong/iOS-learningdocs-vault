---
title: 'addRelativeArc(center:radius:startAngle:delta:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgmutablepath/addrelativearc(center:radius:startangle:delta:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmutablepath/addrelativearc(center:radius:startangle:delta:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmutablepath/addrelativearc%28center%3Aradius%3Astartangle%3Adelta%3Atransform%3A%29.json'
content_hash: 'sha256:c2b50fda95109228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGMutablePath](../cgmutablepath.md)

# addRelativeArc(center:radius:startAngle:delta:transform:)

<sub>Instance Method</sub>

Adds an arc of a circle to the path, specified with a radius and a difference in angle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform = .identity)
```

## Parameters

- `center` — The center of the arc, in user space coordinates.

- `radius` — The radius of the arc, in user space coordinates.

- `startAngle` — The angle to the starting point of the arc, measured in radians from the positive x-axis.

- `delta` — The difference, measured in radians, between the starting angle and ending angle of the arc. A positive value creates a counter-clockwise arc (in user space coordinates), and vice versa.

- `transform` — An affine transform to apply to the arc before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This method calculates starting and ending points using the radius and angles you specify, uses a sequence of cubic Bézier curves to approximate a segment of a circle between those points, and then appends those curves to the path.

The `delta` parameter determines both the length of the arc the direction in which the arc is created; the actual direction of the final path is dependent on the transform parameter and the current transform of a context where the path is drawn. In a flipped coordinate system (the default for UIView drawing methods in iOS), specifying a clockwise arc results in a counterclockwise arc after the transformation is applied.

If the path already contains a subpath, this method adds a line connecting the current point to the starting point of the arc. If the current path is empty, this method creates a new subpath whose starting point is the starting point of the arc. The ending point of the arc becomes the new current point of the path.

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
- [addArc(tangent1End:tangent2End:radius:transform:)](<addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:transform:)](<addcurve(to_control1_control2_transform_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addQuadCurve(to:control:transform:)](<addquadcurve(to_control_transform_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path object to the path.
- [CGPathCloseSubpath](<closesubpath().md>) — Closes and completes a subpath in a mutable graphics path.
