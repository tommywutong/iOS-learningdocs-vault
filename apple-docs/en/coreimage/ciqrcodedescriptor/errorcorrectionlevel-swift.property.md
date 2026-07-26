---
title: errorCorrectionLevel
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property.json'
content_hash: 'sha256:233825cf101c84a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeDescriptor](../ciqrcodedescriptor.md)

# errorCorrectionLevel

<sub>Instance Property</sub>

The error correction level of the QR code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel { get }
```

## Discussion

QR Codes support four levels of Reed-Solomon error correction.

The possible error correction levels are enumerated in [ECCVersion](../cidatamatrixcodedescriptor/eccversion-swift.enum.md).

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected codeword payload that comprises the QR code symbol.
- [symbolVersion](symbolversion-swift.property.md) — The version of the QR code which corresponds to the size of the QR code symbol.
- [maskPattern](maskpattern-swift.property.md) — The data mask pattern for the QR code symbol.
