---
title: videoLayoutAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/videoattributes-swift.class/videolayoutattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videolayoutattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videolayoutattributes.json'
content_hash: 'sha256:3f6dccce0dec8072'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetVariant](../../avassetvariant.md) · [VideoAttributes](../videoattributes-swift.class.md)

# videoLayoutAttributes

<sub>Instance Property</sub>

Attributes that describe the layout of the video content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes] { get }
```

## Discussion

This property may contain more that one element if the variant contains a collection of differing video layout media attributes over time.

## See Also

### Inspecting the attributes

- [codecTypes](codectypes.md) — The video sample codec types present in the variant’s renditions.
- [nominalFrameRate](nominalframerate.md) — The nominal frame rate of the variant’s renditions.
- [presentationSize](presentationsize.md) — The presentation size of the variant’s renditions.
- [videoRange](videorange.md) — The video range of the variant.
- [AVVideoRange](../../avvideorange.md) — Constants that describe a video variant’s dynamic range.
- [LayoutAttributes](layoutattributes.md) — Attributes that describe the layout of video content.
