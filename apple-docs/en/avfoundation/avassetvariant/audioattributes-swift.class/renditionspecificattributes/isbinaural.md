---
title: isBinaural
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural.json'
content_hash: 'sha256:a5ee07fc4f57a3b1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetVariant](../../../avassetvariant.md) · [AudioAttributes](../../audioattributes-swift.class.md) · [RenditionSpecificAttributes](../renditionspecificattributes.md)

# isBinaural

<sub>Instance Property</sub>

A Boolean value that indicates the variant is best suited for delivery to headphones.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isBinaural: Bool { get }
```

## Discussion

A binaural variant may originate from a direct binaural recording or from the processing of a multichannel audio source.

## See Also

### Accessing attributes

- [channelCount](channelcount.md) — The count of audio channels in the rendition.
- [immersive](isimmersive.md) — A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [downmix](isdownmix.md) — A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.
