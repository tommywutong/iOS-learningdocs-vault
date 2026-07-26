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
doc_path: /documentation/coreimage/cicolorcubesmixedwithmask/colorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubesmixedwithmask/colorspace.json'
content_hash: 'sha256:c318dc59c654d838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubesMixedWithMask](../cicolorcubesmixedwithmask.md)

# colorSpace

<sub>Instance Property</sub>

The working color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorSpace: CGColorSpace? { get set }
```

## See Also

### Instance Properties

- [cube0Data](cube0data.md) — The cube texture data to use as a color lookup table.
- [cube1Data](cube1data.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
- [maskImage](maskimage.md) — A masking image.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
