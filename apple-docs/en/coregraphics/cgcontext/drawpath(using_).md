---
title: 'drawPath(using:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/drawpath(using:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/drawpath(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/drawpath%28using%3A%29.json'
content_hash: 'sha256:574b873e8806e1bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# drawPath(using:)

<sub>Instance Method</sub>

Draws the current path using the provided drawing mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drawPath(using mode: CGPathDrawingMode)
```

## Parameters

- `mode` — A path drawing mode constant—[kCGPathFill](../cgpathdrawingmode/fill.md), [kCGPathEOFill](../cgpathdrawingmode/eofill.md), [kCGPathStroke](../cgpathdrawingmode/stroke.md), [kCGPathFillStroke](../cgpathdrawingmode/fillstroke.md), or [kCGPathEOFillStroke](../cgpathdrawingmode/eofillstroke.md). For a discussion of these constants, see [CGPath](../cgpath.md).

## Discussion

The current path is cleared as a side effect of calling this function.

## See Also

### Drawing the Current Graphics Path

- [CGPathDrawingMode](../cgpathdrawingmode.md) — Options for rendering a path.
- [fillPath(using:)](<fillpath(using_).md>) — Paints the area within the current path, as determined by the specified fill rule.
- [CGContextStrokePath](<strokepath().md>) — Paints a line along the current path.
