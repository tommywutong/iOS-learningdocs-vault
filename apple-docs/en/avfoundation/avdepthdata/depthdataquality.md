---
title: depthDataQuality
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/depthdataquality
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/depthdataquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/depthdataquality.json'
content_hash: 'sha256:ff7aef24e1525297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# depthDataQuality

<sub>Instance Property</sub>

The overall quality of the depth map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthDataQuality: AVDepthData.Quality { get }
```

## Discussion

A device typically generates depth data maps by comparing images and calculating disparity. If features are lacking in either input image, it may be difficult to find matching key points, resulting in a depth data map with substantial holes. These holes can be filled with depth data filtering, but still may produce a map of overall poor quality.

If a depth data map suffers from insufficient features, the capture system marks it as [AVDepthDataQualityLow](quality/low.md) quality, indicating that the depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene. A depth map with [AVDepthDataQualityHigh](quality/high.md) quality is feature-rich, contains a high level of detail, making it a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.

## See Also

### Evaluating depth data

- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value indicating whether the depth map contains temporally smoothed data.
- [depthDataAccuracy](depthdataaccuracy.md) — The general accuracy of depth data map values.
- [Accuracy](accuracy.md) — Values indicating the general accuracy of a depth data map.
- [Quality](quality.md) — Values indicating the overall quality of a depth data map.
