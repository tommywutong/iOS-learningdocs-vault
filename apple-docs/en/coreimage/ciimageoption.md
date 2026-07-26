---
title: CIImageOption
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageoption
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption.json'
content_hash: 'sha256:a166bef7a9687979'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIImageOption

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIImageOption
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<ciimageoption/init(rawvalue_).md>)

### Type Properties

- [kCIImageApplyOrientationProperty](ciimageoption/applyorientationproperty.md) — The key for transforming an image according to orientation metadata.
- [kCIImageAuxiliaryDepth](ciimageoption/auxiliarydepth.md) — The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [kCIImageAuxiliaryDisparity](ciimageoption/auxiliarydisparity.md) — The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [kCIImageAuxiliaryHDRGainMap](ciimageoption/auxiliaryhdrgainmap.md)
- [kCIImageAuxiliaryPortraitEffectsMatte](ciimageoption/auxiliaryportraiteffectsmatte.md) — The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [kCIImageAuxiliarySemanticSegmentationGlassesMatte](ciimageoption/auxiliarysemanticsegmentationglassesmatte.md)
- [kCIImageAuxiliarySemanticSegmentationHairMatte](ciimageoption/auxiliarysemanticsegmentationhairmatte.md)
- [kCIImageAuxiliarySemanticSegmentationSkinMatte](ciimageoption/auxiliarysemanticsegmentationskinmatte.md)
- [kCIImageAuxiliarySemanticSegmentationSkyMatte](ciimageoption/auxiliarysemanticsegmentationskymatte.md)
- [kCIImageAuxiliarySemanticSegmentationTeethMatte](ciimageoption/auxiliarysemanticsegmentationteethmatte.md)
- [kCIImageCacheImmediately](ciimageoption/cacheimmediately.md)
- [kCIImageColorSpace](ciimageoption/colorspace.md) — The key for a color space.
- [kCIImageExpandToHDR](ciimageoption/expandtohdr.md) — A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [kCIImageNearestSampling](ciimageoption/nearestsampling.md) — The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [kCIImageProperties](ciimageoption/properties.md) — The key for image metadata properties.
- [kCIImageProviderTileSize](ciimageoption/providertilesize.md) — A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
- [kCIImageProviderUserInfo](ciimageoption/provideruserinfo.md) — A key for data needed by the image provider. The associated value is an object that contains the needed data.
- [kCIImageTextureFormat](ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
- [kCIImageTextureTarget](ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageToneMapHDRtoSDR](ciimageoption/tonemaphdrtosdr.md)
- [kCIImageContentHeadroom](ciimageoption/contentheadroom.md)
- [kCIImageApplyCleanAperture](ciimageoption/applycleanaperture.md) — A Boolean value to control whether an image created with a CVPixelBuffer or an IOSurface should be cropped and offset according clean aperture attachments.
- [kCIImageContentAverageLightLevel](ciimageoption/contentaveragelightlevel.md) — A value for overriding the automatic behavior of the Content Average Light Level property when creating an image.
- [kCIImageSubsampleFactor](ciimageoption/subsamplefactor.md) — The factor by which to scale down a returned images. _(beta)_
- [kCIImageTypeIdentifierHint](ciimageoption/typeidentifierhint.md) — The uniform type identifier string to use in cases where a file’s format cannot be conclusively determined based solely on its contents. _(beta)_
- [kCIImageUseHardwareAcceleration](ciimageoption/usehardwareacceleration.md) — A Boolean value specifying that using hardware is preferred when decoding. _(beta)_
