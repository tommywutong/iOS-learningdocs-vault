---
title: providesPreciseDurationAndTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/providesprecisedurationandtiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/providesprecisedurationandtiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/providesprecisedurationandtiming.json'
content_hash: 'sha256:308669e819114ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# providesPreciseDurationAndTiming

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset provides precise duration and timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var providesPreciseDurationAndTiming: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you initialized the asset with the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [false](../../swift/false.md).

## See Also

### Accessing duration and timing

- [duration](duration.md) — A time value that indicates the asset’s duration.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
