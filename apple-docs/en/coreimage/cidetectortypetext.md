---
title: CIDetectorTypeText
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectortypetext
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectortypetext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectortypetext.json'
content_hash: 'sha256:bcade2c0502ee6b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorTypeText

<sub>Global Variable</sub>

A detector that searches for text in a still image or video, returning [CITextFeature](citextfeature.md) objects that provide information about detected regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorTypeText: String
```

## Discussion

The text detector finds areas that are likely to contain upright text, but does not perform optical character recognition.

## See Also

### Constants

- [CIDetectorTypeFace](cidetectortypeface.md) — A detector that searches for faces in a still image or video, returning [CIFaceFeature](cifacefeature.md) objects that provide information about detected faces.
- [CIDetectorTypeRectangle](cidetectortyperectangle.md) — A detector that searches for rectangular areas in a still image or video, returning [CIRectangleFeature](cirectanglefeature.md) objects that provide information about detected regions.
- [CIDetectorTypeQRCode](cidetectortypeqrcode.md) — A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [CIQRCodeFeature](ciqrcodefeature.md) objects that provide information about detected barcodes.
