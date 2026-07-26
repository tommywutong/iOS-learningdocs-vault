---
title: 'stroke(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/stroke(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/stroke(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/stroke%28_%3A%29.json'
content_hash: 'sha256:adfb91264c71d46e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# stroke(_:)

<sub>Instance Method</sub>

Paints a rectangular path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stroke(_ rect: CGRect)
```

## Parameters

- `rect` — A rectangle, specified in user space coordinates.

## Discussion

The line width and stroke color of the context’s graphics state are used to paint the path. The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRectWithWidth](<stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [strokeLineSegments(between:)](<strokelinesegments(between_).md>) — Strokes a sequence of line segments.
