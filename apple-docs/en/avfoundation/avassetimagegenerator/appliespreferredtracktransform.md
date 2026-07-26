---
title: appliesPreferredTrackTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/appliespreferredtracktransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/appliespreferredtracktransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/appliespreferredtracktransform.json'
content_hash: 'sha256:d46a25e1a774de9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# appliesPreferredTrackTransform

<sub>Instance Property</sub>

A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var appliesPreferredTrackTransform: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). This class only supports rotation by 90, 180, or 270 degrees.

The image generator ignores this property if you set a value for the [videoComposition](videocomposition.md) property.

## See Also

### Configuring image generation

- [maximumSize](maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceBefore](requestedtimetolerancebefore.md) — A maximum length of time before the requested time to allow image generation to occur.
- [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [dynamicRangePolicy](dynamicrangepolicy-swift.property.md) — The dynamic range policy to use when generating images.
- [DynamicRangePolicy](dynamicrangepolicy-swift.struct.md) — A type that specifies the dynamic range policy to apply when generating images.
- [apertureMode](aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
- [ApertureMode](aperturemode-swift.struct.md) — Constants that define aperture modes to use when generating images.
