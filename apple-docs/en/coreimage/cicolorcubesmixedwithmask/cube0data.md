---
title: cube0Data
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcubesmixedwithmask/cube0data
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/cube0data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubesmixedwithmask/cube0data.json'
content_hash: 'sha256:59d6ac4c6eb5718c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubesMixedWithMask](../cicolorcubesmixedwithmask.md)

# cube0Data

<sub>Instance Property</sub>

The cube texture data to use as a color lookup table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cube0Data: Data { get set }
```

## Discussion

This filter maps color values in the input image to new color values using a three-dimensional color lookup table. For each RGBA pixel in the input image, the filter uses the R, G, and B component values as indices to identify a location in the table; the RGBA value at that location becomes the RGBA value of the output pixel.

Use the [cubeData](../cicolorcube/cubedata.md) parameter to provide data formatted for use as a color lookup table, and the inputCubeDimension parameter to specify the size of the table. This data should be an array of texel values in 32-bit floating-point RGBA linear premultiplied format. The inputCubeDimension parameter identifies the size of the cube by specifying the length of one side, so the size of the array should be [cubeDimension](../cicolorcube/cubedimension.md) cubed times the size of a single texel value. In the color table, the R component varies fastest, followed by G, then B.

## See Also

### Instance Properties

- [colorSpace](colorspace.md) — The working color space.
- [cube1Data](cube1data.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
- [maskImage](maskimage.md) — A masking image.
- [extrapolate](extrapolate.md) — If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.
