---
title: CILanczosScaleTransform
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilanczosscaletransform
source_url: 'https://developer.apple.com/documentation/coreimage/cilanczosscaletransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilanczosscaletransform.json'
content_hash: 'sha256:e8756759d48ad2b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CILanczosScaleTransform

<sub>Protocol</sub>

The properties you use to configure a Lanczos scale transform filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CILanczosScaleTransform : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [aspectRatio](cilanczosscaletransform/aspectratio.md) — The additional horizontal scaling factor to use on the image.
- [inputImage](cilanczosscaletransform/inputimage.md) — The image to use as an input image.
- [scale](cilanczosscaletransform/scale.md) — The scaling factor to use on the image.

## See Also

### Related Documentation

- [+ lanczosScaleTransformFilter](<cifilter-swift.class/lanczosscaletransform().md>) — Creates a high-quality, scaled version of a source image.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
