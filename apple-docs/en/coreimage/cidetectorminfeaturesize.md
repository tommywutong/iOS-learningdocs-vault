---
title: CIDetectorMinFeatureSize
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectorminfeaturesize
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectorminfeaturesize.json'
content_hash: 'sha256:3579da06d6598269'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorMinFeatureSize

<sub>Global Variable</sub>

A key used to specify the minimum size that the detector will recognize as a feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorMinFeatureSize: String
```

## Discussion

The value for this key is an `NSNumber` object ranging from 0.0 through 1.0 that represents a fraction of the minor dimension of the image.

## See Also

### Constants

- [CIDetectorAccuracy](cidetectoraccuracy.md) — A key used to specify the desired accuracy for the detector.
- [CIDetectorTracking](cidetectortracking.md) — A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [CIDetectorNumberOfAngles](cidetectornumberofangles.md) — The number of perspectives to use for detecting a face in video input.
- [CIDetectorMaxFeatureCount](cidetectormaxfeaturecount.md) — The key to the configuration dictionary whose value represents the maximum number of features the detector should return.
