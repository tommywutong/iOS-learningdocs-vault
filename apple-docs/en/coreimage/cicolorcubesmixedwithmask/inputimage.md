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
doc_path: /documentation/coreimage/cicolorcubesmixedwithmask/inputimage
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/inputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubesmixedwithmask/inputimage.json'
content_hash: 'sha256:c8e0e9d0935714ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubesMixedWithMask](../cicolorcubesmixedwithmask.md)

# inputImage

<sub>Instance Property</sub>

The image to use as an input image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputImage: CIImage? { get set }
```

## See Also

### Instance Properties

- [colorSpace](colorspace.md) — The working color space.
- [cube0Data](cube0data.md) — The cube texture data to use as a color lookup table.
- [cube1Data](cube1data.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [maskImage](maskimage.md) — A masking image.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
