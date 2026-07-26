---
title: AVAssetVariant.AudioAttributes.RenditionSpecificAttributes
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes.json'
content_hash: 'sha256:67f10ad3fc45b648'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetVariant](../../avassetvariant.md) · [AudioAttributes](../audioattributes-swift.class.md)

# AVAssetVariant.AudioAttributes.RenditionSpecificAttributes

<sub>Class</sub>

An object that represents attributes specific to a particular rendition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class RenditionSpecificAttributes
```

## Relationships

- **Inherits From**: [NSObject](../../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Accessing attributes

- [channelCount](renditionspecificattributes/channelcount.md) — The count of audio channels in the rendition.
- [binaural](renditionspecificattributes/isbinaural.md) — A Boolean value that indicates the variant is best suited for delivery to headphones.
- [immersive](renditionspecificattributes/isimmersive.md) — A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [downmix](renditionspecificattributes/isdownmix.md) — A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.

## See Also

### Inspecting audio attributes

- [formatIDs](formatids.md) — The audio formats of the renditions present in the variant.
- [- renditionSpecificAttributesForMediaOption:](<renditionspecificattributes(for_).md>) — Returns specific attributes for the media option.
