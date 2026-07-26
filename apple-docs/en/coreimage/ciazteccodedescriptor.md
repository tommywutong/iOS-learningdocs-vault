---
title: CIAztecCodeDescriptor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodedescriptor
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodedescriptor.json'
content_hash: 'sha256:1a406daa8b15192a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIAztecCodeDescriptor

<sub>Class</sub>

A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIAztecCodeDescriptor
```

## Overview

An Aztec code symbol is a 2D barcode format defined by the ISO/IEC 24778:2008 standard. It encodes data in concentric square rings around a central bullseye pattern.

## Relationships

- **Inherits From**: [CIBarcodeDescriptor](cibarcodedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Descriptor

- [- initWithPayload:isCompact:layerCount:dataCodewordCount:](<ciazteccodedescriptor/init(payload_iscompact_layercount_datacodewordcount_).md>) — Initializes an Aztec code descriptor for the given payload and parameters.

### Examining a Descriptor

- [errorCorrectedPayload](ciazteccodedescriptor/errorcorrectedpayload-swift.property.md) — The error-corrected payload that comprises the the Aztec code symbol.
- [isCompact](ciazteccodedescriptor/iscompact-swift.property.md) — A Boolean value telling if the Aztec code is compact.
- [layerCount](ciazteccodedescriptor/layercount-swift.property.md) — The number of data layers in the Aztec code symbol.
- [dataCodewordCount](ciazteccodedescriptor/datacodewordcount-swift.property.md) — The number of non-error-correction codewords carried by the Aztec code symbol.

## See Also

### Barcode Descriptions

- [CIBarcodeDescriptor](cibarcodedescriptor.md) — An abstract base class that represents a machine-readable code’s attributes.
- [CIQRCodeDescriptor](ciqrcodedescriptor.md) — A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [CIPDF417CodeDescriptor](cipdf417codedescriptor.md) — A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md) — A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
