---
title: 'strokeEllipse(in:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/strokeellipse(in:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/strokeellipse(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/strokeellipse%28in%3A%29.json'
content_hash: 'sha256:15c067c7ffbe175f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# strokeEllipse(in:)

<sub>Instance Method</sub>

Strokes an ellipse that fits inside the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func strokeEllipse(in rect: CGRect)
```

## Parameters

- `rect` — A rectangle that defines the area for the ellipse to fit in.

## Discussion

The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [strokeLineSegments(between:)](<strokelinesegments(between_).md>) — Strokes a sequence of line segments.
