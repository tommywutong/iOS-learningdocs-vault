---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/duration.json'
content_hash: 'sha256:6c9a3a0b3fbc98e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# duration

<sub>Type Property</sub>

A time value that represents the duration of the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var duration: AVAsyncProperty<Root, CMTime> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

If the value of [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) is [false](../../swift/false.md), the asset returns a best-available estimate of the duration. You can specify your preferred degree of precision for timing-related properties when you create an [AVURLAsset](../avurlasset.md) by passing a value for the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option.

## See Also

### Loading duration and timing

- [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
