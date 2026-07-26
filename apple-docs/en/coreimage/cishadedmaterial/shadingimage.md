---
title: shadingImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cishadedmaterial/shadingimage
source_url: 'https://developer.apple.com/documentation/coreimage/cishadedmaterial/shadingimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cishadedmaterial/shadingimage.json'
content_hash: 'sha256:635291fd5607a579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIShadedMaterial](../cishadedmaterial.md)

# shadingImage

<sub>Instance Property</sub>

The image to use as the height field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shadingImage: CIImage? { get set }
```

## Discussion

The resulting image has greater heights with lighter shades, and lesser heights (lower areas) with darker shades.

## See Also

### Instance Properties

- [inputImage](inputimage.md) — The image to use as an input image.
- [scale](scale.md) — The scale of the effect.
