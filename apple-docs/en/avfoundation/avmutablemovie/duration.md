---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/duration.json'
content_hash: 'sha256:5ce2324bea043124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# duration

<sub>Instance Property</sub>

A time value that indicates the asset’s duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var duration: CMTime { get }
```

## Discussion

If you initialized the composition’s assets by passing the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [providesPreciseDurationAndTiming](../avasset/providesprecisedurationandtiming.md) property.

## See Also

### Accessing duration and timing

- [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
