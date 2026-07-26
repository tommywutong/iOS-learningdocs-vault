---
title: intensity
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolormonochrome/intensity
source_url: 'https://developer.apple.com/documentation/coreimage/cicolormonochrome/intensity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolormonochrome/intensity.json'
content_hash: 'sha256:718085e61e6e2ce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorMonochrome](../cicolormonochrome.md)

# intensity

<sub>Instance Property</sub>

The intensity of the monochrome effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intensity: Float { get set }
```

## Discussion

A value of 1.0 creates a monochrome image using the supplied color. A value of 0.0 has no effect on the image.

## See Also

### Instance Properties

- [color](color.md) — The monochrome color to apply to the image.
- [inputImage](inputimage.md) — The image to use as an input image.
