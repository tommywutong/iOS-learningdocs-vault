---
title: AVDepthData.Accuracy
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/accuracy
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/accuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/accuracy.json'
content_hash: 'sha256:169149bd59930684'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# AVDepthData.Accuracy

<sub>Enumeration</sub>

Values indicating the general accuracy of a depth data map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Accuracy
```

## Overview

The accuracy of a depth data map is highly dependent on the camera calibration data used to generate it. If the camera’s focal length cannot be precisely determined at the time of capture, a scaling error in the z (depth) plane is introduced. If the camera’s optical center can’t be precisely determined at capture time, a principal point error is introduced, leading to an offset error in the disparity estimate.

These values report the accuracy of a map’s values with respect to its reported units.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accuracy values

- [AVDepthDataAccuracyRelative](accuracy/relative.md) — Values within the depth data map are usable for foreground/background separation, but are not absolutely accurate in the physical world.
- [AVDepthDataAccuracyAbsolute](accuracy/absolute.md) — Values within the depth map are absolutely accurate within the physical world.

### Initializers

- [init(rawValue:)](<accuracy/init(rawvalue_).md>)

## See Also

### Evaluating depth data

- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value indicating whether the depth map contains temporally smoothed data.
- [depthDataAccuracy](depthdataaccuracy.md) — The general accuracy of depth data map values.
- [depthDataQuality](depthdataquality.md) — The overall quality of the depth map.
- [Quality](quality.md) — Values indicating the overall quality of a depth data map.
