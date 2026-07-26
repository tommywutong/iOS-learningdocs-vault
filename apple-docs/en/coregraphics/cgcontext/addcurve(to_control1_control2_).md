---
title: 'addCurve(to:control1:control2:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/addcurve(to:control1:control2:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/addcurve(to:control1:control2:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/addcurve%28to%3Acontrol1%3Acontrol2%3A%29.json'
content_hash: 'sha256:1cdfb9bd7661602e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addCurve(to:control1:control2:)

<sub>Instance Method</sub>

Adds a cubic Bézier curve to the current path, with the specified end point and control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addCurve(to end: CGPoint, control1: CGPoint, control2: CGPoint)
```

## Parameters

- `end` — The point, in user space coordinates, at which to end the curve.

- `control1` — The first control point of the curve, in user space coordinates.

- `control2` — The second control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and ending at the specified end point, with curvature defined by the two control points. After this method appends that curve to the current path, the end point of the curve becomes the path’s current point.

## See Also

### Constructing a Current Graphics Path

- [CGContextBeginPath](<beginpath().md>) — Creates a new empty path in a graphics context.
- [move(to:)](<move(to_).md>) — Begins a new subpath at the specified point.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:)](<addlines(between_).md>) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<addrect(__).md>) — Adds a rectangular path to the current path.
- [addRects(_:)](<addrects(__).md>) — Adds a set of rectangular paths to the current path.
- [CGContextAddEllipseInRect](<addellipse(in_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addArc(center:radius:startAngle:endAngle:clockwise:)](<addarc(center_radius_startangle_endangle_clockwise_).md>) — Adds an arc of a circle to the current path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:)](<addarc(tangent1end_tangent2end_radius_).md>) — Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
