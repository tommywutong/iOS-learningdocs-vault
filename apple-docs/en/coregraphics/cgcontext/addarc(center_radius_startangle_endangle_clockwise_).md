---
title: 'addArc(center:radius:startAngle:endAngle:clockwise:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/addarc(center:radius:startangle:endangle:clockwise:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/addarc(center:radius:startangle:endangle:clockwise:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/addarc%28center%3Aradius%3Astartangle%3Aendangle%3Aclockwise%3A%29.json'
content_hash: 'sha256:aac00da8f8b136cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# addArc(center:radius:startAngle:endAngle:clockwise:)

<sub>Instance Method</sub>

Adds an arc of a circle to the current path, specified with a radius and angles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

## Parameters

- `center` — The center of the arc, in user space coordinates.

- `radius` — The radius of the arc, in user space coordinates.

- `startAngle` — The angle to the starting point of the arc, measured in radians from the positive x-axis.

- `endAngle` — The angle to the end point of the arc, measured in radians from the positive x-axis.

- `clockwise` — [true](../../swift/true.md) to make a clockwise arc; [false](../../swift/false.md) to make a counterclockwise arc.

## Discussion

This method calculates starting and ending points using the radius and angles you specify, uses a sequence of cubic Bézier curves to approximate a segment of a circle between those points, and then appends those curves to the current path.

The `clockwise` parameter determines the direction in which the arc is created; the actual direction of the final path is dependent on the current transformation matrix of the graphics context. In a flipped coordinate system (the default for [UIView](../../uikit/uiview.md) drawing methods in iOS), specifying a clockwise arc results in a counterclockwise arc after the transformation is applied.

If the current path already contains a subpath, this method adds a line connecting the current point to the starting point of the arc. If the current path is empty, his method creates a new subpath whose starting point is the starting point of the arc. The ending point of the arc becomes the new current point of the path.

## See Also

### Constructing a Current Graphics Path

- [CGContextBeginPath](<beginpath().md>) — Creates a new empty path in a graphics context.
- [move(to:)](<move(to_).md>) — Begins a new subpath at the specified point.
- [addLine(to:)](<addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:)](<addlines(between_).md>) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<addrect(__).md>) — Adds a rectangular path to the current path.
- [addRects(_:)](<addrects(__).md>) — Adds a set of rectangular paths to the current path.
- [CGContextAddEllipseInRect](<addellipse(in_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addArc(tangent1End:tangent2End:radius:)](<addarc(tangent1end_tangent2end_radius_).md>) — Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
