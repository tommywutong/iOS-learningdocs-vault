---
title: CGContextDrawLayerInRect
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextdrawlayerinrect
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextdrawlayerinrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextdrawlayerinrect.json'
content_hash: 'sha256:09aebcf97ce57a92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextDrawLayerInRect

<sub>Function</sub>

Draws the contents of a layer object into the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextDrawLayerInRect(CGContextRef context, CGRect rect, CGLayerRef layer);
```

## Parameters

- `context` — The graphics context associated with the layer.

- `rect` — The rectangle, in current user space coordinates, to draw to.

- `layer` — The layer whose contents you want to draw.

## Discussion

The contents are scaled, if necessary, to fit into the rectangle.

## See Also

### Drawing Core Graphics Layers

- [CGContextDrawLayerAtPoint](cgcontextdrawlayeratpoint.md) — Draws the contents of a CGLayer object at the specified point.
