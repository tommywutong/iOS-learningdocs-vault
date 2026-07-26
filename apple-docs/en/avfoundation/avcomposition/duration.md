---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/duration.json'
content_hash: 'sha256:2c83d2e549f0304a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# duration

<sub>Instance Property</sub>

A time value that indicates the asset’s duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var duration: CMTime { get }
```

## Discussion

If you initialized the composition’s assets by passing the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [providesPreciseDurationAndTiming](../avasset/providesprecisedurationandtiming.md) property.

## See Also

### Accessing duration and timing

- [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
