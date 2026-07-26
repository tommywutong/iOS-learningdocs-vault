---
title: CIDetectorNumberOfAngles
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectornumberofangles
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectornumberofangles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectornumberofangles.json'
content_hash: 'sha256:473c44f21f2fefe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorNumberOfAngles

<sub>Global Variable</sub>

The number of perspectives to use for detecting a face in video input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorNumberOfAngles: String
```

## Discussion

The value for this key is an `NSNumber` object containing the number 1, 3, 5, 7, 9, or 11. At higher numbers of angles, face detection in video becomes more accurate, but at a higher computational cost.

## See Also

### Constants

- [CIDetectorAccuracy](cidetectoraccuracy.md) — A key used to specify the desired accuracy for the detector.
- [CIDetectorTracking](cidetectortracking.md) — A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [CIDetectorMinFeatureSize](cidetectorminfeaturesize.md) — A key used to specify the minimum size that the detector will recognize as a feature.
- [CIDetectorMaxFeatureCount](cidetectormaxfeaturecount.md) — The key to the configuration dictionary whose value represents the maximum number of features the detector should return.
