---
title: CGContextFillRects
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextfillrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextfillrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextfillrects.json'
content_hash: 'sha256:5ce3d2a9dc94851a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextFillRects

<sub>Function</sub>

Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextFillRects(CGContextRef c, const CGRect *rects, size_t count);
```

## Parameters

- `c` — A graphics context .

- `rects` — An array of rectangles, in user space coordinates.

- `count` — The number rectangles in the  `rects` array.

## Discussion

The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<cgcontext/clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<cgcontext/fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<cgcontext/fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<cgcontext/stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<cgcontext/stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<cgcontext/strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [CGContextStrokeLineSegments](cgcontextstrokelinesegments.md) — Strokes a sequence of line segments.
