---
title: CGColorRenderingIntent.perceptual
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrenderingintent/perceptual
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/perceptual'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrenderingintent/perceptual.json'
content_hash: 'sha256:79edabc6b61974e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorRenderingIntent](../cgcolorrenderingintent.md)

# CGColorRenderingIntent.perceptual

<sub>Case</sub>

Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case perceptual
```

## See Also

### Constants

- [kCGRenderingIntentDefault](defaultintent.md) — The default rendering intent for the graphics context.
- [kCGRenderingIntentAbsoluteColorimetric](absolutecolorimetric.md)
- [kCGRenderingIntentRelativeColorimetric](relativecolorimetric.md)
- [kCGRenderingIntentSaturation](saturation.md)
