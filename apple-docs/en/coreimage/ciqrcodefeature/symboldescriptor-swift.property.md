---
title: symbolDescriptor
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodefeature/symboldescriptor-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodefeature/symboldescriptor-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodefeature/symboldescriptor-swift.property.json'
content_hash: 'sha256:6900a48b50d31c23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeFeature](../ciqrcodefeature.md)

# symbolDescriptor

<sub>Instance Property</sub>

An abstract representation of a QR Code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var symbolDescriptor: CIQRCodeDescriptor? { get }
```

## Discussion

The property is a [CIQRCodeDescriptor](../ciqrcodedescriptor.md) instance that contains the payload, symbol version, mask pattern, and error correction level, so the QR Code can be reproduced.

## See Also

### Decoding a Detected Barcode

- [messageString](messagestring.md) — The string decoded from the detected barcode.
