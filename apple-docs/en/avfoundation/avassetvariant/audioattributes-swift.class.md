---
title: AVAssetVariant.AudioAttributes
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class.json'
content_hash: 'sha256:33b39a00e5e75412'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariant](../avassetvariant.md)

# AVAssetVariant.AudioAttributes

<sub>Class</sub>

An object that defines the audio attributes for an asset variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AudioAttributes
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting audio attributes

- [formatIDs](audioattributes-swift.class/formatids.md) — The audio formats of the renditions present in the variant.
- [- renditionSpecificAttributesForMediaOption:](<audioattributes-swift.class/renditionspecificattributes(for_).md>) — Returns specific attributes for the media option.
- [RenditionSpecificAttributes](audioattributes-swift.class/renditionspecificattributes.md) — An object that represents attributes specific to a particular rendition.

## See Also

### Configuring attributes

- [audioAttributes](audioattributes-swift.property.md) — The audio rendition attributes for the variant.
- [videoAttributes](videoattributes-swift.property.md) — The video rendition attributes for the variant.
- [VideoAttributes](videoattributes-swift.class.md) — An object that defines the video attributes for an asset variant.
