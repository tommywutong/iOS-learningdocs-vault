---
title: extrapolate
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcubewithcolorspace/extrapolate
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubewithcolorspace/extrapolate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubewithcolorspace/extrapolate.json'
content_hash: 'sha256:be628eac694f352c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubeWithColorSpace](../cicolorcubewithcolorspace.md)

# extrapolate

<sub>Instance Property</sub>

If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extrapolate: Bool { get set }
```

## See Also

### Instance Properties

- [colorSpace](colorspace.md) — The working color space.
- [cubeData](cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
