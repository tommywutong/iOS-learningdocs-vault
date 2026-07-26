---
title: requestedTimeToleranceBefore
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/requestedtimetolerancebefore
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/requestedtimetolerancebefore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/requestedtimetolerancebefore.json'
content_hash: 'sha256:e14c17f791bda389'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# requestedTimeToleranceBefore

<sub>Instance Property</sub>

A maximum length of time before the requested time to allow image generation to occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requestedTimeToleranceBefore: CMTime { get set }
```

## Discussion

The default value is [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md). Set the values of [requestedTimeToleranceBefore](requestedtimetolerancebefore.md) and [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) to [zero](../../coremedia/cmtime/zero.md) to request frame-accurate image generation; this may incur additional decoding delay.

## See Also

### Configuring image generation

- [maximumSize](maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceAfter](requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [dynamicRangePolicy](dynamicrangepolicy-swift.property.md) — The dynamic range policy to use when generating images.
- [DynamicRangePolicy](dynamicrangepolicy-swift.struct.md) — A type that specifies the dynamic range policy to apply when generating images.
- [appliesPreferredTrackTransform](appliespreferredtracktransform.md) — A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [apertureMode](aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
- [ApertureMode](aperturemode-swift.struct.md) — Constants that define aperture modes to use when generating images.
