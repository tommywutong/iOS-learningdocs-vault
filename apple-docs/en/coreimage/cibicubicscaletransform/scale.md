---
title: scale
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cibicubicscaletransform/scale
source_url: 'https://developer.apple.com/documentation/coreimage/cibicubicscaletransform/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cibicubicscaletransform/scale.json'
content_hash: 'sha256:c4a65d94ca90c338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIBicubicScaleTransform](../cibicubicscaletransform.md)

# scale

<sub>Instance Property</sub>

The scaling factor to use on the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var scale: Float { get set }
```

## Discussion

Values less than 1.0 scale down the images. Values greater than 1.0 scale up the image.

## See Also

### Instance Properties

- [aspectRatio](aspectratio.md) — The additional horizontal scaling factor to use on the image.
- [inputImage](inputimage.md) — The image to use as an input image.
- [parameterB](parameterb.md) — The value of B to use for the cubic resampling function.
- [parameterC](parameterc.md) — The value of C to use for the cubic resampling function.
