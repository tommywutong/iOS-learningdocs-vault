---
title: CGColorRenderingIntent.saturation
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrenderingintent/saturation
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/saturation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrenderingintent/saturation.json'
content_hash: 'sha256:353e27e13a662a35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorRenderingIntent](../cgcolorrenderingintent.md)

# CGColorRenderingIntent.saturation

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case saturation
```

## Discussion

Preserve the relative saturation value of the colors when converting into the gamut of the output device. The result is an image with bright, saturated colors. Saturation intent is good for reproducing images with low detail, such as presentation charts and graphs.

## See Also

### Constants

- [kCGRenderingIntentDefault](defaultintent.md) — The default rendering intent for the graphics context.
- [kCGRenderingIntentAbsoluteColorimetric](absolutecolorimetric.md)
- [kCGRenderingIntentRelativeColorimetric](relativecolorimetric.md)
- [kCGRenderingIntentPerceptual](perceptual.md) — Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
