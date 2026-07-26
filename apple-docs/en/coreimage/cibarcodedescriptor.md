---
title: CIBarcodeDescriptor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cibarcodedescriptor
source_url: 'https://developer.apple.com/documentation/coreimage/cibarcodedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cibarcodedescriptor.json'
content_hash: 'sha256:c9329da27f5e537c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIBarcodeDescriptor

<sub>Class</sub>

An abstract base class that represents a machine-readable code’s attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIBarcodeDescriptor
```

## Overview

Subclasses encapsulate the formal specification and fields specific to a code type. Each subclass is sufficient to recreate the unique symbol exactly as seen or used with a custom parser.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [CIAztecCodeDescriptor](ciazteccodedescriptor.md), [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md), [CIPDF417CodeDescriptor](cipdf417codedescriptor.md), [CIQRCodeDescriptor](ciqrcodedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Initializers

- [init(coder:)](<cibarcodedescriptor/init(coder_).md>)

## See Also

### Barcode Descriptions

- [CIQRCodeDescriptor](ciqrcodedescriptor.md) — A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [CIAztecCodeDescriptor](ciazteccodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [CIPDF417CodeDescriptor](cipdf417codedescriptor.md) — A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
