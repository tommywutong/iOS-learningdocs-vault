---
title: CIDetectorTypeRectangle
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetectortyperectangle
source_url: 'https://developer.apple.com/documentation/coreimage/cidetectortyperectangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetectortyperectangle.json'
content_hash: 'sha256:d0d966257a6e7c5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetectorTypeRectangle

<sub>Global Variable</sub>

A detector that searches for rectangular areas in a still image or video, returning [CIRectangleFeature](cirectanglefeature.md) objects that provide information about detected regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIDetectorTypeRectangle: String
```

## Discussion

The rectangle detector finds areas that are likely to represent rectangular objects that appear in perspective in the image, such as papers or books seen on a desktop.

## See Also

### Constants

- [CIDetectorTypeFace](cidetectortypeface.md) — A detector that searches for faces in a still image or video, returning [CIFaceFeature](cifacefeature.md) objects that provide information about detected faces.
- [CIDetectorTypeQRCode](cidetectortypeqrcode.md) — A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [CIQRCodeFeature](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [CIDetectorTypeText](cidetectortypetext.md) — A detector that searches for text in a still image or video, returning [CITextFeature](citextfeature.md) objects that provide information about detected regions.
