---
title: CGContextDrawImage
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextdrawimage
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextdrawimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextdrawimage.json'
content_hash: 'sha256:71b85560964eb3cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextDrawImage

<sub>Function</sub>

Draws an image into a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextDrawImage(CGContextRef c, CGRect rect, CGImageRef image);
```

## Parameters

- `c` — The graphics context in which to draw the image.

- `rect` — The location and dimensions in user space of the bounding box in which to draw the image.

- `image` — The image to draw.

## Discussion

The image is scaled—disproportionately, if necessary—to fit the bounds specified by the `rect` parameter.

## See Also

### Drawing Images and PDF Content

- [CGContextDrawTiledImage](cgcontextdrawtiledimage.md) — Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.
- [CGContextDrawPDFPage](<cgcontext/drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGContextGetInterpolationQuality](cgcontext/interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
- [CGContextSetInterpolationQuality](cgcontextsetinterpolationquality.md) — Sets the level of interpolation quality for a graphics context.
- [CGInterpolationQuality](cginterpolationquality.md) — Levels of interpolation quality for rendering an image.
