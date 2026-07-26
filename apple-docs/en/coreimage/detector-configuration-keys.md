---
title: Detector Configuration Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/detector-configuration-keys
source_url: 'https://developer.apple.com/documentation/coreimage/detector-configuration-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/detector-configuration-keys.json'
content_hash: 'sha256:79b87a149c7a51dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIDetector](cidetector.md)

# Detector Configuration Keys

<sub>API Collection</sub>

Keys used in the options dictionary to configure a detector.

## Topics

### Constants

- [CIDetectorAccuracy](cidetectoraccuracy.md) — A key used to specify the desired accuracy for the detector.
- [CIDetectorTracking](cidetectortracking.md) — A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [CIDetectorMinFeatureSize](cidetectorminfeaturesize.md) — A key used to specify the minimum size that the detector will recognize as a feature.
- [CIDetectorNumberOfAngles](cidetectornumberofangles.md) — The number of perspectives to use for detecting a face in video input.
- [CIDetectorMaxFeatureCount](cidetectormaxfeaturecount.md) — The key to the configuration dictionary whose value represents the maximum number of features the detector should return.

## See Also

### Constants

- [Detector Types](detector-types.md) — Strings used to declare the detector for which you are interested.
- [Detector Accuracy Options](detector-accuracy-options.md) — Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md) — Keys used in the options dictionary for [- featuresInImage:options:](<cidetector/features(in_options_).md>).
