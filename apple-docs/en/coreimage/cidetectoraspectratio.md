---
title: CIDetectorAspectRatio
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectoraspectratio
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectoraspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectoraspectratio.json'
content_hash: 'sha256:3451401f0a4bedfd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorAspectRatio

<sub>Global Variable</sub>

An option specifying the aspect ratio (width divided by height) of rectangles to search for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorAspectRatio: String
```

## Discussion

The value of this key is an [NSNumber](../foundation/nsnumber.md) object whose value is a positive floating-point number. Use this option with the [CIDetectorTypeRectangle](cidetectortyperectangle.md) detector type to fine-tune the accuracy of the detector. For example, to more accurately find a business card (3.5 x 2 inches) in an image, specify an aspect ratio of `1.75` (3.5 / 2).

## See Also

### Constants

- [CIDetectorImageOrientation](cidetectorimageorientation.md) — An option for the display orientation of the image whose features you want to detect.
- [CIDetectorEyeBlink](cidetectoreyeblink.md) — An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [CIDetectorSmile](cidetectorsmile.md) — An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [CIDetectorFocalLength](cidetectorfocallength.md) — An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [CIDetectorReturnSubFeatures](cidetectorreturnsubfeatures.md) — An option specifying whether to return feature information for components of detected features.
