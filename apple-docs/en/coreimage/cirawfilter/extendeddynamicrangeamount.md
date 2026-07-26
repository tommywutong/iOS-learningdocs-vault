---
title: extendedDynamicRangeAmount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/extendeddynamicrangeamount
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/extendeddynamicrangeamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/extendeddynamicrangeamount.json'
content_hash: 'sha256:4c6b104ebfac3ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# extendedDynamicRangeAmount

<sub>Instance Property</sub>

A value that indicates the amount of extended dynamic range (EDR) to apply to the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extendedDynamicRangeAmount: Float { get set }
```

## Discussion

The value should be in the range of `0...2`. The default value is `0`. A value of `0` indicates no EDR. A value of `1` indicates default EDR, and a value of `2` indicates maximum EDR.

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
- [draftModeEnabled](isdraftmodeenabled.md) — A Boolean that indicates whether to enable draft mode.
- [gamutMappingEnabled](isgamutmappingenabled.md) — A Boolean that indicates whether to enable gamut mapping.
- [lensCorrectionEnabled](islenscorrectionenabled.md) — A Boolean that indicates whether to enable lens correction.
- [linearSpaceFilter](linearspacefilter.md) — An optional filter you can apply to the RAW image while it’s in linear space.
- [localToneMapAmount](localtonemapamount.md) — A value that indicates the amount of local tone curve to apply to the image.
- [luminanceNoiseReductionAmount](luminancenoisereductionamount.md) — A value that indicates the amount of luminance noise reduction to apply to the image.
- [moireReductionAmount](moirereductionamount.md) — A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
