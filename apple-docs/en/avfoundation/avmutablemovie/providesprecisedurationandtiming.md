---
title: providesPreciseDurationAndTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/providesprecisedurationandtiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/providesprecisedurationandtiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/providesprecisedurationandtiming.json'
content_hash: 'sha256:258cf3354e4847d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# providesPreciseDurationAndTiming

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset provides precise duration and timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var providesPreciseDurationAndTiming: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you initialized the asset with the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [false](../../swift/false.md).

## See Also

### Accessing duration and timing

- [duration](duration.md) — A time value that indicates the asset’s duration.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
