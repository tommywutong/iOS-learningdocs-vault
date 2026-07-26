---
title: CIQRCodeDescriptor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodedescriptor
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodedescriptor.json'
content_hash: 'sha256:3e689d3b14b0eb8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIQRCodeDescriptor

<sub>Class</sub>

A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIQRCodeDescriptor
```

## Overview

ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity. QR Codes can encode text, vCard contact information, or Uniform Resource Identifiers (URI).

## Relationships

- **Inherits From**: [CIBarcodeDescriptor](cibarcodedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Descriptor

- [- initWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:](<ciqrcodedescriptor/init(payload_symbolversion_maskpattern_errorcorrectionlevel_).md>) — Initializes a QR code descriptor for the given payload and parameters.

### Examining a Descriptor

- [errorCorrectedPayload](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md) — The error-corrected codeword payload that comprises the QR code symbol.
- [symbolVersion](ciqrcodedescriptor/symbolversion-swift.property.md) — The version of the QR code which corresponds to the size of the QR code symbol.
- [maskPattern](ciqrcodedescriptor/maskpattern-swift.property.md) — The data mask pattern for the QR code symbol.
- [errorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.property.md) — The error correction level of the QR code symbol.

### Error Correction Constants

- [ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.enum.md) — Constants indicating the percentage of the symbol that is dedicated to error correction.

## See Also

### Barcode Descriptions

- [CIBarcodeDescriptor](cibarcodedescriptor.md) — An abstract base class that represents a machine-readable code’s attributes.
- [CIAztecCodeDescriptor](ciazteccodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [CIPDF417CodeDescriptor](cipdf417codedescriptor.md) — A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
