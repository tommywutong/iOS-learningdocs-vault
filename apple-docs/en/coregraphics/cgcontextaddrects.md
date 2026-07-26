---
title: CGContextAddRects
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextaddrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextaddrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextaddrects.json'
content_hash: 'sha256:62114e96e3033fba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextAddRects

<sub>Function</sub>

Adds a set of rectangular paths to the current path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextAddRects(CGContextRef c, const CGRect *rects, size_t count);
```

## Parameters

- `c` — A graphics context.

- `rects` — An array of rectangles, specified in user space coordinates.

- `count` — The number of rectangles in the `rects` array.

## Discussion

This is a convenience function that adds an array of rectangles to a path, as if it called [CGContextAddRect](<cgcontext/addrect(__).md>) for each rectangle.

## See Also

### Constructing a Current Graphics Path

- [CGContextBeginPath](<cgcontext/beginpath().md>) — Creates a new empty path in a graphics context.
- [CGContextMoveToPoint](cgcontextmovetopoint.md) — Begins a new subpath at the point you specify.
- [CGContextAddLineToPoint](cgcontextaddlinetopoint.md) — Appends a straight line segment from the current point to the provided point .
- [CGContextAddLines](cgcontextaddlines.md) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<cgcontext/addrect(__).md>) — Adds a rectangular path to the current path.
- [CGContextAddEllipseInRect](<cgcontext/addellipse(in_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [CGContextAddArc](cgcontextaddarc.md) — Adds an arc of a circle to the current path, possibly preceded by a straight line segment
- [CGContextAddArcToPoint](cgcontextaddarctopoint.md) — Adds an arc of a circle to the current path, using a radius and tangent points.
- [CGContextAddCurveToPoint](cgcontextaddcurvetopoint.md) — Appends a cubic Bézier curve from the current point, using the provided control points and end point .
- [CGContextAddQuadCurveToPoint](cgcontextaddquadcurvetopoint.md) — Appends a quadratic Bézier curve from the current point, using a control point and an end point you specify.
- [CGContextAddPath](<cgcontext/addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<cgcontext/closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](cgcontext/path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<cgcontext/replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.
