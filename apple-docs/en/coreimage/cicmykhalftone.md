---
title: CICMYKHalftone
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicmykhalftone
source_url: 'https://developer.apple.com/documentation/coreimage/cicmykhalftone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicmykhalftone.json'
content_hash: 'sha256:d7112e28e0c4deb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CICMYKHalftone

<sub>Protocol</sub>

The properties you use to configure a CMYK halftone filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CICMYKHalftone : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [angle](cicmykhalftone/angle.md) — The angle of the pattern.
- [center](cicmykhalftone/center.md) — The x and y position to use as the center of the halftone pattern.
- [grayComponentReplacement](cicmykhalftone/graycomponentreplacement.md) — The gray component replacement value.
- [inputImage](cicmykhalftone/inputimage.md) — The image to use as an input image.
- [sharpness](cicmykhalftone/sharpness.md) — The sharpness of the pattern.
- [underColorRemoval](cicmykhalftone/undercolorremoval.md) — The under color removal value.
- [width](cicmykhalftone/width.md) — The distance between dots in the pattern.

## See Also

### Related Documentation

- [+ CMYKHalftone](<cifilter-swift.class/cmykhalftone().md>) — Adds a series of colorful dots to an image.

### Protocols

- [CICircularScreen](cicircularscreen.md) — The properties you use to configure a circular screen filter.
- [CIDotScreen](cidotscreen.md) — The properties you use to configure a dot screen filter.
- [CIHatchedScreen](cihatchedscreen.md) — The properties you use to configure a hatched screen filter.
- [CILineScreen](cilinescreen.md) — The properties you use to configure a line screen filter.
