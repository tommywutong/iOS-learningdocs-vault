---
title: CIFeatureTypeQRCode
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeaturetypeqrcode
source_url: 'https://developer.apple.com/documentation/coreimage/cifeaturetypeqrcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeaturetypeqrcode.json'
content_hash: 'sha256:898821b51f8ee07b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFeatureTypeQRCode

<sub>Global Variable</sub>

A Core Image feature type for QR code object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIFeatureTypeQRCode: String
```

## Discussion

To detect QR codes in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [CIQRCodeFeature](ciqrcodefeature.md) class to find more information about the detected QR code.

## See Also

### Feature Types

- [CIFeatureTypeFace](cifeaturetypeface.md) — A Core Image feature type for person’s face.
- [CIFeatureTypeRectangle](cifeaturetyperectangle.md) — A Core Image feature type for rectangular object.
- [CIFeatureTypeText](cifeaturetypetext.md) — A Core Image feature type for text.
