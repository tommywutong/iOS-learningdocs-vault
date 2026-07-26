---
title: noiseReductionDetailAmount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coreimage/cirawfilteroption/noisereductiondetailamount
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilteroption/noisereductiondetailamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilteroption/noisereductiondetailamount.json'
content_hash: 'sha256:4ef0cffd5d83f905'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilterOption](../cirawfilteroption.md)

# noiseReductionDetailAmount

<sub>Type Property</sub>

A key for the amount of detail enhancement to apply during noise reduction.

> [!warning] Deprecated
> Use new CIRAWFilter class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let noiseReductionDetailAmount: CIRAWFilterOption
```

## Discussion

The value for this key is a [NSNumber](../../foundation/nsnumber.md) object containing a value between `0.0` and `1.0`.

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
- [kCIInputDisableGamutMapKey](disablegamutmap.md) — Whether or not to disable gamut mapping. _(deprecated)_
- [kCIInputEnableChromaticNoiseTrackingKey](enablechromaticnoisetracking.md) — A key for progressive chromatic noise tracking (based on ISO and exposure time). _(deprecated)_
- [kCIInputEnableSharpeningKey](enablesharpening.md) — A key for the sharpening state. _(deprecated)_
- [kCIInputEnableVendorLensCorrectionKey](enablevendorlenscorrection.md) — A key for whether to automatically correct for image distortion from known lenses. _(deprecated)_
- [kCIInputIgnoreImageOrientationKey](ignoreimageorientation.md) — A key for specifying whether to ignore the image orientation _(deprecated)_
- [kCIInputImageOrientationKey](imageorientation.md) — A key for the image orientation. _(deprecated)_
