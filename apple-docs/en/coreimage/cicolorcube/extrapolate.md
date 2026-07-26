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
doc_path: /documentation/coreimage/cicolorcube/extrapolate
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcube/extrapolate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcube/extrapolate.json'
content_hash: 'sha256:882e85fe948d97fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCube](../cicolorcube.md)

# extrapolate

<sub>Instance Property</sub>

If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extrapolate: Bool { get set }
```

## See Also

### Instance Properties

- [cubeData](cubedata.md) — The cube texture data to use as a color lookup table.
- [cubeDimension](cubedimension.md) — The length, in texels, of each side of the cube texture.
- [inputImage](inputimage.md) — The image to use as an input image.
