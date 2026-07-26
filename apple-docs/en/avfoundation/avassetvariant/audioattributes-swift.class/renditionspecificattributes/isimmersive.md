---
title: isImmersive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive.json'
content_hash: 'sha256:7ce642fd8753a5ba'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetVariant](../../../avassetvariant.md) · [AudioAttributes](../../audioattributes-swift.class.md) · [RenditionSpecificAttributes](../renditionspecificattributes.md)

# isImmersive

<sub>Instance Property</sub>

A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isImmersive: Bool { get }
```

## Discussion

If a variant audio redition is immersive it’s eligible for rendering to headphones or speakers.

## See Also

### Accessing attributes

- [channelCount](channelcount.md) — The count of audio channels in the rendition.
- [binaural](isbinaural.md) — A Boolean value that indicates the variant is best suited for delivery to headphones.
- [downmix](isdownmix.md) — A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.
