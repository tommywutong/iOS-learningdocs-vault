---
title: AVVideoRange
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideorange
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideorange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideorange.json'
content_hash: 'sha256:25edb405373ee98f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoRange

<sub>Structure</sub>

Constants that describe a video variant’s dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVVideoRange
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Video ranges

- [AVVideoRangePQ](avvideorange/pq.md) — Indicates Perceptual Quantizer (PQ) high-dynamic-range video.
- [AVVideoRangeHLG](avvideorange/hlg.md) — Indicates Hybrid-Log Gamma (HLG) high-dynamic-range video.
- [AVVideoRangeSDR](avvideorange/sdr.md) — Indicates standard-dynamic-range (SDR) video.

### Initializers

- [init(rawValue:)](<avvideorange/init(rawvalue_).md>) — Creates a video range with a string.

## See Also

### Inspecting the attributes

- [codecTypes](avassetvariant/videoattributes-swift.class/codectypes.md) — The video sample codec types present in the variant’s renditions.
- [nominalFrameRate](avassetvariant/videoattributes-swift.class/nominalframerate.md) — The nominal frame rate of the variant’s renditions.
- [presentationSize](avassetvariant/videoattributes-swift.class/presentationsize.md) — The presentation size of the variant’s renditions.
- [videoRange](avassetvariant/videoattributes-swift.class/videorange.md) — The video range of the variant.
- [videoLayoutAttributes](avassetvariant/videoattributes-swift.class/videolayoutattributes.md) — Attributes that describe the layout of the video content.
- [LayoutAttributes](avassetvariant/videoattributes-swift.class/layoutattributes.md) — Attributes that describe the layout of video content.
