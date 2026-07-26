---
title: auxiliaryDisparity
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageoption/auxiliarydisparity
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/auxiliarydisparity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/auxiliarydisparity.json'
content_hash: 'sha256:0186e9135370d39e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# auxiliaryDisparity

<sub>Type Property</sub>

The key into the properties dictionary indicating whether to return an auxiliary disparity image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let auxiliaryDisparity: CIImageOption
```

## Discussion

The value of this key is an [NSNumber](../../foundation/nsnumber.md) containing a Boolean `true` or `false`.  If the value is `true`, then calls to [imageWithContentsOfURL:options:](../ciimage/imagewithcontentsofurl_options_.md) and [imageWithData:options:](../ciimage/imagewithdata_options_.md) will return the auxiliary image as a half-float monochrome image instead of the primary image, or [nil](../../objectivec/nil-227m0.md) if no auxiliary image exists.

## See Also

### Type Properties

- [kCIImageApplyOrientationProperty](applyorientationproperty.md) — The key for transforming an image according to orientation metadata.
- [kCIImageAuxiliaryDepth](auxiliarydepth.md) — The key into the properties dictionary indicating whether to return an auxiliary depth image.
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
- [kCIImageProperties](properties.md) — The key for image metadata properties.
- [kCIImageProviderTileSize](providertilesize.md) — A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
