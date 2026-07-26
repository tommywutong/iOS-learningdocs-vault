---
title: minimumTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/minimumtimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/minimumtimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/minimumtimeoffsetfromlive.json'
content_hash: 'sha256:66f36239d8be3ce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# minimumTimeOffsetFromLive

<sub>Type Property</sub>

A time value that indicates how closely playback follows the latest live stream content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

This property value is only valid when working with live streaming content. For non-live assets, this property value is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Loading duration and timing

- [duration](duration.md) — A time value that represents the duration of the asset.
- [providesPreciseDurationAndTiming](providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
