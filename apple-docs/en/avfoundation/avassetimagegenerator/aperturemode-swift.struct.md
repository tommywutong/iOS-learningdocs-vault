---
title: AVAssetImageGenerator.ApertureMode
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct.json'
content_hash: 'sha256:6666cf86877112cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# AVAssetImageGenerator.ApertureMode

<sub>Structure</sub>

Constants that define aperture modes to use when generating images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct ApertureMode
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Aperture modes

- [AVAssetImageGeneratorApertureModeCleanAperture](aperturemode-swift.struct/cleanaperture.md) — A mode that applies both pixel aspect ratio and clean aperture.
- [AVAssetImageGeneratorApertureModeEncodedPixels](aperturemode-swift.struct/encodedpixels.md) — A mode that applies neither pixel aspect ratio nor clean aperture.
- [AVAssetImageGeneratorApertureModeProductionAperture](aperturemode-swift.struct/productionaperture.md) — A mode that applies only pixel aspect ratio.

### Initializers

- [init(rawValue:)](<aperturemode-swift.struct/init(rawvalue_).md>) — Creates an aperture mode with a string value.

## See Also

### Configuring image generation

- [maximumSize](maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceBefore](requestedtimetolerancebefore.md) — A maximum length of time before the requested time to allow image generation to occur.
- [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [dynamicRangePolicy](dynamicrangepolicy-swift.property.md) — The dynamic range policy to use when generating images.
- [DynamicRangePolicy](dynamicrangepolicy-swift.struct.md) — A type that specifies the dynamic range policy to apply when generating images.
- [appliesPreferredTrackTransform](appliespreferredtracktransform.md) — A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [apertureMode](aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
