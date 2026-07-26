---
title: semanticSegmentationSkinMatte
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/semanticsegmentationskinmatte
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/semanticsegmentationskinmatte'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/semanticsegmentationskinmatte.json'
content_hash: 'sha256:7fd3708857a219fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# semanticSegmentationSkinMatte

<sub>Instance Property</sub>

An optional auxiliary image that represents the semantic segmentation skin matte of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var semanticSegmentationSkinMatte: CIImage? { get }
```

## Discussion

This matting image segments skin from all people in the visible field of view of the image.

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
- [luminanceNoiseReductionAmount](luminancenoisereductionamount.md) — A value that indicates the amount of luminance noise reduction to apply to the image.
