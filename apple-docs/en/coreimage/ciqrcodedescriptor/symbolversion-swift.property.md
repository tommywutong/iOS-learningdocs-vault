---
title: symbolVersion
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodedescriptor/symbolversion-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/symbolversion-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor/symbolversion-swift.property.json'
content_hash: 'sha256:3790773b829d92da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeDescriptor](../ciqrcodedescriptor.md)

# symbolVersion

<sub>Instance Property</sub>

The version of the QR code which corresponds to the size of the QR code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var symbolVersion: Int { get }
```

## Discussion

ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity. This field is required in order to properly interpret the error corrected payload.

## See Also

### Examining a Descriptor

- [errorCorrectedPayload](errorcorrectedpayload-swift.property.md) — The error-corrected codeword payload that comprises the QR code symbol.
- [maskPattern](maskpattern-swift.property.md) — The data mask pattern for the QR code symbol.
- [errorCorrectionLevel](errorcorrectionlevel-swift.property.md) — The error correction level of the QR code symbol.
