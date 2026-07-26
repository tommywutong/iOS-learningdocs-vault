---
title: AVDepthData.Quality.low
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/quality/low
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/quality/low'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/quality/low.json'
content_hash: 'sha256:654dc079a6cc7212'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVDepthData](../../avdepthdata.md) · [Quality](../quality.md)

# AVDepthData.Quality.low

<sub>Case</sub>

The depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case low
```

## Discussion

Low quality occurs when the process generating the depth map (such as inference of depth from disparity on a device with dual cameras) cannot find enough distinct key points in the input images, resulting in a large number of invalid depth values in the (pre-filtered) map.

## See Also

### Depth quality values

- [AVDepthDataQualityHigh](high.md) — The depth map is a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.
