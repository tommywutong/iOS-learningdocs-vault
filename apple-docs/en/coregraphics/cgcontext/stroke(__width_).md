---
title: 'stroke(_:width:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/stroke(_:width:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/stroke(_:width:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/stroke%28_%3Awidth%3A%29.json'
content_hash: 'sha256:4a86c4c75b61a3f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# stroke(_:width:)

<sub>Instance Method</sub>

Paints a rectangular path, using the specified line width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stroke(_ rect: CGRect, width: CGFloat)
```

## Parameters

- `rect` — A rectangle, in user space coordinates.

- `width` — A value, in user space units, that is greater than zero. This value does not affect the line width values in the current graphics state.

## Discussion

Aside from the line width value, Core Graphics uses the current attributes of the graphics state (such as stroke color) to paint the line. The line straddles the path, with half of the total width on either side.

The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeEllipseInRect](<strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [strokeLineSegments(between:)](<strokelinesegments(between_).md>) — Strokes a sequence of line segments.
