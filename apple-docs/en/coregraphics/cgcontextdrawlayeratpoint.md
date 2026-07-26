---
title: CGContextDrawLayerAtPoint
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextdrawlayeratpoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextdrawlayeratpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextdrawlayeratpoint.json'
content_hash: 'sha256:56bec2c0cad7421f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextDrawLayerAtPoint

<sub>Function</sub>

Draws the contents of a CGLayer object at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextDrawLayerAtPoint(CGContextRef context, CGPoint point, CGLayerRef layer);
```

## Parameters

- `context` — The graphics context associated with the layer.

- `point` — The location, in current user space coordinates, to use as the origin for the drawing.

- `layer` — The layer whose contents you want to draw.

## Discussion

Calling the function `CGContextDrawLayerAtPoint` is equivalent to calling the function `CGContextDrawLayerInRect` with a rectangle that has its origin at `point` and its size equal to the size of the layer.

## See Also

### Drawing Core Graphics Layers

- [CGContextDrawLayerInRect](cgcontextdrawlayerinrect.md) — Draws the contents of a layer object into the specified rectangle.
