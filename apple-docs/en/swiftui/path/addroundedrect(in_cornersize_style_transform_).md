---
title: 'addRoundedRect(in:cornerSize:style:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/addroundedrect(in:cornersize:style:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/addroundedrect(in:cornersize:style:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/addroundedrect%28in%3Acornersize%3Astyle%3Atransform%3A%29.json'
content_hash: 'sha256:38262b91f7625867'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# addRoundedRect(in:cornerSize:style:transform:)

<sub>Instance Method</sub>

Adds a rounded rectangle to the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addRoundedRect(in rect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle = .continuous, transform: CGAffineTransform = .identity)
```

## Parameters

- `rect` — A rectangle, specified in user space coordinates.

- `cornerSize` — The size of the corners, specified in user space coordinates.

- `style` — The corner style. Defaults to the `continous` style if not specified.

- `transform` — An affine transform to apply to the rectangle before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path, starting by moving to the center of the right edge and then adding lines and curves counter-clockwise to create a rounded rectangle, closing the subpath.

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
- [addRects(_:transform:)](<addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [closeSubpath()](<closesubpath().md>) — Closes and completes the current subpath.
