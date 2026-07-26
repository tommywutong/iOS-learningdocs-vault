---
title: CIQRCodeGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciqrcodegenerator
source_url: 'https://developer.apple.com/documentation/coreimage/ciqrcodegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciqrcodegenerator.json'
content_hash: 'sha256:5588d70ff9a29481'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIQRCodeGenerator

<sub>Protocol</sub>

The properties you use to configure a QR code generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIQRCodeGenerator : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [correctionLevel](ciqrcodegenerator/correctionlevel.md) — The QR code correction level: L, M, Q, or H.
- [message](ciqrcodegenerator/message.md) — The message to encode in the QR code.

## See Also

### Related Documentation

- [+ QRCodeGenerator](<cifilter-swift.class/qrcodegenerator().md>) — Generates a quick response (QR) code image.

### Protocols

- [CICode128BarcodeGenerator](cicode128barcodegenerator.md) — The properties you use to configure a Code 128 barcode generator filter.
- [CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md) — The properties you use to configure an attributed-text image generator filter.
- [CIAztecCodeGenerator](ciazteccodegenerator.md) — The properties you use to configure an Aztec code generator filter.
- [CIBarcodeGenerator](cibarcodegenerator.md) — The properties you use to configure a barcode generator filter.
- [CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CICheckerboardGenerator](cicheckerboardgenerator.md) — The properties you use to configure a checkerboard generator filter.
- [CILenticularHaloGenerator](cilenticularhalogenerator.md) — The properties you use to configure a lenticular halo generator filter.
- [CIMeshGenerator](cimeshgenerator.md) — The properties you use to configure a mesh generator filter.
- [CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md) — The properties you use to configure a PDF417 barcode generator filter.
- [CIRandomGenerator](cirandomgenerator.md) — The properties you use to configure a random generator filter.
- [CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md) — The properties you use to configure a rounded rectangle generator filter.
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CIStarShineGenerator](cistarshinegenerator.md) — The properties you use to configure a star-shine generator filter.
- [CIStripesGenerator](cistripesgenerator.md) — The properties you use to configure a stripes generator filter.
