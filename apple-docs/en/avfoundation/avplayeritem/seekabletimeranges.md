---
title: seekableTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/seekabletimeranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/seekabletimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/seekabletimeranges.json'
content_hash: 'sha256:4a576097a70b216f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# seekableTimeRanges

<sub>Instance Property</sub>

An array of time ranges within which it is possible to seek.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var seekableTimeRanges: [NSValue] { get }
```

## Discussion

The array contains [NSValue](../../foundation/nsvalue.md) objects containing a [CMTimeRange](../../coremedia/cmtimerange.md) value indicating the times ranges to which the player item can seek. The time ranges returned may be discontinuous.

## See Also

### Determining available time ranges

- [loadedTimeRanges](loadedtimeranges.md) — An array of time ranges indicating media data that is readily available.
