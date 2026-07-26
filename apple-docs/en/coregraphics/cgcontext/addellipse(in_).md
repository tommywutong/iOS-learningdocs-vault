---
title: 'addEllipse(in:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/addellipse(in:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/addellipse(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/addellipse%28in%3A%29.json'
content_hash: 'sha256:bc3398831f635f74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addEllipse(in:)

<sub>Instance Method</sub>

Adds an ellipse that fits inside the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addEllipse(in rect: CGRect)
```

## Parameters

- `rect` — A rectangle that defines the area for the ellipse to fit in.

## Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the midpoint of the rectangle defined by the `rect` parameter. If the rectangle is square, then the ellipse is circular with a radius equal to one-half the width (or height) of the rectangle. If the `rect` parameter specifies a rectangular shape, then the major and minor axes of the ellipse are defined by the width and height of the rectangle.

The ellipse forms a complete subpath of the path—that is, the ellipse drawing starts with a move-to operation and ends with a close-subpath operation, with all moves oriented in the clockwise direction.

## See Also

### Constructing a Current Graphics Path

- [CGContextBeginPath](<beginpath().md>) — Creates a new empty path in a graphics context.
- [move(to:)](<move(to_).md>) — Begins a new subpath at the specified point.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:)](<addlines(between_).md>) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<addrect(__).md>) — Adds a rectangular path to the current path.
- [addRects(_:)](<addrects(__).md>) — Adds a set of rectangular paths to the current path.
- [addArc(center:radius:startAngle:endAngle:clockwise:)](<addarc(center_radius_startangle_endangle_clockwise_).md>) — Adds an arc of a circle to the current path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:)](<addarc(tangent1end_tangent2end_radius_).md>) — Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
