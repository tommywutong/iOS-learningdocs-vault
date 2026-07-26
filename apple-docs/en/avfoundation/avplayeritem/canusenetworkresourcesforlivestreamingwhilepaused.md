---
title: canUseNetworkResourcesForLiveStreamingWhilePaused
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused.json'
content_hash: 'sha256:ea6cefcc196735f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# canUseNetworkResourcesForLiveStreamingWhilePaused

<sub>Instance Property</sub>

A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool { get set }
```

## Discussion

For live streaming content, the player item may need to use extra networking and power resources to keep playback state up to date when paused.  For example, when this property is set to true, the [seekableTimeRanges](seekabletimeranges.md) property will be periodically updated to reflect the current state of the live stream.

To minimize power usage, avoid setting this property to `true` when you do not need playback state to stay up to date while paused.

## See Also

### Configuring network behavior

- [preferredPeakBitRate](preferredpeakbitrate.md) — The desired limit, in bits per second, of network bandwidth consumption for this item.
- [preferredForwardBufferDuration](preferredforwardbufferduration.md) — The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.
