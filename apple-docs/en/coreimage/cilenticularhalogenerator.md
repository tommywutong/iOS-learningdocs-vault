---
title: CILenticularHaloGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilenticularhalogenerator
source_url: 'https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilenticularhalogenerator.json'
content_hash: 'sha256:58c59bca06b06628'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CILenticularHaloGenerator

<sub>Protocol</sub>

The properties you use to configure a lenticular halo generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CILenticularHaloGenerator : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [center](cilenticularhalogenerator/center.md) — The x and y position to use as the center of the halo.
- [color](cilenticularhalogenerator/color.md) — The color of the halo.
- [haloOverlap](cilenticularhalogenerator/halooverlap.md) — The separation of colors in the halo.
- [haloRadius](cilenticularhalogenerator/haloradius.md) — The radius of the halo.
- [haloWidth](cilenticularhalogenerator/halowidth.md) — The width of the halo, from its inner radius to its outer radius.
- [striationContrast](cilenticularhalogenerator/striationcontrast.md) — The contrast of the halo colors.
- [striationStrength](cilenticularhalogenerator/striationstrength.md) — The intensity of the halo colors.
- [time](cilenticularhalogenerator/time.md) — The current time of the effect.

## See Also

### Related Documentation

- [+ lenticularHaloGeneratorFilter](<cifilter-swift.class/lenticularhalogenerator().md>) — Generates a lenticular halo image.

### Protocols

- [CICode128BarcodeGenerator](cicode128barcodegenerator.md) — The properties you use to configure a Code 128 barcode generator filter.
- [CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md) — The properties you use to configure an attributed-text image generator filter.
- [CIAztecCodeGenerator](ciazteccodegenerator.md) — The properties you use to configure an Aztec code generator filter.
- [CIBarcodeGenerator](cibarcodegenerator.md) — The properties you use to configure a barcode generator filter.
- [CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CICheckerboardGenerator](cicheckerboardgenerator.md) — The properties you use to configure a checkerboard generator filter.
- [CIMeshGenerator](cimeshgenerator.md) — The properties you use to configure a mesh generator filter.
- [CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md) — The properties you use to configure a PDF417 barcode generator filter.
- [CIQRCodeGenerator](ciqrcodegenerator.md) — The properties you use to configure a QR code generator filter.
- [CIRandomGenerator](cirandomgenerator.md) — The properties you use to configure a random generator filter.
- [CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md) — The properties you use to configure a rounded rectangle generator filter.
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CIStarShineGenerator](cistarshinegenerator.md) — The properties you use to configure a star-shine generator filter.
- [CIStripesGenerator](cistripesgenerator.md) — The properties you use to configure a stripes generator filter.
