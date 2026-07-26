---
title: maskPattern
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodedescriptor/maskpattern-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/maskpattern-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor/maskpattern-swift.property.json'
content_hash: 'sha256:75160eae468e620d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeDescriptor](../ciqrcodedescriptor.md)

# maskPattern

<sub>Instance Property</sub>

The data mask pattern for the QR code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maskPattern: UInt8 { get }
```

## Discussion

QR Codes support eight data mask patterns, which are used to avoid large black or large white areas inside the symbol body. Valid values range from 0 to 7.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected codeword payload that comprises the QR code symbol.
- [symbolVersion](symbolversion-swift.property.md) — The version of the QR code which corresponds to the size of the QR code symbol.
- [errorCorrectionLevel](errorcorrectionlevel-swift.property.md) — The error correction level of the QR code symbol.
