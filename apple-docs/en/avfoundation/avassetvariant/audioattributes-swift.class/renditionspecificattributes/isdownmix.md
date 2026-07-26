---
title: isDownmix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.json'
content_hash: 'sha256:0a4e5aeaf785b231'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetVariant](../../../avassetvariant.md) · [AudioAttributes](../../audioattributes-swift.class.md) · [RenditionSpecificAttributes](../renditionspecificattributes.md)

# isDownmix

<sub>Instance Property</sub>

A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDownmix: Bool { get }
```

## Discussion

If the stream provides one or more multichannel variants, the system assumes the dowmix rendition to be compatible in its internal timing and other attributes with the other variants. Typically, this is because the variant derives its content from the same source. You can use a downmix as a suitable substitute for a multichannel variant under some conditions.

## See Also

### Accessing attributes

- [channelCount](channelcount.md) — The count of audio channels in the rendition.
- [binaural](isbinaural.md) — A Boolean value that indicates the variant is best suited for delivery to headphones.
- [immersive](isimmersive.md) — A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
