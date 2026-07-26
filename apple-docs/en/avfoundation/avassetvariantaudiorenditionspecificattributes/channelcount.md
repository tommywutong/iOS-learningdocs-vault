---
title: channelCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariantaudiorenditionspecificattributes/channelcount
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariantaudiorenditionspecificattributes/channelcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariantaudiorenditionspecificattributes/channelcount.json'
content_hash: 'sha256:71c47c4400a9293d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [RenditionSpecificAttributes](../avassetvariant/audioattributes-swift.class/renditionspecificattributes.md)

# channelCount

<sub>Instance Property</sub>

The count of audio channels in the rendition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSInteger channelCount;
```

## See Also

### Accessing attributes

- [binaural](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural.md) — A Boolean value that indicates the variant is best suited for delivery to headphones.
- [immersive](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive.md) — A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [downmix](../avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.md) — A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.
