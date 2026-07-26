---
title: CIFourCoordinateGeometryFilter
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifourcoordinategeometryfilter
source_url: 'https://developer.apple.com/documentation/coreimage/cifourcoordinategeometryfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifourcoordinategeometryfilter.json'
content_hash: 'sha256:2110d9412bcb8261'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFourCoordinateGeometryFilter

<sub>Protocol</sub>

The properties you use to configure a geometry adjustment filters that requires four coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIFourCoordinateGeometryFilter : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

- **Inherited By**: [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md), [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md), [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md), [CIPerspectiveCorrection](ciperspectivecorrection.md), [CIPerspectiveTransform](ciperspectivetransform.md), [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)

## Topics

### Instance Properties

- [bottomLeft](cifourcoordinategeometryfilter/bottomleft.md)
- [bottomRight](cifourcoordinategeometryfilter/bottomright.md)
- [inputImage](cifourcoordinategeometryfilter/inputimage.md) — The image to use as an input image.
- [topLeft](cifourcoordinategeometryfilter/topleft.md)
- [topRight](cifourcoordinategeometryfilter/topright.md)

## See Also

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
