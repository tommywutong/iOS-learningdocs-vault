---
title: CICircularScreen
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicircularscreen
source_url: 'https://developer.apple.com/documentation/coreimage/cicircularscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicircularscreen.json'
content_hash: 'sha256:22eae1d7c89b0d7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CICircularScreen

<sub>Protocol</sub>

The properties you use to configure a circular screen filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CICircularScreen : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [center](cicircularscreen/center.md) — The x and y position to use as the center of the circular screen pattern.
- [inputImage](cicircularscreen/inputimage.md) — The image to use as an input image.
- [sharpness](cicircularscreen/sharpness.md) — The sharpness of the circles.
- [width](cicircularscreen/width.md) — The distance between each circle in the pattern.

## See Also

### Related Documentation

- [+ circularScreenFilter](<cifilter-swift.class/circularscreen().md>) — Adds a circular overlay to an image.

### Protocols

- [CICMYKHalftone](cicmykhalftone.md) — The properties you use to configure a CMYK halftone filter.
- [CIDotScreen](cidotscreen.md) — The properties you use to configure a dot screen filter.
- [CIHatchedScreen](cihatchedscreen.md) — The properties you use to configure a hatched screen filter.
- [CILineScreen](cilinescreen.md) — The properties you use to configure a line screen filter.
