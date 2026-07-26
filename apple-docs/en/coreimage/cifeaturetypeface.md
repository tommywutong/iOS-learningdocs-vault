---
title: CIFeatureTypeFace
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeaturetypeface
source_url: 'https://developer.apple.com/documentation/coreimage/cifeaturetypeface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeaturetypeface.json'
content_hash: 'sha256:d9d737a93b40b5d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFeatureTypeFace

<sub>Global Variable</sub>

A Core Image feature type for person’s face.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIFeatureTypeFace: String
```

## Discussion

To detect faces in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [CIFaceFeature](cifacefeature.md) class to find more information about the detected face.

## See Also

### Feature Types

- [CIFeatureTypeRectangle](cifeaturetyperectangle.md) — A Core Image feature type for rectangular object.
- [CIFeatureTypeQRCode](cifeaturetypeqrcode.md) — A Core Image feature type for QR code object.
- [CIFeatureTypeText](cifeaturetypetext.md) — A Core Image feature type for text.
