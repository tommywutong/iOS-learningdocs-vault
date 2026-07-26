---
title: strokePath()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/strokepath()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/strokepath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/strokepath%28%29.json'
content_hash: 'sha256:9a38ef9170076dde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# strokePath()

<sub>Instance Method</sub>

Paints a line along the current path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func strokePath()
```

## Discussion

The line width and stroke color of the context’s graphics state are used to paint the path. The current path is cleared as a side effect of calling this function.

## See Also

### Drawing the Current Graphics Path

- [CGContextDrawPath](<drawpath(using_).md>) — Draws the current path using the provided drawing mode.
- [CGPathDrawingMode](../cgpathdrawingmode.md) — Options for rendering a path.
- [fillPath(using:)](<fillpath(using_).md>) — Paints the area within the current path, as determined by the specified fill rule.
