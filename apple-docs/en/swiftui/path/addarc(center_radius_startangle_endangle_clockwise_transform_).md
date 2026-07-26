---
title: 'addArc(center:radius:startAngle:endAngle:clockwise:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/addarc(center:radius:startangle:endangle:clockwise:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/addarc(center:radius:startangle:endangle:clockwise:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/addarc%28center%3Aradius%3Astartangle%3Aendangle%3Aclockwise%3Atransform%3A%29.json'
content_hash: 'sha256:e69abafc27eb4425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# addArc(center:radius:startAngle:endAngle:clockwise:transform:)

<sub>Instance Method</sub>

Adds an arc of a circle to the path, specified with a radius and angles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle: Angle, clockwise: Bool, transform: CGAffineTransform = .identity)
```

## Parameters

- `center` — The center of the arc, in user space coordinates.

- `radius` — The radius of the arc, in user space coordinates.

- `startAngle` — The angle to the starting point of the arc, measured from the positive x-axis.

- `endAngle` — The angle to the end point of the arc, measured from the positive x-axis.

- `clockwise` — True to make a clockwise arc; false to make a counterclockwise arc.

- `transform` — An affine transform to apply to the arc before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This method calculates starting and ending points using the radius and angles you specify, uses a sequence of cubic Bézier curves to approximate a segment of a circle between those points, and then appends those curves to the path.

The `clockwise` parameter determines the direction in which the arc is created; the actual direction of the final path is dependent on the `transform` parameter and the current transform of a context where the path is drawn. However, because SwiftUI by default uses a vertically-flipped coordinate system (with the origin in the top-left of the view), specifying a clockwise arc results in a counterclockwise arc after the transformation is applied.

If the path ends with an unclosed subpath, this method adds a line connecting the current point to the starting point of the arc. If there is no unclosed subpath, this method creates a new subpath whose starting point is the starting point of the arc. The ending point of the arc becomes the new current point of the path.

## See Also

### Drawing a path

- [move(to:)](<move(to_).md>) — Begins a new subpath at the specified point.
- [addArc(tangent1End:tangent2End:radius:transform:)](<addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addEllipse(in:transform:)](<addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle to the path.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(_:)](<addlines(__).md>) — Adds a sequence of connected straight-line segments to the path.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path value to this path.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addRoundedRect(in:cornerSize:style:transform:)](<addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [closeSubpath()](<closesubpath().md>) — Closes and completes the current subpath.
