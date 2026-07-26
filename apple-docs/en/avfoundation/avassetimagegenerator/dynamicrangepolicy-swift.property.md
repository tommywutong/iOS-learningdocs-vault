---
title: dynamicRangePolicy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.property.json'
content_hash: 'sha256:eae7d861888e8439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# dynamicRangePolicy

<sub>Instance Property</sub>

The dynamic range policy to use when generating images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy { get set }
```

## Discussion

This property defaults to [AVAssetImageGeneratorDynamicRangePolicyForceSDR](dynamicrangepolicy-swift.struct/forcesdr.md).

## See Also

### Configuring image generation

- [maximumSize](maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceBefore](requestedtimetolerancebefore.md) — A maximum length of time before the requested time to allow image generation to occur.
- [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [DynamicRangePolicy](dynamicrangepolicy-swift.struct.md) — A type that specifies the dynamic range policy to apply when generating images.
- [appliesPreferredTrackTransform](appliespreferredtracktransform.md) — A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [apertureMode](aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
- [ApertureMode](aperturemode-swift.struct.md) — Constants that define aperture modes to use when generating images.
