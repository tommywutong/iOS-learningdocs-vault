---
title: CIPerspectiveCorrection
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciperspectivecorrection
source_url: 'https://developer.apple.com/documentation/coreimage/ciperspectivecorrection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciperspectivecorrection.json'
content_hash: 'sha256:a92ad0c342451e94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPerspectiveCorrection

<sub>Protocol</sub>

The properties you use to configure a perspective correction filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPerspectiveCorrection : CIFourCoordinateGeometryFilter
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md), [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)

## Topics

### Instance Properties

- [crop](ciperspectivecorrection/crop.md) — A rectangle that specifies the extent of the corrected image.

## See Also

### Related Documentation

- [+ perspectiveCorrectionFilter](<cifilter-swift.class/perspectivecorrection().md>) — Transforms an image’s perspective.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveRotate](ciperspectiverotate.md) — The properties you use to configure a perspective rotate filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
