---
title: videoRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/videoattributes-swift.class/videorange
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videorange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videorange.json'
content_hash: 'sha256:09288c6a3e54fe97'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetVariant](../../avassetvariant.md) · [VideoAttributes](../videoattributes-swift.class.md)

# videoRange

<sub>Instance Property</sub>

The video range of the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var videoRange: AVVideoRange { get }
```

## Discussion

The property defaults to [AVVideoRangeSDR](../../avvideorange/sdr.md).

## See Also

### Inspecting the attributes

- [codecTypes](codectypes.md) — The video sample codec types present in the variant’s renditions.
- [nominalFrameRate](nominalframerate.md) — The nominal frame rate of the variant’s renditions.
- [presentationSize](presentationsize.md) — The presentation size of the variant’s renditions.
- [AVVideoRange](../../avvideorange.md) — Constants that describe a video variant’s dynamic range.
- [videoLayoutAttributes](videolayoutattributes.md) — Attributes that describe the layout of the video content.
- [LayoutAttributes](layoutattributes.md) — Attributes that describe the layout of video content.
