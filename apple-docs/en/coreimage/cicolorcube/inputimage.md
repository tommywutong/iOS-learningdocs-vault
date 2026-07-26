---
title: inputImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcube/inputimage
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcube/inputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcube/inputimage.json'
content_hash: 'sha256:529a721dec11cad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCube](../cicolorcube.md)

# inputImage

<sub>Instance Property</sub>

The image to use as an input image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputImage: CIImage? { get set }
```

## See Also

### Instance Properties

- [cubeData](cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
