---
title: luminanceNoiseReductionAmount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/luminancenoisereductionamount
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/luminancenoisereductionamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/luminancenoisereductionamount.json'
content_hash: 'sha256:0bdcc60546f1975d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# luminanceNoiseReductionAmount

<sub>Instance Property</sub>

A value that indicates the amount of luminance noise reduction to apply to the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var luminanceNoiseReductionAmount: Float { get set }
```

## Discussion

The value should be in the range of `0...1`. The default value varies by image. A value of `0` indicates no luminance noise reduction, and a value of `1` indicates maximum luminance noise reduction.

> [!note] Note
> The [luminanceNoiseReductionSupported](isluminancenoisereductionsupported.md) property is `false` if the current image doesn’t support this adjustment.

## See Also

### Configuring a filter

- [baselineExposure](baselineexposure.md) — A value that indicates the baseline exposure to apply to the image.
- [boostAmount](boostamount.md) — A value that indicates the amount of global tone curve to apply to the image.
- [boostShadowAmount](boostshadowamount.md) — A value that indicates the amount to boost the shadow areas of the image.
- [colorNoiseReductionAmount](colornoisereductionamount.md) — A value that indicates the amount of chroma noise reduction to apply to the image.
- [contrastAmount](contrastamount.md) — A value that indicates the amount of local contrast to apply to the edges of the image.
- [decoderVersion](decoderversion.md) — A value that indicates the decoder version to use.
- [detailAmount](detailamount.md) — A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [exposure](exposure.md) — A value that indicates the amount of exposure to apply to the image.
- [extendedDynamicRangeAmount](extendeddynamicrangeamount.md) — A value that indicates the amount of extended dynamic range (EDR) to apply to the image.
- [draftModeEnabled](isdraftmodeenabled.md) — A Boolean that indicates whether to enable draft mode.
- [gamutMappingEnabled](isgamutmappingenabled.md) — A Boolean that indicates whether to enable gamut mapping.
- [lensCorrectionEnabled](islenscorrectionenabled.md) — A Boolean that indicates whether to enable lens correction.
- [linearSpaceFilter](linearspacefilter.md) — An optional filter you can apply to the RAW image while it’s in linear space.
- [localToneMapAmount](localtonemapamount.md) — A value that indicates the amount of local tone curve to apply to the image.
- [moireReductionAmount](moirereductionamount.md) — A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
