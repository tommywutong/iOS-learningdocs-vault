---
title: CISharpenLuminance
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisharpenluminance
source_url: 'https://developer.apple.com/documentation/coreimage/cisharpenluminance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisharpenluminance.json'
content_hash: 'sha256:cdeb18fdab3d20a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CISharpenLuminance

<sub>Protocol</sub>

The properties you use to configure a sharpen luminance filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CISharpenLuminance : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cisharpenluminance/inputimage.md) — The image to use as an input image.
- [radius](cisharpenluminance/radius.md) — The distance from the center of the effect.
- [sharpness](cisharpenluminance/sharpness.md) — The amount of sharpening to apply.

## See Also

### Related Documentation

- [+ sharpenLuminanceFilter](<cifilter-swift.class/sharpenluminance().md>) — Applies a sharpening effect to an image.

### Protocols

- [CIUnsharpMask](ciunsharpmask.md) — The properties you use to configure an unsharp mask filter.
