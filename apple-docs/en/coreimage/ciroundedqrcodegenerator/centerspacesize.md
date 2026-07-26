---
title: centerSpaceSize
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciroundedqrcodegenerator/centerspacesize
source_url: 'https://developer.apple.com/documentation/coreimage/ciroundedqrcodegenerator/centerspacesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciroundedqrcodegenerator/centerspacesize.json'
content_hash: 'sha256:76e32f00b375d548'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRoundedQRCodeGenerator](../ciroundedqrcodegenerator.md)

# centerSpaceSize

<sub>Instance Property</sub>

The fraction of the center space of the QRCode to fill with Color 1. If the size is 0.0 or the Correction Level is L or M, the center of the QRCode will be unaltered. The size will be limited to 0.25 if the Correction Level is Q. The size will be limited to 0.33 if the Correction Level is H.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var centerSpaceSize: Float { get set }
```
