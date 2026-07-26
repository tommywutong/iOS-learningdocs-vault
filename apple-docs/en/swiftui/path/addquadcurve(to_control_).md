---
title: 'addQuadCurve(to:control:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/addquadcurve(to:control:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/addquadcurve(to:control:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/addquadcurve%28to%3Acontrol%3A%29.json'
content_hash: 'sha256:d6c3f544690e53c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# addQuadCurve(to:control:)

<sub>Instance Method</sub>

Adds a quadratic Bézier curve to the path, with the specified end point and control point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addQuadCurve(to end: CGPoint, control: CGPoint)
```

## Parameters

- `control` — The control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and ending at the specified end point, with curvature defined by the control point. After this method appends that curve to the current path, the end point of the curve becomes the path’s current point.

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
- [addRect(_:transform:)](<addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addRoundedRect(in:cornerSize:style:transform:)](<addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [closeSubpath()](<closesubpath().md>) — Closes and completes the current subpath.
