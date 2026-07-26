---
title: CIHatchedScreen
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cihatchedscreen
source_url: 'https://developer.apple.com/documentation/coreimage/cihatchedscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cihatchedscreen.json'
content_hash: 'sha256:41cb65f29448499d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIHatchedScreen

<sub>Protocol</sub>

The properties you use to configure a hatched screen filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIHatchedScreen : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [angle](cihatchedscreen/angle.md) — The angle of the pattern.
- [center](cihatchedscreen/center.md) — The x and y position to use as the center of the hatched screen pattern.
- [inputImage](cihatchedscreen/inputimage.md) — The image to use as an input image.
- [sharpness](cihatchedscreen/sharpness.md) — The amount of sharpening to apply.
- [width](cihatchedscreen/width.md) — The distance between lines in the pattern.

## See Also

### Related Documentation

- [+ hatchedScreenFilter](<cifilter-swift.class/hatchedscreen().md>) — Creates a monochrome image with a series of lines to add detail.

### Protocols

- [CICircularScreen](cicircularscreen.md) — The properties you use to configure a circular screen filter.
- [CICMYKHalftone](cicmykhalftone.md) — The properties you use to configure a CMYK halftone filter.
- [CIDotScreen](cidotscreen.md) — The properties you use to configure a dot screen filter.
- [CILineScreen](cilinescreen.md) — The properties you use to configure a line screen filter.
