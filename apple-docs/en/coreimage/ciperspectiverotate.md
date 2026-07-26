---
title: CIPerspectiveRotate
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciperspectiverotate
source_url: 'https://developer.apple.com/documentation/coreimage/ciperspectiverotate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciperspectiverotate.json'
content_hash: 'sha256:e481a4158338fa6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPerspectiveRotate

<sub>Protocol</sub>

The properties you use to configure a perspective rotate filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIPerspectiveRotate : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [focalLength](ciperspectiverotate/focallength.md) — The 35mm equivalent focal length of the input image.
- [inputImage](ciperspectiverotate/inputimage.md) — The image to process.
- [pitch](ciperspectiverotate/pitch.md) — The pitch angle, in radians.
- [roll](ciperspectiverotate/roll.md) — The roll angle, in radians.
- [yaw](ciperspectiverotate/yaw.md) — The yaw angle, in radians.

## See Also

### Related Documentation

- [+ perspectiveRotateFilter](<cifilter-swift.class/perspectiverotate().md>) — Rotates an image in a 3D space.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md) — The properties you use to configure an edge preserve upsample filter.
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md) — The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md) — The properties you use to configure a keystone correction combined filter.
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md) — The properties you use to configure a keystone correction horizontal filter.
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md) — The properties you use to configure a keystone correction vertical filter.
- [CILanczosScaleTransform](cilanczosscaletransform.md) — The properties you use to configure a Lanczos scale transform filter.
- [CIPerspectiveCorrection](ciperspectivecorrection.md) — The properties you use to configure a perspective correction filter.
- [CIPerspectiveTransform](ciperspectivetransform.md) — The properties you use to configure a perspective transform filter.
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md) — The properties you use to configure a perspective transform with extent filter.
- [CIStraighten](cistraighten.md) — The properties you use to configure a straighten filter.
