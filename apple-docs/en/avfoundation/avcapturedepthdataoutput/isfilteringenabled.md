---
title: isFilteringEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedepthdataoutput/isfilteringenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/isfilteringenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutput/isfilteringenabled.json'
content_hash: 'sha256:2a855c5a12aa0ed9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md)

# isFilteringEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the depth data output should filter depth data to smooth out noise and fill invalid values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isFilteringEnabled: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md) (the default), the capture output smooths noise and fills in missing or invalid values (caused by low light or lens occlusion) in depth data maps by temporally interpolating between previous and subsequent frames of captured depth data.

Filtering depth data makes it more useful for applying visual effects to a companion image, but alters the data such that it may no longer be suitable for computer vision tasks. (In an unfiltered depth map, missing values are represented as `NaN`.)

## See Also

### Configuring depth data capture

- [alwaysDiscardsLateDepthData](alwaysdiscardslatedepthdata.md) — A Boolean value that determines whether the capture output should discard any depth data that is not processed before the next depth data is captured.
