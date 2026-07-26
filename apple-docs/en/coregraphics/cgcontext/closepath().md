---
title: closePath()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/closepath()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/closepath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/closepath%28%29.json'
content_hash: 'sha256:cb555dee66d4e81b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# closePath()

<sub>Instance Method</sub>

Closes and terminates the current path’s subpath.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func closePath()
```

## Discussion

Appends a line from the current point to the starting point of the current subpath and ends the subpath.

After closing the subpath, your application can begin a new subpath without first calling [CGContextMoveToPoint](../cgcontextmovetopoint.md). In this case, a new subpath is implicitly created with a starting and current point equal to the previous subpath’s starting point.

If the current path is empty or the current subpath is already closed, this function does nothing.

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
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
