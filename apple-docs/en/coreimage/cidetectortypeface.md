---
title: CIDetectorTypeFace
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectortypeface
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectortypeface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectortypeface.json'
content_hash: 'sha256:8d0e54f94332c785'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorTypeFace

<sub>Global Variable</sub>

A detector that searches for faces in a still image or video, returning [CIFaceFeature](cifacefeature.md) objects that provide information about detected faces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorTypeFace: String
```

## Discussion

For better accuracy and performance in face detection, use the [CIDetectorImageOrientation](cidetectorimageorientation.md) key to specify the image orientation when using the [- featuresInImage:options:](<cidetector/features(in_options_).md>) method.

## See Also

### Constants

- [CIDetectorTypeRectangle](cidetectortyperectangle.md) — A detector that searches for rectangular areas in a still image or video, returning [CIRectangleFeature](cirectanglefeature.md) objects that provide information about detected regions.
- [CIDetectorTypeQRCode](cidetectortypeqrcode.md) — A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [CIQRCodeFeature](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [CIDetectorTypeText](cidetectortypetext.md) — A detector that searches for text in a still image or video, returning [CITextFeature](citextfeature.md) objects that provide information about detected regions.
