---
title: forwardPlaybackEndTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/forwardplaybackendtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/forwardplaybackendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/forwardplaybackendtime.json'
content_hash: 'sha256:02a85effb94353b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# forwardPlaybackEndTime

<sub>Instance Property</sub>

The time at which forward playback ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var forwardPlaybackEndTime: CMTime { get set }
```

## Discussion

The value indicates the time at which playback should end when the playback rate is positive (see `AVPlayer`’s [rate](../avplayer/rate.md) property).

The default value is [invalid](../../coremedia/cmtime/invalid.md), which indicates that no end time for forward playback is specified. In this case, the effective end time for forward playback is the item’s duration.

The value of this property has no effect on playback when the rate is negative.

## See Also

### Setting playback boundaries

- [reversePlaybackEndTime](reverseplaybackendtime.md) — The time at which reverse playback ends.
