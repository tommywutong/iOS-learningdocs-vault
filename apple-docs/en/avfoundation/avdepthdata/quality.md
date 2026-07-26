---
title: AVDepthData.Quality
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/quality
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/quality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/quality.json'
content_hash: 'sha256:6522a241490b37bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# AVDepthData.Quality

<sub>Enumeration</sub>

Values indicating the overall quality of a depth data map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Quality
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Depth quality values

- [AVDepthDataQualityLow](quality/low.md) — The depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene.
- [AVDepthDataQualityHigh](quality/high.md) — The depth map is a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.

### Initializers

- [init(rawValue:)](<quality/init(rawvalue_).md>)

## See Also

### Evaluating depth data

- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value indicating whether the depth map contains temporally smoothed data.
- [depthDataAccuracy](depthdataaccuracy.md) — The general accuracy of depth data map values.
- [Accuracy](accuracy.md) — Values indicating the general accuracy of a depth data map.
- [depthDataQuality](depthdataquality.md) — The overall quality of the depth map.
