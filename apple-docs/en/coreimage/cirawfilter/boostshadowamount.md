---
title: boostShadowAmount
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/boostshadowamount
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/boostshadowamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/boostshadowamount.json'
content_hash: 'sha256:cece5c148d146736'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# boostShadowAmount

<sub>Instance Property</sub>

A value that indicates the amount to boost the shadow areas of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var boostShadowAmount: Float { get set }
```

## Discussion

Use this value to lighten details in shadows. The value should be in the range of `0...2`. The default value is `1`. A value less than `1` darkens the shadows, and a value greater than `1` lightens the shadows.

> [!note] Note
> Setting this value has no effect if the [boostAmount](boostamount.md) is `0`.

## See Also

### Configuring a filter

- [baselineExposure](baselineexposure.md) — A value that indicates the baseline exposure to apply to the image.
- [boostAmount](boostamount.md) — A value that indicates the amount of global tone curve to apply to the image.
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
- [luminanceNoiseReductionAmount](luminancenoisereductionamount.md) — A value that indicates the amount of luminance noise reduction to apply to the image.
- [moireReductionAmount](moirereductionamount.md) — A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
