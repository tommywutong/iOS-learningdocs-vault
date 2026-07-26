---
title: colorSpace
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcubewithcolorspace/colorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubewithcolorspace/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubewithcolorspace/colorspace.json'
content_hash: 'sha256:b75b88ae63f0a46f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubeWithColorSpace](../cicolorcubewithcolorspace.md)

# colorSpace

<sub>Instance Property</sub>

The working color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorSpace: CGColorSpace? { get set }
```

## See Also

### Instance Properties

- [cubeData](cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
