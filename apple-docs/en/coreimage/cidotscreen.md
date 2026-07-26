---
title: CIDotScreen
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidotscreen
source_url: 'https://developer.apple.com/documentation/coreimage/cidotscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidotscreen.json'
content_hash: 'sha256:cc7fc1977c02c054'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDotScreen

<sub>Protocol</sub>

The properties you use to configure a dot screen filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIDotScreen : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [angle](cidotscreen/angle.md) — The angle of the pattern.
- [center](cidotscreen/center.md) — The x and y position to use as the center of the dot screen pattern.
- [inputImage](cidotscreen/inputimage.md) — The image to use as an input image.
- [sharpness](cidotscreen/sharpness.md) — The sharpness of the pattern.
- [width](cidotscreen/width.md) — The distance between dots in the pattern.

## See Also

### Related Documentation

- [+ dotScreenFilter](<cifilter-swift.class/dotscreen().md>) — Creates a monochrome image with a series of dots to add detail.

### Protocols

- [CICircularScreen](cicircularscreen.md) — The properties you use to configure a circular screen filter.
- [CICMYKHalftone](cicmykhalftone.md) — The properties you use to configure a CMYK halftone filter.
- [CIHatchedScreen](cihatchedscreen.md) — The properties you use to configure a hatched screen filter.
- [CILineScreen](cilinescreen.md) — The properties you use to configure a line screen filter.
