---
title: CIFeatureTypeRectangle
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeaturetyperectangle
source_url: 'https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeaturetyperectangle.json'
content_hash: 'sha256:cbf71d68a889a503'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFeatureTypeRectangle

<sub>Global Variable</sub>

A Core Image feature type for rectangular object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let CIFeatureTypeRectangle: String
```

## Discussion

To detect rectangles in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [CIRectangleFeature](cirectanglefeature.md) class to find more information about the detected rectangle.

## See Also

### Feature Types

- [CIFeatureTypeFace](cifeaturetypeface.md) — A Core Image feature type for person’s face.
- [CIFeatureTypeQRCode](cifeaturetypeqrcode.md) — A Core Image feature type for QR code object.
- [CIFeatureTypeText](cifeaturetypetext.md) — A Core Image feature type for text.
