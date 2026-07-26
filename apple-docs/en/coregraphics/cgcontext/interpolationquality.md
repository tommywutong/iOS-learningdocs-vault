---
title: interpolationQuality
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/interpolationquality
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/interpolationquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/interpolationquality.json'
content_hash: 'sha256:ffc7c47c374dba57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# interpolationQuality

<sub>Instance Property</sub>

Returns the current level of interpolation quality for a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interpolationQuality: CGInterpolationQuality { get set }
```

## Discussion

Interpolation quality is a graphics state parameter that provides a hint for the level of quality to use for image interpolation (for example, when scaling the image). Not all contexts support all interpolation quality levels.

## See Also

### Drawing Images and PDF Content

- [draw(_:in:byTiling:)](<draw(__in_bytiling_).md>) — Draws an image in the specified area.
- [CGContextDrawPDFPage](<drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGInterpolationQuality](../cginterpolationquality.md) — Levels of interpolation quality for rendering an image.
