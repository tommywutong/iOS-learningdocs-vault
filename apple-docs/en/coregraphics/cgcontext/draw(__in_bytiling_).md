---
title: 'draw(_:in:byTiling:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/draw(_:in:bytiling:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:in:bytiling:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/draw%28_%3Ain%3Abytiling%3A%29.json'
content_hash: 'sha256:e7bee5be494b2305'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# draw(_:in:byTiling:)

<sub>Instance Method</sub>

Draws an image in the specified area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(_ image: CGImage, in rect: CGRect, byTiling: Bool = false)
```

## Parameters

- `image` — The image to draw.

- `rect` — The rectangle, in user space coordinates, in which to draw the image.

- `byTiling` — If [true](../../swift/true.md), this method fills the context’s entire clipping region by tiling many copies of the image, and the `rect` parameter defines the origin and size of the tiling pattern. If [false](../../swift/false.md) (the default), this method draws a single copy of the image in the area defined by the `rect` parameter.

## Discussion

This method scales the image (disproportionately, if necessary) to fit the bounds specified by the `rect` parameter.When the `byTiling` parameter is [true](../../swift/true.md), the image is tiled in user space—thus, unlike when drawing with patterns, the current transformation (see the [CGContextGetCTM](ctm.md) property) affects the final result.

## See Also

### Drawing Images and PDF Content

- [CGContextDrawPDFPage](<drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGContextGetInterpolationQuality](interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
- [CGInterpolationQuality](../cginterpolationquality.md) — Levels of interpolation quality for rendering an image.
