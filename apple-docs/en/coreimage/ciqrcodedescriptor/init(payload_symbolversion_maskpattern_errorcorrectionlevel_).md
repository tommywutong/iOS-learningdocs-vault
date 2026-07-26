---
title: 'init(payload:symbolVersion:maskPattern:errorCorrectionLevel:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciqrcodedescriptor/init(payload:symbolversion:maskpattern:errorcorrectionlevel:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/init(payload:symbolversion:maskpattern:errorcorrectionlevel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor/init%28payload%3Asymbolversion%3Amaskpattern%3Aerrorcorrectionlevel%3A%29.json'
content_hash: 'sha256:76fd99c51525dde5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIQRCodeDescriptor](../ciqrcodedescriptor.md)

# init(payload:symbolVersion:maskPattern:errorCorrectionLevel:)

<sub>Initializer</sub>

Initializes a QR code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(payload errorCorrectedPayload: Data, symbolVersion: Int, maskPattern: UInt8, errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel)
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the QR code symbol.

- `symbolVersion` — The symbol version, from 1 through 40.

- `maskPattern` — The mask pattern to use in the QR code, from 0 to 7.

- `errorCorrectionLevel` — The QR code’s error correction level: L, M, Q, or H.

## Return Value

An initialized [CIAztecCodeDescriptor](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid
