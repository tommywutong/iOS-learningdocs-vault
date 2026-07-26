---
title: CICode128BarcodeGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicode128barcodegenerator
source_url: 'https://developer.apple.com/documentation/coreimage/cicode128barcodegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicode128barcodegenerator.json'
content_hash: 'sha256:9530c28428ca7c46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CICode128BarcodeGenerator

<sub>Protocol</sub>

The properties you use to configure a Code 128 barcode generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CICode128BarcodeGenerator : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [barcodeHeight](cicode128barcodegenerator/barcodeheight.md) — The height, in pixels, of the generated barcode.
- [message](cicode128barcodegenerator/message.md) — The message to encode in the Code 128 barcode.
- [quietSpace](cicode128barcodegenerator/quietspace.md) — The number of empty white pixels that should surround the barcode.

## See Also

### Related Documentation

- [+ code128BarcodeGeneratorFilter](<cifilter-swift.class/code128barcodegenerator().md>) — Generates a high-density, linear barcode.

### Protocols

- [CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md) — The properties you use to configure an attributed-text image generator filter.
- [CIAztecCodeGenerator](ciazteccodegenerator.md) — The properties you use to configure an Aztec code generator filter.
- [CIBarcodeGenerator](cibarcodegenerator.md) — The properties you use to configure a barcode generator filter.
- [CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CICheckerboardGenerator](cicheckerboardgenerator.md) — The properties you use to configure a checkerboard generator filter.
- [CILenticularHaloGenerator](cilenticularhalogenerator.md) — The properties you use to configure a lenticular halo generator filter.
- [CIMeshGenerator](cimeshgenerator.md) — The properties you use to configure a mesh generator filter.
- [CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md) — The properties you use to configure a PDF417 barcode generator filter.
- [CIQRCodeGenerator](ciqrcodegenerator.md) — The properties you use to configure a QR code generator filter.
- [CIRandomGenerator](cirandomgenerator.md) — The properties you use to configure a random generator filter.
- [CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md) — The properties you use to configure a rounded rectangle generator filter.
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CIStarShineGenerator](cistarshinegenerator.md) — The properties you use to configure a star-shine generator filter.
- [CIStripesGenerator](cistripesgenerator.md) — The properties you use to configure a stripes generator filter.
