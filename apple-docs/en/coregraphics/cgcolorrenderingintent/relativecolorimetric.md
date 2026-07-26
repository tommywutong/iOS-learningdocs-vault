---
title: CGColorRenderingIntent.relativeColorimetric
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrenderingintent/relativecolorimetric
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/relativecolorimetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrenderingintent/relativecolorimetric.json'
content_hash: 'sha256:04ba870042b259d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorRenderingIntent](../cgcolorrenderingintent.md)

# CGColorRenderingIntent.relativeColorimetric

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case relativeColorimetric
```

## Discussion

Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device. This can produce a clipping effect, where two different color values in the gamut of the graphics context are mapped to the same color value in the output device’s gamut. The relative colorimetric shifts all colors (including those within the gamut) to account for the difference between the white point of the graphics context and the white point of the output device.

## See Also

### Constants

- [kCGRenderingIntentDefault](defaultintent.md) — The default rendering intent for the graphics context.
- [kCGRenderingIntentAbsoluteColorimetric](absolutecolorimetric.md)
- [kCGRenderingIntentPerceptual](perceptual.md) — Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
- [kCGRenderingIntentSaturation](saturation.md)
