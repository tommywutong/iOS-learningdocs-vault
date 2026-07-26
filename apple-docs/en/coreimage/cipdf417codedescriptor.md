---
title: CIPDF417CodeDescriptor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cipdf417codedescriptor
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor.json'
content_hash: 'sha256:22bf050ad0dec2bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIPDF417CodeDescriptor

<sub>Class</sub>

A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIPDF417CodeDescriptor
```

## Overview

PDF417 is a stacked linear barcode symbol format used predominantly in transport, ID cards, and inventory management. Each pattern in the code comprises 4 bars and spaces, 17 units long.

Refer to the ISO/IEC 15438:2006(E) for the PDF417 symbol specification.

## Relationships

- **Inherits From**: [CIBarcodeDescriptor](cibarcodedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Descriptor

- [- initWithPayload:isCompact:rowCount:columnCount:](<cipdf417codedescriptor/init(payload_iscompact_rowcount_columncount_).md>) — Initializes an PDF417 code descriptor for the given payload and parameters.

### Examining a Descriptor

- [errorCorrectedPayload](cipdf417codedescriptor/errorcorrectedpayload-swift.property.md) — The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [isCompact](cipdf417codedescriptor/iscompact-swift.property.md) — A boolean value telling if the PDF417 code is compact.
- [rowCount](cipdf417codedescriptor/rowcount-swift.property.md) — The number of rows in the PDF417 code symbol.
- [columnCount](cipdf417codedescriptor/columncount-swift.property.md) — The number of columns in the PDF417 code symbol.

## See Also

### Barcode Descriptions

- [CIBarcodeDescriptor](cibarcodedescriptor.md) — An abstract base class that represents a machine-readable code’s attributes.
- [CIQRCodeDescriptor](ciqrcodedescriptor.md) — A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [CIAztecCodeDescriptor](ciazteccodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
