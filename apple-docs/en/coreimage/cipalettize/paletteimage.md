---
title: paletteImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipalettize/paletteimage
source_url: 'https://developer.apple.com/documentation/coreimage/cipalettize/paletteimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipalettize/paletteimage.json'
content_hash: 'sha256:084fd612bd195689'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPalettize](../cipalettize.md)

# paletteImage

<sub>Instance Property</sub>

The input color palette, obtained by using a k-means clustering filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var paletteImage: CIImage? { get set }
```

## See Also

### Instance Properties

- [inputImage](inputimage.md) — The image to use as an input image.
- [perceptual](perceptual.md) — A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.
