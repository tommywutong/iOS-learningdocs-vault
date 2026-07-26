---
title: 'move(to:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/move(to:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/move(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/move%28to%3A%29.json'
content_hash: 'sha256:01263979c6c72125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# move(to:)

<sub>Instance Method</sub>

Begins a new subpath at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func move(to point: CGPoint)
```

## Parameters

- `point` — The point, in user space coordinates, at which to start a new subpath.

## Discussion

The specified point becomes the start point of a new subpath. The current point is set to this start point.

## See Also

### Constructing a Current Graphics Path

- [CGContextBeginPath](<beginpath().md>) — Creates a new empty path in a graphics context.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:)](<addlines(between_).md>) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<addrect(__).md>) — Adds a rectangular path to the current path.
- [addRects(_:)](<addrects(__).md>) — Adds a set of rectangular paths to the current path.
- [CGContextAddEllipseInRect](<addellipse(in_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addArc(center:radius:startAngle:endAngle:clockwise:)](<addarc(center_radius_startangle_endangle_clockwise_).md>) — Adds an arc of a circle to the current path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:)](<addarc(tangent1end_tangent2end_radius_).md>) — Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
