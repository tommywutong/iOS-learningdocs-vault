---
title: 'descriptorWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciqrcodedescriptor/descriptorwithpayload:symbolversion:maskpattern:errorcorrectionlevel:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/descriptorwithpayload:symbolversion:maskpattern:errorcorrectionlevel:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor/descriptorwithpayload%3Asymbolversion%3Amaskpattern%3Aerrorcorrectionlevel%3A.json'
content_hash: 'sha256:4ee9511dbb83e839'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeDescriptor](../ciqrcodedescriptor.md)

# descriptorWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:

<sub>Type Method</sub>

Creates a QR code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload symbolVersion:(NSInteger) symbolVersion maskPattern:(uint8_t) maskPattern errorCorrectionLevel:(CIQRCodeErrorCorrectionLevel) errorCorrectionLevel;
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the QR code symbol.

- `symbolVersion` — The symbol version, from 1 through 40.

- `maskPattern` — The mask pattern to use in the QR code, from 0 to 7.

- `errorCorrectionLevel` — The QR code’s error correction level: L, M, Q, or H.

## Return Value

An autoreleased [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## See Also

### Creating a Descriptor

- [- initWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:](<init(payload_symbolversion_maskpattern_errorcorrectionlevel_).md>) — Initializes a QR code descriptor for the given payload and parameters.
