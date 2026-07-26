---
title: CIQRCodeFeature
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodefeature
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodefeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodefeature.json'
content_hash: 'sha256:f64879cba2aa9f94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIQRCodeFeature

<sub>Class</sub>

Information about a Quick Response code detected in a still or video image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIQRCodeFeature
```

## Overview

> [!note] Note
> In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [VNDetectBarcodesRequest](../vision/vndetectbarcodesrequest.md))

A QR code is a two-dimensional barcode using the ISO/IEC 18004:2006 standard. The properties of a CIQRCodeFeature object identify the corners of the barcode in the image perspective and provide the decoded message.

To detect QR codes in an image or video, choose [CIDetectorTypeQRCode](cidetectortypeqrcode.md) type when initializing a [CIDetector](cidetector.md) object.

## Relationships

- **Inherits From**: [CIFeature](cifeature.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Locating a Detected Feature

- [bounds](ciqrcodefeature/bounds-swift.property.md) — A rectangle that indicates the position and extent of the QR code feature in image coordinates.

### Decoding a Detected Barcode

- [messageString](ciqrcodefeature/messagestring.md) — The string decoded from the detected barcode.
- [symbolDescriptor](ciqrcodefeature/symboldescriptor-swift.property.md) — An abstract representation of a QR Code symbol.

### Identifying the Corners of a Detected Barcode

- [bottomLeft](ciqrcodefeature/bottomleft-swift.property.md) — The image coordinate of the lower-left corner of the detected QR code.
- [bottomRight](ciqrcodefeature/bottomright-swift.property.md) — The image coordinate of the lower-right corner of the detected QR code.
- [topLeft](ciqrcodefeature/topleft-swift.property.md) — The image coordinate of the upper-left corner of the detected QR code.
- [topRight](ciqrcodefeature/topright-swift.property.md) — The image coordinate of the upper-right corner of the detected QR code.

### Initializers

- [init(coder:)](<ciqrcodefeature/init(coder_).md>)

## See Also

### Image Feature Detection

- [CIDetector](cidetector.md) — An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [CIFeature](cifeature.md) — The abstract superclass for objects representing notable features detected in an image.
- [CIFaceFeature](cifacefeature.md) — Information about a face detected in a still or video image.
- [CIRectangleFeature](cirectanglefeature.md) — Information about a rectangular region detected in a still or video image.
- [CITextFeature](citextfeature.md) — Information about a text that was detected in a still or video image.
