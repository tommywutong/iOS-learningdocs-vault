---
title: AVAssetVariant
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant.json'
content_hash: 'sha256:ffd5e2a9cd007833'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetVariant

<sub>Class</sub>

An object that represents a bit rate variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetVariant
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring attributes

- [audioAttributes](avassetvariant/audioattributes-swift.property.md) — The audio rendition attributes for the variant.
- [AudioAttributes](avassetvariant/audioattributes-swift.class.md) — An object that defines the audio attributes for an asset variant.
- [videoAttributes](avassetvariant/videoattributes-swift.property.md) — The video rendition attributes for the variant.
- [VideoAttributes](avassetvariant/videoattributes-swift.class.md) — An object that defines the video attributes for an asset variant.

### Configuring bit rate

- [averageBitRate](avassetvariant/averagebitrate-5p1oh.md) — The average bit rate for the variant.
- [peakBitRate](avassetvariant/peakbitrate-9hzpi.md) — The peak bit rate for the variant.

### Accessing the URL

- [URL](avassetvariant/url.md) — Provides URL to media playlist corresponding to variant

## See Also

### Creating a variant qualifier

- [+ assetVariantQualifierWithVariant:](<avassetvariantqualifier/init(variant_).md>) — Creates a variant qualifier with an asset variant.
- [+ assetVariantQualifierWithPredicate:](<avassetvariantqualifier/init(predicate_).md>) — Creates a variant qualifier with a predicate.
