---
title: 'addArc(tangent1End:tangent2End:radius:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/addarc(tangent1end:tangent2end:radius:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/addarc(tangent1end:tangent2end:radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/addarc%28tangent1end%3Atangent2end%3Aradius%3A%29.json'
content_hash: 'sha256:e3bf158df6a5822f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addArc(tangent1End:tangent2End:radius:)

<sub>Instance Method</sub>

Adds an arc of a circle to the current path, specified with a radius and two tangent lines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat)
```

## Parameters

- `tangent1End` — The end point, in user space coordinates, for the first tangent line to be used in constructing the arc. (The start point for this tangent line is the path’s current point.)

- `tangent2End` — The end point, in user space coordinates, for the second tangent line to be used in constructing the arc. (The start point for this tangent line is the `tangent1End` point.)

- `radius` — The radius of the arc, in user space coordinates.

## Discussion

This method calculates two tangent lines—the first from the current point to the `tangent1End` point, and the second from the `tangent1End` point to the `tangent2End` point—then calculates the start and end points for a circular arc of the specified radius such that the arc is tangent to both lines. Finally, this method approximates that arc with a sequence of cubic Bézier curves and appends those curves to the current path.

If the starting point of the arc (that is, the point where a circle of the specified radius must meet the first tangent line in order to also be tangent to the second line) is not the current point, this method appends a straight line segment from the current point to the starting point of the arc.

The ending point of the arc (that is, the point where a circle of the specified radius must meet the second tangent line in order to also be tangent to the first line) becomes the new current point of the path.

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
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
