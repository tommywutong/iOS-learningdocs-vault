---
title: CGContextFillPath
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextfillpath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextfillpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextfillpath.json'
content_hash: 'sha256:32034d33471b3e5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextFillPath

<sub>Function</sub>

Paints the area within the current path, using the nonzero winding number rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextFillPath(CGContextRef c);
```

## Parameters

- `c` — A graphics context that contains a path to fill.

## Discussion

Each subpath is treated as if it were closed by calling [CGContextClosePath](<cgcontext/closepath().md>). The nonzero winding number rule is described in [Filling a Path](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211-TPXREF106) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066). The current path is cleared as a side effect of calling this function.

## See Also

### Drawing the Current Graphics Path

- [CGContextDrawPath](<cgcontext/drawpath(using_).md>) — Draws the current path using the provided drawing mode.
- [CGPathDrawingMode](cgpathdrawingmode.md) — Options for rendering a path.
- [CGContextEOFillPath](cgcontexteofillpath.md) — Paints the area within the current path, using the even-odd fill rule.
- [CGContextStrokePath](<cgcontext/strokepath().md>) — Paints a line along the current path.
