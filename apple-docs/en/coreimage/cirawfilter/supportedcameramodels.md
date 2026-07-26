---
title: supportedCameraModels
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawfilter/supportedcameramodels
source_url: 'https://developer.apple.com/documentation/coreimage/cirawfilter/supportedcameramodels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawfilter/supportedcameramodels.json'
content_hash: 'sha256:c5bc32a99e452d78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRAWFilter](../cirawfilter.md)

# supportedCameraModels

<sub>Type Property</sub>

An array containing the names of all supported camera models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class var supportedCameraModels: [String] { get }
```

## See Also

### Inspecting supported camera models, decoders, and filters

- [supportedDecoderVersions](supporteddecoderversions.md) — An array of all supported decoder versions for the given image type.
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
