---
title: providesPreciseDurationAndTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/providesprecisedurationandtiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/providesprecisedurationandtiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/providesprecisedurationandtiming.json'
content_hash: 'sha256:eb3b3d4df1c81d13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# providesPreciseDurationAndTiming

<sub>Type Property</sub>

A Boolean value that indicates whether the asset provides precise duration and timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

This property value is [true](../../swift/true.md) if you initialized the asset with the [AVURLAssetPreferPreciseDurationAndTimingKey](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [false](../../swift/false.md).

> [!note] Note
> If calculating precise duration and timing isn’t possible for the media resources that the URL references, the value of this property is [false](../../swift/false.md), even if you requested otherwise.

## See Also

### Loading duration and timing

- [duration](duration.md) — A time value that represents the duration of the asset.
- [minimumTimeOffsetFromLive](minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.
