---
title: CIEdgePreserveUpsample
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciedgepreserveupsample
source_url: 'https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciedgepreserveupsample.json'
content_hash: 'sha256:e6ce96bb98cfa19a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIEdgePreserveUpsample

<sub>Protocol</sub>

The properties you use to configure an edge preserve upsample filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIEdgePreserveUpsample : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](ciedgepreserveupsample/inputimage.md) — The image to use as an input image.
- [lumaSigma](ciedgepreserveupsample/lumasigma.md) — A value that specifies the influence of the input image’s luma information on the upsampling operation.
- [smallImage](ciedgepreserveupsample/smallimage.md) — The image that the filter upsamples.
- [spatialSigma](ciedgepreserveupsample/spatialsigma.md) — A value that specifies the influence of the input image’s spatial information on the upsampling operation.

## See Also

### Related Documentation

- [+ edgePreserveUpsampleFilter](<cifilter-swift.class/edgepreserveupsample().md>) — Creates a high-quality upscaled image.

### Protocols

- [CIBicubicScaleTransform](cibicubicscaletransform.md) — The properties you use to configure a bicubic scale transform filter.
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
