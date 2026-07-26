---
title: AVPlayerItemSegment
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsegment
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsegment.json'
content_hash: 'sha256:8ac1cf98bce93c15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemSegment

<sub>Class</sub>

An immutable object that represents a segment of time on the integrated timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemSegment
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the type

- [segmentType](avplayeritemsegment/segmenttype-swift.property.md) — The type content this segment represents.
- [SegmentType](avplayeritemsegment/segmenttype-swift.enum.md) — Constants that specify the type of segment.

### Inspecting the segment

- [timeMapping](avplayeritemsegment/timemapping.md) — The time mapping for this segment.
- [loadedTimeRanges](avplayeritemsegment/loadedtimeranges-879hc.md) — The time ranges for the segment that have media data is readily available.
- [startDate](avplayeritemsegment/startdate.md) — The date at which a segment starts.
- [interstitialEvent](avplayeritemsegment/interstitialevent.md) — The associated interstitial event for this segment.

## See Also

### Inspecting the snapshot

- [duration](avplayeritemintegratedtimelinesnapshot/duration.md) — The total duration of the primary item and scheduled interstitial events.
- [currentSegment](avplayeritemintegratedtimelinesnapshot/currentsegment.md) — The currently playing segment.
- [segments](avplayeritemintegratedtimelinesnapshot/segments.md) — The segments for this snapshot.
- [currentTime](avplayeritemintegratedtimelinesnapshot/currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
- [currentDate](avplayeritemintegratedtimelinesnapshot/currentdate.md) — The current date on the integrated timeline when the system created the snapshot.
