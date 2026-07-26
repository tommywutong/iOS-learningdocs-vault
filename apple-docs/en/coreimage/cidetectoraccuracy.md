---
title: CIDetectorAccuracy
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectoraccuracy
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectoraccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectoraccuracy.json'
content_hash: 'sha256:aedda46e0041ed8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorAccuracy

<sub>Global Variable</sub>

A key used to specify the desired accuracy for the detector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorAccuracy: String
```

## Discussion

The value associated with the key should be one of the values found in [Detector Accuracy Options](detector-accuracy-options.md).

## See Also

### Constants

- [CIDetectorTracking](cidetectortracking.md) — A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [CIDetectorMinFeatureSize](cidetectorminfeaturesize.md) — A key used to specify the minimum size that the detector will recognize as a feature.
- [CIDetectorNumberOfAngles](cidetectornumberofangles.md) — The number of perspectives to use for detecting a face in video input.
- [CIDetectorMaxFeatureCount](cidetectormaxfeaturecount.md) — The key to the configuration dictionary whose value represents the maximum number of features the detector should return.
