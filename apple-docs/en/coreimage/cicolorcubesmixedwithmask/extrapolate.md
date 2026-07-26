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
doc_path: /documentation/coreimage/cicolorcubesmixedwithmask/extrapolate
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/extrapolate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcubesmixedwithmask/extrapolate.json'
content_hash: 'sha256:8e16340f6507098e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCubesMixedWithMask](../cicolorcubesmixedwithmask.md)

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
- [cube0Data](cube0data.md) — The cube texture data to use as a color lookup table.
- [cube1Data](cube1data.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
- [maskImage](maskimage.md) — A masking image.
