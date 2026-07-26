---
title: CIPerspectiveTransformWithExtent
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciperspectivetransformwithextent
source_url: 'https://developer.apple.com/documentation/coreimage/ciperspectivetransformwithextent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciperspectivetransformwithextent.json'
content_hash: 'sha256:97926eff585a4b8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPerspectiveTransformWithExtent

<sub>Protocol</sub>

The properties you use to configure a perspective transform with extent filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPerspectiveTransformWithExtent : CIFourCoordinateGeometryFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)

## Topics

### Instance Properties

- [extent](ciperspectivetransformwithextent/extent.md) — A rectangle that defines the extent of the effect.

## See Also

### Related Documentation

- [+ perspectiveTransformWithExtentFilter](<cifilter-swift.class/perspectivetransformwithextent().md>) — Alters an image’s geometry to adjust the perspective while applying constraints.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
