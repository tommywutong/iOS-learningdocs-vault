---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/timerange.json'
content_hash: 'sha256:055a1a4ca253a22a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# timeRange

<sub>Type Property</sub>

The time range of the track within the overall timeline of the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var timeRange: AVAsyncProperty<Root, CMTimeRange> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

If the start of the time range is greater than [zero](../../coremedia/cmtime/zero.md), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

## See Also

### Loading temporal information

- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.
