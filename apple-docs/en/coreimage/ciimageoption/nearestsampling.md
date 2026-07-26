---
title: nearestSampling
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/nearestsampling
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/nearestsampling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/nearestsampling.json'
content_hash: 'sha256:a8f72eb3702c568a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# nearestSampling

<sub>Type Property</sub>

The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let nearestSampling: CIImageOption
```

## Discussion

The value for this key is an [NSNumber](../../foundation/nsnumber.md) containing a Boolean value specifying whether the image should be sampled using nearest neighbor behavior.  An unspecified value defaults to linear sampling.

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
- [kCIImageProperties](properties.md) — The key for image metadata properties.
- [kCIImageProviderTileSize](providertilesize.md) — A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
