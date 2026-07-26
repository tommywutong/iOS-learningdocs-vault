---
title: supportedDecoderVersions
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/supporteddecoderversions
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/supporteddecoderversions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/supporteddecoderversions.json'
content_hash: 'sha256:dd7e3edb189daeed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# supportedDecoderVersions

<sub>Instance Property</sub>

An array of all supported decoder versions for the given image type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportedDecoderVersions: [CIRAWDecoderVersion] { get }
```

## Discussion

This array is sorted in reverse chronological order. All entries represent a valid version identifier set to [decoderVersion](decoderversion.md).

## See Also

### Inspecting supported camera models, decoders, and filters

- [supportedCameraModels](supportedcameramodels.md) — An array containing the names of all supported camera models.
- [CIRAWDecoderVersion](../cirawdecoderversion.md)
- [colorNoiseReductionSupported](iscolornoisereductionsupported.md) — A Boolean that indicates if the current image supports color noise reduction adjustments.
- [contrastSupported](iscontrastsupported.md) — A Boolean that indicates if the current image supports contrast adjustments.
- [detailSupported](isdetailsupported.md) — A Boolean that indicates if the current image supports detail enhancement adjustments.
- [lensCorrectionSupported](islenscorrectionsupported.md) — A Boolean that indicates if you can enable lens correction for the current image.
- [localToneMapSupported](islocaltonemapsupported.md) — A Boolean that indicates if the current image supports local tone curve adjustments.
- [luminanceNoiseReductionSupported](isluminancenoisereductionsupported.md) — A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [moireReductionSupported](ismoirereductionsupported.md) — A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [sharpnessSupported](issharpnesssupported.md) — A Boolean that indicates if the current image supports sharpness adjustments.
- [nativeSize](nativesize.md) — The full native size of the unscaled image.
