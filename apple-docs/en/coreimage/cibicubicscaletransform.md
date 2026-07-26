---
title: CIBicubicScaleTransform
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cibicubicscaletransform
source_url: 'https://developer.apple.com/documentation/coreimage/cibicubicscaletransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cibicubicscaletransform.json'
content_hash: 'sha256:1704449a05a3c4d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIBicubicScaleTransform

<sub>Protocol</sub>

The properties you use to configure a bicubic scale transform filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIBicubicScaleTransform : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [aspectRatio](cibicubicscaletransform/aspectratio.md) — The additional horizontal scaling factor to use on the image.
- [inputImage](cibicubicscaletransform/inputimage.md) — The image to use as an input image.
- [parameterB](cibicubicscaletransform/parameterb.md) — The value of B to use for the cubic resampling function.
- [parameterC](cibicubicscaletransform/parameterc.md) — The value of C to use for the cubic resampling function.
- [scale](cibicubicscaletransform/scale.md) — The scaling factor to use on the image.

## See Also

### Related Documentation

- [+ bicubicScaleTransformFilter](<cifilter-swift.class/bicubicscaletransform().md>) — Produces a high-quality scaled version of an image.

### Protocols

- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
