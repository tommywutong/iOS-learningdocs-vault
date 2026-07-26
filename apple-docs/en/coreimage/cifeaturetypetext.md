---
title: CIFeatureTypeText
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeaturetypetext
source_url: 'https://developer.apple.com/documentation/coreimage/cifeaturetypetext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeaturetypetext.json'
content_hash: 'sha256:e7f58583e2be4950'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFeatureTypeText

<sub>Global Variable</sub>

A Core Image feature type for text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIFeatureTypeText: String
```

## Discussion

To detect text in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [CITextFeature](citextfeature.md) class to find more information about the detected text.

## See Also

### Feature Types

- [CIFeatureTypeFace](cifeaturetypeface.md) — A Core Image feature type for person’s face.
- [CIFeatureTypeRectangle](cifeaturetyperectangle.md) — A Core Image feature type for rectangular object.
- [CIFeatureTypeQRCode](cifeaturetypeqrcode.md) — A Core Image feature type for QR code object.
