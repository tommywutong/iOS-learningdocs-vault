---
title: cubeData
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcube/cubedata
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcube/cubedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcube/cubedata.json'
content_hash: 'sha256:4ae929824946612d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCube](../cicolorcube.md)

# cubeData

<sub>Instance Property</sub>

The cube texture data to use as a color lookup table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cubeData: Data { get set }
```

## Discussion

This filter maps color values in the input image to new color values using a three-dimensional color lookup table. For each RGBA pixel in the input image, the filter uses the R, G, and B component values as indices to identify a location in the table; the RGBA value at that location becomes the RGBA value of the output pixel.

Use the [cubeData](cubedata.md) parameter to provide data formatted for use as a color lookup table, and the inputCubeDimension parameter to specify the size of the table. This data should be an array of texel values in 32-bit floating-point RGBA linear premultiplied format. The inputCubeDimension parameter identifies the size of the cube by specifying the length of one side, so the size of the array should be [cubeDimension](cubedimension.md) cubed times the size of a single texel value. In the color table, the R component varies fastest, followed by G, then B.

## See Also

### Instance Properties

- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
