---
title: CGContextStrokeLineSegments
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextstrokelinesegments
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextstrokelinesegments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextstrokelinesegments.json'
content_hash: 'sha256:5a90730894547d8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextStrokeLineSegments

<sub>Function</sub>

Strokes a sequence of line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextStrokeLineSegments(CGContextRef c, const CGPoint *points, size_t count);
```

## Parameters

- `c` — A graphics context.

- `points` — An array of points, organized as pairs—the starting point of a line segment followed by the ending point of a line segment. For example, the first point in the array specifies the starting position of the first line, the second point specifies the ending position of the first line, the third point specifies the starting position of the second line, and so forth.

- `count` — The number of points in the `points` array.

## Discussion

This function creates a new path, adds the individual line segments to the path, and then strokes the path. The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<cgcontext/clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<cgcontext/fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [CGContextFillRects](cgcontextfillrects.md) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<cgcontext/fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<cgcontext/stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<cgcontext/stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<cgcontext/strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
