---
title: reversePlaybackEndTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/reverseplaybackendtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/reverseplaybackendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/reverseplaybackendtime.json'
content_hash: 'sha256:174d6099e8dd9568'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# reversePlaybackEndTime

<sub>Instance Property</sub>

The time at which reverse playback ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var reversePlaybackEndTime: CMTime { get set }
```

## Discussion

The value indicated the time at which playback should end when the playback rate is negative (see `AVPlayer`’s [rate](../avplayer/rate.md) property).

The default value is [invalid](../../coremedia/cmtime/invalid.md), which indicates that no end time for reverse playback is specified. In this case, the effective end time for reverse playback is [zero](../../coremedia/cmtime/zero.md).

The value of this property has no effect on playback when the rate is positive.

## See Also

### Setting playback boundaries

- [forwardPlaybackEndTime](forwardplaybackendtime.md) — The time at which forward playback ends.
