---
title: minimumTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/minimumtimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/minimumtimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/minimumtimeoffsetfromlive.json'
content_hash: 'sha256:e1c831450366c280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# minimumTimeOffsetFromLive

<sub>Instance Property</sub>

A time value that indicates how closely playback follows the latest live stream content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var minimumTimeOffsetFromLive: CMTime { get }
```

## Discussion

This property value is only valid when working with live streaming content. For non-live assets, this property value is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Accessing duration and timing

- [duration](duration.md) — A time value that indicates the asset’s duration.
- [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
