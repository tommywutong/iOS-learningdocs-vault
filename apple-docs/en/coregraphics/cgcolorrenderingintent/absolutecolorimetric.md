---
title: CGColorRenderingIntent.absoluteColorimetric
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric.json'
content_hash: 'sha256:94d741c997b3c563'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorRenderingIntent](../cgcolorrenderingintent.md)

# CGColorRenderingIntent.absoluteColorimetric

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case absoluteColorimetric
```

## Discussion

Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device. This can produce a clipping effect, where two different color values in the gamut of the graphics context are mapped to the same color value in the output device’s gamut. Unlike the relative colorimetric, absolute colorimetric does not modify colors inside the gamut of the output device.

## See Also

### Constants

- [kCGRenderingIntentDefault](defaultintent.md) — The default rendering intent for the graphics context.
- [kCGRenderingIntentRelativeColorimetric](relativecolorimetric.md)
- [kCGRenderingIntentPerceptual](perceptual.md) — Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
- [kCGRenderingIntentSaturation](saturation.md)
