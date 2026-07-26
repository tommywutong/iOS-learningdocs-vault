---
title: CGContextSetInterpolationQuality
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextsetinterpolationquality
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextsetinterpolationquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextsetinterpolationquality.json'
content_hash: 'sha256:0dc6e84ca521058a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextSetInterpolationQuality

<sub>Function</sub>

Sets the level of interpolation quality for a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextSetInterpolationQuality(CGContextRef c, CGInterpolationQuality quality);
```

## Parameters

- `c` — The graphics context to modify.

- `quality` — A constant that specifies the required level of interpolation quality. For possible values, see [CGInterpolationQuality](cginterpolationquality.md).

## Discussion

Interpolation quality is merely a hint to the context—not all contexts support all interpolation quality levels.

## See Also

### Drawing Images and PDF Content

- [CGContextDrawTiledImage](cgcontextdrawtiledimage.md) — Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.
- [CGContextDrawImage](cgcontextdrawimage.md) — Draws an image into a graphics context.
- [CGContextDrawPDFPage](<cgcontext/drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGContextGetInterpolationQuality](cgcontext/interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
- [CGInterpolationQuality](cginterpolationquality.md) — Levels of interpolation quality for rendering an image.
