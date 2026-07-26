---
title: disableGamutMap
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.12+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coreimage/cirawfilteroption/disablegamutmap
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilteroption/disablegamutmap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilteroption/disablegamutmap.json'
content_hash: 'sha256:e3305edf37fc66f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilterOption](../cirawfilteroption.md)

# disableGamutMap

<sub>Type Property</sub>

Whether or not to disable gamut mapping.

> [!warning] Deprecated
> Use new CIRAWFilter class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let disableGamutMap: CIRAWFilterOption
```

## Discussion

A value of `true` disables gamut mapping.  The default is `false`.

## See Also

### Type Properties

- [kCIActiveKeys](activekeys.md) — A key for the set of input keys available for use. _(deprecated)_
- [kCIInputAllowDraftModeKey](allowdraftmode.md) — A key for allowing draft mode. _(deprecated)_
- [kCIInputBaselineExposureKey](baselineexposure.md) — The amount of baseline exposure applied. _(deprecated)_
- [kCIInputBoostKey](boostamount.md) — A key for the amount of boost to apply to an image. _(deprecated)_
- [kCIInputBoostShadowAmountKey](boostshadowamount.md) — A key for the amount to boost the shadow areas of the image. _(deprecated)_
- [kCIInputEnableEDRModeKey](ciinputenableedrmodekey.md) _(deprecated)_
- [kCIInputLocalToneMapAmountKey](ciinputlocaltonemapamountkey.md) _(deprecated)_
- [kCIInputColorNoiseReductionAmountKey](colornoisereductionamount.md) — A key for the amount of noise reduction to apply to color data in the image. _(deprecated)_
- [kCIInputDecoderVersionKey](decoderversion.md) — A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [kCISupportedDecoderVersionsKey](supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is _visually_ the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW. _(deprecated)_
- [kCIInputEnableChromaticNoiseTrackingKey](enablechromaticnoisetracking.md) — A key for progressive chromatic noise tracking (based on ISO and exposure time). _(deprecated)_
- [kCIInputEnableSharpeningKey](enablesharpening.md) — A key for the sharpening state. _(deprecated)_
- [kCIInputEnableVendorLensCorrectionKey](enablevendorlenscorrection.md) — A key for whether to automatically correct for image distortion from known lenses. _(deprecated)_
- [kCIInputIgnoreImageOrientationKey](ignoreimageorientation.md) — A key for specifying whether to ignore the image orientation _(deprecated)_
- [kCIInputImageOrientationKey](imageorientation.md) — A key for the image orientation. _(deprecated)_
- [kCIInputLinearSpaceFilter](linearspacefilter.md) — A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [CIFilter](../cifilter-swift.class.md) object. _(deprecated)_
