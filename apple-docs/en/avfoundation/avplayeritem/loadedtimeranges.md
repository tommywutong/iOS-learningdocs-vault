---
title: loadedTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/loadedtimeranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/loadedtimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/loadedtimeranges.json'
content_hash: 'sha256:afcb451c287e45c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# loadedTimeRanges

<sub>Instance Property</sub>

An array of time ranges indicating media data that is readily available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var loadedTimeRanges: [NSValue] { get }
```

## Discussion

The array contains [NSValue](../../foundation/nsvalue.md) objects containing a [CMTimeRange](../../coremedia/cmtimerange.md) value indicating the times ranges for which the player item has media data readily available. The time ranges returned may be discontinuous.

## See Also

### Determining available time ranges

- [seekableTimeRanges](seekabletimeranges.md) — An array of time ranges within which it is possible to seek.
