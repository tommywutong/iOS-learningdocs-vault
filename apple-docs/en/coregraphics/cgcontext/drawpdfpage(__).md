---
title: 'drawPDFPage(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/drawpdfpage(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/drawpdfpage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/drawpdfpage%28_%3A%29.json'
content_hash: 'sha256:6b9c9035fa664c2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# drawPDFPage(_:)

<sub>Instance Method</sub>

Draws the content of a PDF page into the current graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drawPDFPage(_ page: CGPDFPage)
```

## Parameters

- `page` — A Core Graphics PDF page.

## Discussion

This function works in conjunction with the [CGPDFPage](../cgpdfpage.md) type to draw individual PDF pages into a context.

## See Also

### Drawing Images and PDF Content

- [draw(_:in:byTiling:)](<draw(__in_bytiling_).md>) — Draws an image in the specified area.
- [CGContextGetInterpolationQuality](interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
- [CGInterpolationQuality](../cginterpolationquality.md) — Levels of interpolation quality for rendering an image.
