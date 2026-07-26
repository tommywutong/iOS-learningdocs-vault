---
title: kCIInputBiasKey
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kciinputbiaskey
source_url: 'https://developer.apple.com/documentation/coreimage/kciinputbiaskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kciinputbiaskey.json'
content_hash: 'sha256:35cdf68ac95b4feb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCIInputBiasKey

<sub>Global Variable</sub>

Simple bias value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCIInputBiasKey: String
```

## Discussion

A key for the simple bias value to use along with the exposure adjustment ([kCIInputEVKey](kciinputevkey.md)). The associated value must be an [NSNumber](../foundation/nsnumber.md) object that specifies floating-point value. The value has no effect if the image used for initialization is not RAW.

## See Also

### Constants

- [kCIInputDecoderVersionKey](cirawfilteroption/decoderversion.md) — A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [kCISupportedDecoderVersionsKey](cirawfilteroption/supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is _visually_ the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW. _(deprecated)_
- [kCISupportedDecoderVersionsKey](cirawfilteroption/supporteddecoderversions.md) — A key for the supported decoder versions. _(deprecated)_
- [kCIInputBoostKey](cirawfilteroption/boostamount.md) — A key for the amount of boost to apply to an image. _(deprecated)_
- [kCIInputNeutralChromaticityXKey](cirawfilteroption/neutralchromaticityx.md) — The x value of the chromaticity. _(deprecated)_
- [kCIInputNeutralChromaticityYKey](cirawfilteroption/neutralchromaticityy.md) — The y value of the chromaticity. _(deprecated)_
- [kCIInputNeutralTemperatureKey](cirawfilteroption/neutraltemperature.md) — A key for neutral temperature. _(deprecated)_
- [kCIInputNeutralTintKey](cirawfilteroption/neutraltint.md) — A key for the neutral tint. _(deprecated)_
- [kCIInputNeutralLocationKey](cirawfilteroption/neutrallocation.md) — A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [CIVector](civector.md) object that specifies the location (`x`, `y`). _(deprecated)_
- [kCIInputScaleFactorKey](cirawfilteroption/scalefactor.md) — A key for the scale factor. _(deprecated)_
- [kCIInputAllowDraftModeKey](cirawfilteroption/allowdraftmode.md) — A key for allowing draft mode. _(deprecated)_
- [kCIInputIgnoreImageOrientationKey](cirawfilteroption/ignoreimageorientation.md) — A key for specifying whether to ignore the image orientation _(deprecated)_
- [kCIInputImageOrientationKey](cirawfilteroption/imageorientation.md) — A key for the image orientation. _(deprecated)_
- [kCIInputEnableSharpeningKey](cirawfilteroption/enablesharpening.md) — A key for the sharpening state. _(deprecated)_
- [kCIInputEnableChromaticNoiseTrackingKey](cirawfilteroption/enablechromaticnoisetracking.md) — A key for progressive chromatic noise tracking (based on ISO and exposure time). _(deprecated)_
- [kCIInputNoiseReductionAmountKey](cirawfilteroption/noisereductionamount.md) — A key for the amount to reduce noise in the image. _(deprecated)_
