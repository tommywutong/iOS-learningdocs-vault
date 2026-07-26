---
title: isDepthDataFiltered
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/isdepthdatafiltered
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/isdepthdatafiltered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/isdepthdatafiltered.json'
content_hash: 'sha256:b3f5c39d0c3cca93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# isDepthDataFiltered

<sub>Instance Property</sub>

A Boolean value indicating whether the depth map contains temporally smoothed data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isDepthDataFiltered: Bool { get }
```

## Discussion

The capture system can smooth noise and fill in missing values (caused by low light or lens occlusion) in depth data maps by temporally interpolating between previous and subsequent frames of captured depth data. Use the [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) [filteringEnabled](../avcapturedepthdataoutput/isfilteringenabled.md) property to control filtering for streaming depth capture, or the [AVCapturePhotoSettings](../avcapturephotosettings.md) [depthDataFiltered](isdepthdatafiltered.md) property to control filtering for depth data captured alongside photo capture.

Filtering depth data makes it more useful for applying visual effects to a companion image, but alters the data such that it may no longer be suitable for computer vision tasks. (In an unfiltered depth map, missing values are represented as `NaN`.)

## See Also

### Evaluating depth data

- [depthDataAccuracy](depthdataaccuracy.md) — The general accuracy of depth data map values.
- [Accuracy](accuracy.md) — Values indicating the general accuracy of a depth data map.
- [depthDataQuality](depthdataquality.md) — The overall quality of the depth map.
- [Quality](quality.md) — Values indicating the overall quality of a depth data map.
