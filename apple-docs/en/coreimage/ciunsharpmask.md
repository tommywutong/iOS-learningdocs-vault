---
title: CIUnsharpMask
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciunsharpmask
source_url: 'https://developer.apple.com/documentation/coreimage/ciunsharpmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciunsharpmask.json'
content_hash: 'sha256:7462fed5f237f12c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIUnsharpMask

<sub>Protocol</sub>

The properties you use to configure an unsharp mask filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIUnsharpMask : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](ciunsharpmask/inputimage.md) — The image to use as an input image.
- [intensity](ciunsharpmask/intensity.md) — The intensity of the effect.
- [radius](ciunsharpmask/radius.md) — The radius of the unsharp mask effect.

## See Also

### Related Documentation

- [+ unsharpMaskFilter](<cifilter-swift.class/unsharpmask().md>) — Increases an image’s contrast between two colors.

### Protocols

- [CISharpenLuminance](cisharpenluminance.md) — The properties you use to configure a sharpen luminance filter.
