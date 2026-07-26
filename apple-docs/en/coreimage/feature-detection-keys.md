---
title: Feature Detection Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/feature-detection-keys
source_url: 'https://developer.apple.com/documentation/coreimage/feature-detection-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/feature-detection-keys.json'
content_hash: 'sha256:9c5a97c54dafc9a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIDetector](cidetector.md)

# Feature Detection Keys

<sub>API Collection</sub>

Keys used in the options dictionary for [- featuresInImage:options:](<cidetector/features(in_options_).md>).

## Topics

### Constants

- [CIDetectorImageOrientation](cidetectorimageorientation.md) — An option for the display orientation of the image whose features you want to detect.
- [CIDetectorEyeBlink](cidetectoreyeblink.md) — An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [CIDetectorSmile](cidetectorsmile.md) — An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [CIDetectorFocalLength](cidetectorfocallength.md) — An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [CIDetectorAspectRatio](cidetectoraspectratio.md) — An option specifying the aspect ratio (width divided by height) of rectangles to search for.
- [CIDetectorReturnSubFeatures](cidetectorreturnsubfeatures.md) — An option specifying whether to return feature information for components of detected features.

## See Also

### Constants

- [Detector Types](detector-types.md) — Strings used to declare the detector for which you are interested.
- [Detector Configuration Keys](detector-configuration-keys.md) — Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md) — Value options used to specify the desired accuracy of the detector.
