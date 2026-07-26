---
title: AVAssetImageGenerator.DynamicRangePolicy
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct.json'
content_hash: 'sha256:1d6aaf10558b1ec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# AVAssetImageGenerator.DynamicRangePolicy

<sub>Structure</sub>

A type that specifies the dynamic range policy to apply when generating images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct DynamicRangePolicy
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Policies

- [AVAssetImageGeneratorDynamicRangePolicyForceSDR](dynamicrangepolicy-swift.struct/forcesdr.md) — A policy that forces conversion to standard dynamic range.
- [AVAssetImageGeneratorDynamicRangePolicyMatchSource](dynamicrangepolicy-swift.struct/matchsource.md) — A policy that preserves the color parameters of the source media.

### Initializers

- [init(rawValue:)](<dynamicrangepolicy-swift.struct/init(rawvalue_).md>)

## See Also

### Configuring image generation

- [maximumSize](maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceBefore](requestedtimetolerancebefore.md) — A maximum length of time before the requested time to allow image generation to occur.
- [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [dynamicRangePolicy](dynamicrangepolicy-swift.property.md) — The dynamic range policy to use when generating images.
- [appliesPreferredTrackTransform](appliespreferredtracktransform.md) — A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [apertureMode](aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
- [ApertureMode](aperturemode-swift.struct.md) — Constants that define aperture modes to use when generating images.
