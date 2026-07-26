---
title: isColorNoiseReductionSupported
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/iscolornoisereductionsupported
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/iscolornoisereductionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/iscolornoisereductionsupported.json'
content_hash: 'sha256:f904cbab8d71facb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# isColorNoiseReductionSupported

<sub>Instance Property</sub>

A Boolean that indicates if the current image supports color noise reduction adjustments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isColorNoiseReductionSupported: Bool { get }
```

## Discussion

If this value is `true`, you can adjust the amount of color noise reduction to apply to the image by setting [colorNoiseReductionAmount](colornoisereductionamount.md).

## See Also

### Inspecting supported camera models, decoders, and filters

- [supportedCameraModels](supportedcameramodels.md) — An array containing the names of all supported camera models.
- [supportedDecoderVersions](supporteddecoderversions.md) — An array of all supported decoder versions for the given image type.
- [CIRAWDecoderVersion](../cirawdecoderversion.md)
- [contrastSupported](iscontrastsupported.md) — A Boolean that indicates if the current image supports contrast adjustments.
- [detailSupported](isdetailsupported.md) — A Boolean that indicates if the current image supports detail enhancement adjustments.
- [lensCorrectionSupported](islenscorrectionsupported.md) — A Boolean that indicates if you can enable lens correction for the current image.
- [localToneMapSupported](islocaltonemapsupported.md) — A Boolean that indicates if the current image supports local tone curve adjustments.
- [luminanceNoiseReductionSupported](isluminancenoisereductionsupported.md) — A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [moireReductionSupported](ismoirereductionsupported.md) — A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [sharpnessSupported](issharpnesssupported.md) — A Boolean that indicates if the current image supports sharpness adjustments.
- [nativeSize](nativesize.md) — The full native size of the unscaled image.
