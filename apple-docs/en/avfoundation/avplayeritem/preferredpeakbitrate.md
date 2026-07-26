---
title: preferredPeakBitRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/preferredpeakbitrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredpeakbitrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/preferredpeakbitrate.json'
content_hash: 'sha256:43ddc1687a96b88a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# preferredPeakBitRate

<sub>Instance Property</sub>

The desired limit, in bits per second, of network bandwidth consumption for this item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var preferredPeakBitRate: Double { get set }
```

## Discussion

Set `preferredPeakBitRate` to nonzero to indicate that the player should attempt to limit item playback to that bit rate, expressed in bits per second.

If the system can’t lower network bandwidth consumption to meet the this value, it reduces it as much as possible while it continues to play the item.

## See Also

### Configuring network behavior

- [preferredForwardBufferDuration](preferredforwardbufferduration.md) — The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.
- [canUseNetworkResourcesForLiveStreamingWhilePaused](canusenetworkresourcesforlivestreamingwhilepaused.md) — A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.
