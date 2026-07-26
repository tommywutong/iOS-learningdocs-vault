---
title: videoAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/videoattributes-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/videoattributes-swift.property.json'
content_hash: 'sha256:c797d97e5f1b76c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVariant](../avassetvariant.md)

# videoAttributes

<sub>Instance Property</sub>

The video rendition attributes for the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var videoAttributes: AVAssetVariant.VideoAttributes? { get }
```

## Discussion

This property value is `nil` if the variant defines no video attributes.

## See Also

### Configuring attributes

- [audioAttributes](audioattributes-swift.property.md) — The audio rendition attributes for the variant.
- [AudioAttributes](audioattributes-swift.class.md) — An object that defines the audio attributes for an asset variant.
- [VideoAttributes](videoattributes-swift.class.md) — An object that defines the video attributes for an asset variant.
