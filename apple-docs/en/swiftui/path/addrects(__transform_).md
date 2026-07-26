---
title: 'addRects(_:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/addrects(_:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/addrects(_:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/addrects%28_%3Atransform%3A%29.json'
content_hash: 'sha256:a2f3e6a801778d8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# addRects(_:transform:)

<sub>Instance Method</sub>

Adds a set of rectangular subpaths to the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addRects(_ rects: [CGRect], transform: CGAffineTransform = .identity)
```

## Discussion

Calling this convenience method is equivalent to repeatedly calling the `addRect(_:transform:)` method for each rectangle in the array.

- Parameter:

    - rects: An array of rectangles, specified in user space coordinates.
    - transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

### Drawing a path

- [move(to:)](<move(to_).md>) — Begins a new subpath at the specified point.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](<addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addEllipse(in:transform:)](<addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle to the path.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(_:)](<addlines(__).md>) — Adds a sequence of connected straight-line segments to the path.
- [addPath(_:transform:)](<addpath(__transform_).md>) — Appends another path value to this path.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addRoundedRect(in:cornerSize:style:transform:)](<addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [closeSubpath()](<closesubpath().md>) — Closes and completes the current subpath.
