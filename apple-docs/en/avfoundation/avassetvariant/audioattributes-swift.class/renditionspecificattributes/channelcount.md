---
title: channelCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount.json'
content_hash: 'sha256:a0d013308f2dde33'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetVariant](../../../avassetvariant.md) · [AudioAttributes](../../audioattributes-swift.class.md) · [RenditionSpecificAttributes](../renditionspecificattributes.md)

# channelCount

<sub>Instance Property</sub>

The count of audio channels in the rendition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc var channelCount: Int? { get }
```

## See Also

### Accessing attributes

- [binaural](isbinaural.md) — A Boolean value that indicates the variant is best suited for delivery to headphones.
- [immersive](isimmersive.md) — A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [downmix](isdownmix.md) — A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.
