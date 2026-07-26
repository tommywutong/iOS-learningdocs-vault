---
title: 'clear(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/clear(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/clear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/clear%28_%3A%29.json'
content_hash: 'sha256:dc0890c7160f1c37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# clear(_:)

<sub>Instance Method</sub>

Paints a transparent rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clear(_ rect: CGRect)
```

## Parameters

- `rect` — The rectangle, in user space coordinates.

## Discussion

If the provided context is a window or bitmap context, Core Graphics clears the rectangle. For other context types, Core Graphics fills the rectangle in a device-dependent manner. However, you should not use this function in contexts other than window or bitmap contexts.

## See Also

### Drawing Shapes

- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [strokeLineSegments(between:)](<strokelinesegments(between_).md>) — Strokes a sequence of line segments.
