---
title: CIAztecCodeGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciazteccodegenerator
source_url: 'https://developer.apple.com/documentation/coreimage/ciazteccodegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciazteccodegenerator.json'
content_hash: 'sha256:32ed234d3cfb52d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIAztecCodeGenerator

<sub>Protocol</sub>

The properties you use to configure an Aztec code generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIAztecCodeGenerator : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [compactStyle](ciazteccodegenerator/compactstyle.md) — A Boolean that specifies whether to force a compact style Aztec code.
- [correctionLevel](ciazteccodegenerator/correctionlevel.md) — The Aztec error correction, a value from 5 to 95.
- [layers](ciazteccodegenerator/layers.md) — The number of Aztec layers, a value from 1 to 32.
- [message](ciazteccodegenerator/message.md) — The message to encode in the Aztec barcode.

## See Also

### Related Documentation

- [+ aztecCodeGeneratorFilter](<cifilter-swift.class/azteccodegenerator().md>) — Generates a low-density barcode.

### Protocols

- [CICode128BarcodeGenerator](cicode128barcodegenerator.md) — The properties you use to configure a Code 128 barcode generator filter.
- [CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md) — The properties you use to configure an attributed-text image generator filter.
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
