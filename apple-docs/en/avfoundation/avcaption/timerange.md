---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/timerange.json'
content_hash: 'sha256:5243f3068ec90ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# timeRange

<sub>Instance Property</sub>

The time range over which the system presents the caption.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

Apple iTT format only permits captions to have overlapping time ranges if they’re associated with different regions.

CEA608 closed caption time ranges can’t start with zero, because the decoder needs transmission time. Align time ranges with the video frame rate.

## See Also

### Accessing text and timing

- [text](text.md) — The caption text.
