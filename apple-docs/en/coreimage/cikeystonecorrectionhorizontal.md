---
title: CIKeystoneCorrectionHorizontal
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cikeystonecorrectionhorizontal
source_url: 'https://developer.apple.com/documentation/coreimage/cikeystonecorrectionhorizontal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikeystonecorrectionhorizontal.json'
content_hash: 'sha256:f751db0c6b6e8937'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIKeystoneCorrectionHorizontal

<sub>Protocol</sub>

The properties you use to configure a keystone correction horizontal filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIKeystoneCorrectionHorizontal : CIFourCoordinateGeometryFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)

## Topics

### Instance Properties

- [focalLength](cikeystonecorrectionhorizontal/focallength.md) — The 35mm equivalent focal length of the input image.

## See Also

### Related Documentation

- [+ keystoneCorrectionHorizontalFilter](<cifilter-swift.class/keystonecorrectionhorizontal().md>) — Horizontally adjusts an image to remove distortion.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
