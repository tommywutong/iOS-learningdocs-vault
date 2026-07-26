---
title: properties
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/properties
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/properties.json'
content_hash: 'sha256:5513ccd7d8a904ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# properties

<sub>Type Property</sub>

The key for image metadata properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let properties: CIImageOption
```

## Discussion

To ensure that an image has no metadata properties, set the value of this key to `[NSNull null]`.

For more information about image metadata properties, see [Image Properties](../../imageio/image-properties.md) and [CGImageMetadata](../../imageio/cgimagemetadata.md).

## See Also

### Type Properties

- [kCIImageApplyOrientationProperty](applyorientationproperty.md) — The key for transforming an image according to orientation metadata.
- [kCIImageAuxiliaryDepth](auxiliarydepth.md) — The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [kCIImageAuxiliaryDisparity](auxiliarydisparity.md) — The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [kCIImageAuxiliaryHDRGainMap](auxiliaryhdrgainmap.md)
- [kCIImageAuxiliaryPortraitEffectsMatte](auxiliaryportraiteffectsmatte.md) — The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [kCIImageAuxiliarySemanticSegmentationGlassesMatte](auxiliarysemanticsegmentationglassesmatte.md)
- [kCIImageAuxiliarySemanticSegmentationHairMatte](auxiliarysemanticsegmentationhairmatte.md)
- [kCIImageAuxiliarySemanticSegmentationSkinMatte](auxiliarysemanticsegmentationskinmatte.md)
- [kCIImageAuxiliarySemanticSegmentationSkyMatte](auxiliarysemanticsegmentationskymatte.md)
- [kCIImageAuxiliarySemanticSegmentationTeethMatte](auxiliarysemanticsegmentationteethmatte.md)
- [kCIImageCacheImmediately](cacheimmediately.md)
- [kCIImageColorSpace](colorspace.md) — The key for a color space.
- [kCIImageExpandToHDR](expandtohdr.md) — A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [kCIImageNearestSampling](nearestsampling.md) — The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [kCIImageProviderTileSize](providertilesize.md) — A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
