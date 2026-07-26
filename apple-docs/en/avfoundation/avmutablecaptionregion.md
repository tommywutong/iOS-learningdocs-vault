---
title: AVMutableCaptionRegion
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecaptionregion
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaptionregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaptionregion.json'
content_hash: 'sha256:dd3006cbb52164ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableCaptionRegion

<sub>Class</sub>

A mutable caption region subclass that you use to create new caption regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVMutableCaptionRegion
```

## Relationships

- **Inherits From**: [AVCaptionRegion](avcaptionregion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a caption region

- [- init](<avmutablecaptionregion/init().md>) — Creates a caption region.
- [- initWithIdentifier:](<avmutablecaptionregion/init(identifier_).md>) — Creates a caption region that has an identifier.

### Configuring the region

- [origin](avmutablecaptionregion/origin.md) — The region’s top-left position.
- [size](avmutablecaptionregion/size.md) — The height and width of the region.
- [displayAlignment](avmutablecaptionregion/displayalignment.md) — The alignment of lines for the region.
- [scroll](avmutablecaptionregion/scroll.md) — The scroll mode of the region.
- [writingMode](avmutablecaptionregion/writingmode.md) — The block and inline progression direction of the region.

## See Also

### Regions

- [AVCaptionRegion](avcaptionregion.md) — An object that represents the region in which the system presents a caption.
