---
title: currentDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentdate.json'
content_hash: 'sha256:cf220d0eb82a77fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md)

# currentDate

<sub>Instance Property</sub>

The current date on the integrated timeline when the system created the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentDate: Date? { get }
```

## Discussion

This value is `nil` if playback doesn’t map to a date.

## See Also

### Inspecting the snapshot

- [duration](duration.md) — The total duration of the primary item and scheduled interstitial events.
- [currentSegment](currentsegment.md) — The currently playing segment.
- [segments](segments.md) — The segments for this snapshot.
- [AVPlayerItemSegment](../avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentTime](currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
