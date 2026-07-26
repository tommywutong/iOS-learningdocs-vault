---
title: 'fill(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/fill(_:)-6jc4y'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/fill(_:)-6jc4y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/fill%28_%3A%29-6jc4y.json'
content_hash: 'sha256:64c5062629e55239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# fill(_:)

<sub>Instance Method</sub>

Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fill(_ rects: [CGRect])
```

## Parameters

- `rects` — An array of rectangles, in user space coordinates.

## Discussion

The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [strokeLineSegments(between:)](<strokelinesegments(between_).md>) — Strokes a sequence of line segments.
