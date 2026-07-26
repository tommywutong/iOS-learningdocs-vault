---
title: CIRoundedQRCodeGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciroundedqrcodegenerator
source_url: 'https://developer.apple.com/documentation/coreimage/ciroundedqrcodegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciroundedqrcodegenerator.json'
content_hash: 'sha256:1a6a77450749dceb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRoundedQRCodeGenerator

<sub>Protocol</sub>

The protocol for the Rounded QR Code Generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIRoundedQRCodeGenerator : CIFilterProtocol
```

## Overview

Generate a QR Code image for message data.

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [centerSpaceSize](ciroundedqrcodegenerator/centerspacesize.md) — The fraction of the center space of the QRCode to fill with Color 1. If the size is 0.0 or the Correction Level is L or M, the center of the QRCode will be unaltered. The size will be limited to 0.25 if the Correction Level is Q. The size will be limited to 0.33 if the Correction Level is H.
- [color0](ciroundedqrcodegenerator/color0.md) — The background color for the QRCode
- [color1](ciroundedqrcodegenerator/color1.md) — The foreground color for the QRCode
- [correctionLevel](ciroundedqrcodegenerator/correctionlevel.md) — QR Code correction level L, M, Q, or H.
- [message](ciroundedqrcodegenerator/message.md) — The message to encode in the QR Code
- [roundedData](ciroundedqrcodegenerator/roundeddata.md) — If true then the data points in the QRCode should have a rounded appearance.
- [roundedMarkers](ciroundedqrcodegenerator/roundedmarkers.md) — If 1, then the Finder Patterns in the QRCode should have a rounded appearance. If 2, then the Alignment Patterns will also be rounded
- [scale](ciroundedqrcodegenerator/scale.md) — The scale factor to enlarge the QRCode by.
