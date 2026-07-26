---
title: Detector Types
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/detector-types
source_url: 'https://developer.apple.com/documentation/coreimage/detector-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/detector-types.json'
content_hash: 'sha256:b80e515455945544'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIDetector](cidetector.md)

# Detector Types

<sub>API Collection</sub>

Strings used to declare the detector for which you are interested.

## Topics

### Constants

- [CIDetectorTypeFace](cidetectortypeface.md) — A detector that searches for faces in a still image or video, returning [CIFaceFeature](cifacefeature.md) objects that provide information about detected faces.
- [CIDetectorTypeRectangle](cidetectortyperectangle.md) — A detector that searches for rectangular areas in a still image or video, returning [CIRectangleFeature](cirectanglefeature.md) objects that provide information about detected regions.
- [CIDetectorTypeQRCode](cidetectortypeqrcode.md) — A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [CIQRCodeFeature](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [CIDetectorTypeText](cidetectortypetext.md) — A detector that searches for text in a still image or video, returning [CITextFeature](citextfeature.md) objects that provide information about detected regions.

## See Also

### Constants

- [Detector Configuration Keys](detector-configuration-keys.md) — Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md) — Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md) — Keys used in the options dictionary for [- featuresInImage:options:](<cidetector/features(in_options_).md>).
