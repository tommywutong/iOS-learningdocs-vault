---
title: CIDetectorMaxFeatureCount
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectormaxfeaturecount
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectormaxfeaturecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectormaxfeaturecount.json'
content_hash: 'sha256:48eace172cca6b03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorMaxFeatureCount

<sub>Global Variable</sub>

The key to the configuration dictionary whose value represents the maximum number of features the detector should return.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorMaxFeatureCount: String
```

## Discussion

The default value is 1.  Valid values fall between 1 and 256 inclusive.

## See Also

### Constants

- [CIDetectorAccuracy](cidetectoraccuracy.md) — A key used to specify the desired accuracy for the detector.
- [CIDetectorTracking](cidetectortracking.md) — A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [CIDetectorMinFeatureSize](cidetectorminfeaturesize.md) — A key used to specify the minimum size that the detector will recognize as a feature.
- [CIDetectorNumberOfAngles](cidetectornumberofangles.md) — The number of perspectives to use for detecting a face in video input.
