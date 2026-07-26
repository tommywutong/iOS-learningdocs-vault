---
title: audioAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.property.json'
content_hash: 'sha256:1e671b5cc7edf260'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariant](../avassetvariant.md)

# audioAttributes

<sub>Instance Property</sub>

The audio rendition attributes for the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var audioAttributes: AVAssetVariant.AudioAttributes? { get }
```

## Discussion

This property value is `nil` if the variant defines no audio attributes.

## See Also

### Configuring attributes

- [AudioAttributes](audioattributes-swift.class.md) — An object that defines the audio attributes for an asset variant.
- [videoAttributes](videoattributes-swift.property.md) — The video rendition attributes for the variant.
- [VideoAttributes](videoattributes-swift.class.md) — An object that defines the video attributes for an asset variant.
