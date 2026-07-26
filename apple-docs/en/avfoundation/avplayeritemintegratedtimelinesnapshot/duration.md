---
title: duration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/duration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/duration.json'
content_hash: 'sha256:ee99e0f3315c9426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md)

# duration

<sub>Instance Property</sub>

The total duration of the primary item and scheduled interstitial events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var duration: CMTime { get }
```

## Discussion

The duration property takes into account the interstitial event’s [playoutLimit](../avplayerinterstitialevent/playoutlimit.md) and [resumptionOffset](../avplayerinterstitialevent/resumptionoffset.md) values.

Before loading the duration of the primary item, the value of this property is [invalid](../../coremedia/cmtime/invalid.md). For livestreams, this value is [indefinite](../../coremedia/cmtime/indefinite.md).

## See Also

### Inspecting the snapshot

- [currentSegment](currentsegment.md) — The currently playing segment.
- [segments](segments.md) — The segments for this snapshot.
- [AVPlayerItemSegment](../avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentTime](currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
- [currentDate](currentdate.md) — The current date on the integrated timeline when the system created the snapshot.
