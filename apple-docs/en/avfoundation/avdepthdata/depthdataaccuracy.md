---
title: depthDataAccuracy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/depthdataaccuracy
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/depthdataaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/depthdataaccuracy.json'
content_hash: 'sha256:1bd4fd794432143f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# depthDataAccuracy

<sub>Instance Property</sub>

The general accuracy of depth data map values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthDataAccuracy: AVDepthData.Accuracy { get }
```

## Discussion

The accuracy of a depth data map is highly dependent on the camera calibration data used to generate it. If the camera’s focal length cannot be precisely determined at the time of capture, a scaling error in the z (depth) plane is introduced. If the camera’s optical center can’t be precisely determined at capture time, a principal point error is introduced, leading to an offset error in the disparity estimate. [Accuracy](accuracy.md) constants report the accuracy of a map’s values with respect to its reported units.

## See Also

### Evaluating depth data

- [depthDataFiltered](isdepthdatafiltered.md) — A Boolean value indicating whether the depth map contains temporally smoothed data.
- [Accuracy](accuracy.md) — Values indicating the general accuracy of a depth data map.
- [depthDataQuality](depthdataquality.md) — The overall quality of the depth map.
- [Quality](quality.md) — Values indicating the overall quality of a depth data map.
