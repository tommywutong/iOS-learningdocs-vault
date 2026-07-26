---
title: CILineScreen
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilinescreen
source_url: 'https://developer.apple.com/documentation/coreimage/cilinescreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilinescreen.json'
content_hash: 'sha256:83535bfe210e2c76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CILineScreen

<sub>Protocol</sub>

The properties you use to configure a line screen filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CILineScreen : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [angle](cilinescreen/angle.md) — The angle of the pattern.
- [center](cilinescreen/center.md) — The x and y position to use as the center of the line screen pattern.
- [inputImage](cilinescreen/inputimage.md) — The image to use as an input image.
- [sharpness](cilinescreen/sharpness.md) — The sharpness of the pattern.
- [width](cilinescreen/width.md) — The distance between lines in the pattern.

## See Also

### Related Documentation

- [+ lineScreenFilter](<cifilter-swift.class/linescreen().md>) — Creates a monochrome image with a series of small lines to add detail.

### Protocols

- [CICircularScreen](cicircularscreen.md) — The properties you use to configure a circular screen filter.
- [CICMYKHalftone](cicmykhalftone.md) — The properties you use to configure a CMYK halftone filter.
- [CIDotScreen](cidotscreen.md) — The properties you use to configure a dot screen filter.
- [CIHatchedScreen](cihatchedscreen.md) — The properties you use to configure a hatched screen filter.
