---
title: CIRAWDecoderVersion
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirawdecoderversion
source_url: 'https://developer.apple.com/documentation/coreimage/cirawdecoderversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirawdecoderversion.json'
content_hash: 'sha256:7d16277c75c67f1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRAWDecoderVersion

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIRAWDecoderVersion
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<cirawdecoderversion/init(rawvalue_).md>)

### Type Properties

- [CIRAWDecoderVersionNone](cirawdecoderversion/none.md)
- [CIRAWDecoderVersion6](cirawdecoderversion/version6.md)
- [CIRAWDecoderVersion6DNG](cirawdecoderversion/version6dng.md)
- [CIRAWDecoderVersion7](cirawdecoderversion/version7.md)
- [CIRAWDecoderVersion7DNG](cirawdecoderversion/version7dng.md)
- [CIRAWDecoderVersion8](cirawdecoderversion/version8.md)
- [CIRAWDecoderVersion8DNG](cirawdecoderversion/version8dng.md)
- [CIRAWDecoderVersion9](cirawdecoderversion/version9.md)
- [CIRAWDecoderVersion9DNG](cirawdecoderversion/version9dng.md)

## See Also

### Inspecting supported camera models, decoders, and filters

- [supportedCameraModels](cirawfilter/supportedcameramodels.md) — An array containing the names of all supported camera models.
- [supportedDecoderVersions](cirawfilter/supporteddecoderversions.md) — An array of all supported decoder versions for the given image type.
- [colorNoiseReductionSupported](cirawfilter/iscolornoisereductionsupported.md) — A Boolean that indicates if the current image supports color noise reduction adjustments.
- [contrastSupported](cirawfilter/iscontrastsupported.md) — A Boolean that indicates if the current image supports contrast adjustments.
- [detailSupported](cirawfilter/isdetailsupported.md) — A Boolean that indicates if the current image supports detail enhancement adjustments.
- [lensCorrectionSupported](cirawfilter/islenscorrectionsupported.md) — A Boolean that indicates if you can enable lens correction for the current image.
- [localToneMapSupported](cirawfilter/islocaltonemapsupported.md) — A Boolean that indicates if the current image supports local tone curve adjustments.
- [luminanceNoiseReductionSupported](cirawfilter/isluminancenoisereductionsupported.md) — A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [moireReductionSupported](cirawfilter/ismoirereductionsupported.md) — A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [sharpnessSupported](cirawfilter/issharpnesssupported.md) — A Boolean that indicates if the current image supports sharpness adjustments.
- [nativeSize](cirawfilter/nativesize.md) — The full native size of the unscaled image.
