---
title: 'strokeLineSegments(between:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/strokelinesegments(between:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/strokelinesegments(between:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/strokelinesegments%28between%3A%29.json'
content_hash: 'sha256:93731daf3325bf9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# strokeLineSegments(between:)

<sub>Instance Method</sub>

Strokes a sequence of line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func strokeLineSegments(between points: [CGPoint])
```

## Parameters

- `points` — An array of points, organized as pairs—the starting point of a line segment followed by the ending point of a line segment. For example, the first point in the array specifies the starting position of the first line, the second point specifies the ending position of the first line, the third point specifies the starting position of the second line, and so forth.

## Discussion

This function creates a new path, adds the individual line segments to the path, and then strokes the path. The current path is cleared as a side effect of calling this function.

## See Also

### Drawing Shapes

- [CGContextClearRect](<clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
