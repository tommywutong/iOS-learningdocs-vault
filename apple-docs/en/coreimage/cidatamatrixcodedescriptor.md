---
title: CIDataMatrixCodeDescriptor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor.json'
content_hash: 'sha256:4687837ebb513b1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDataMatrixCodeDescriptor

<sub>Class</sub>

A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIDataMatrixCodeDescriptor
```

## Overview

A Data Matrix code symbol is a 2D barcode format defined by the ISO/IEC 16022:2006(E) standard. It encodes data in square or rectangular symbol with solid lines on the left and bottom sides

## Relationships

- **Inherits From**: [CIBarcodeDescriptor](cibarcodedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Descriptor

- [- initWithPayload:rowCount:columnCount:eccVersion:](<cidatamatrixcodedescriptor/init(payload_rowcount_columncount_eccversion_).md>) — Initializes a Data Matrix code descriptor for the given payload and parameters.

### Examining a Descriptor

- [errorCorrectedPayload](cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [rowCount](cidatamatrixcodedescriptor/rowcount-swift.property.md) — The number of rows in the Data Matrix code symbol.
- [columnCount](cidatamatrixcodedescriptor/columncount-swift.property.md) — The number of columns in the Data Matrix code symbol.
- [eccVersion](cidatamatrixcodedescriptor/eccversion-swift.property.md) — The error correction version of the Data Matrix code symbol.

### Error Correction Constants

- [ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.enum.md) — Constants indicating the Data Matrix code ECC version.

## See Also

### Barcode Descriptions

- [CIBarcodeDescriptor](cibarcodedescriptor.md) — An abstract base class that represents a machine-readable code’s attributes.
- [CIQRCodeDescriptor](ciqrcodedescriptor.md) — A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [CIAztecCodeDescriptor](ciazteccodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [CIPDF417CodeDescriptor](cipdf417codedescriptor.md) — A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
