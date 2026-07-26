---
title: 'setRenderingIntent(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setrenderingintent(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setrenderingintent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setrenderingintent%28_%3A%29.json'
content_hash: 'sha256:26455ef3ac43d292'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setRenderingIntent(_:)

<sub>Instance Method</sub>

Sets the rendering intent in the current graphics state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setRenderingIntent(_ intent: CGColorRenderingIntent)
```

## Parameters

- `intent` — A rendering intent constant—[kCGRenderingIntentDefault](../cgcolorrenderingintent/defaultintent.md), [kCGRenderingIntentAbsoluteColorimetric](../cgcolorrenderingintent/absolutecolorimetric.md), [kCGRenderingIntentRelativeColorimetric](../cgcolorrenderingintent/relativecolorimetric.md), [kCGRenderingIntentPerceptual](../cgcolorrenderingintent/perceptual.md), or [kCGRenderingIntentSaturation](../cgcolorrenderingintent/saturation.md). For a discussion of these constants, see [CGColorSpace](../cgcolorspace.md).

## Discussion

The rendering intent specifies how to handle colors that are not located within the gamut of the destination color space of a graphics context. If you do not explicitly set the rendering intent, Core Graphics uses perceptual rendering intent when drawing sampled images and relative colorimetric rendering intent for all other drawing.

## See Also

### Managing a Graphics Context

- [CGContextFlush](<flush().md>) — Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [CGContextSynchronize](<synchronize().md>) — Marks a window context for update.
- [CGContextSetBlendMode](<setblendmode(__).md>) — Sets how sample values are composited by a graphics context.
- [CGBlendMode](../cgblendmode.md) — Compositing operations for images.
