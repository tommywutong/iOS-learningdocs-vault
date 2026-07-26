---
title: preferredForwardBufferDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/preferredforwardbufferduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredforwardbufferduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/preferredforwardbufferduration.json'
content_hash: 'sha256:e887976a7d2c2163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# preferredForwardBufferDuration

<sub>Instance Property</sub>

The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var preferredForwardBufferDuration: TimeInterval { get set }
```

## Discussion

This property defines the preferred forward buffer duration in seconds. If set to 0, the player will choose an appropriate level of buffering for most use cases. Setting this property to a low value will increase the chance that playback will stall and re-buffer, while setting it to a high value will increase demand on system resources.

## See Also

### Configuring network behavior

- [preferredPeakBitRate](preferredpeakbitrate.md) — The desired limit, in bits per second, of network bandwidth consumption for this item.
- [canUseNetworkResourcesForLiveStreamingWhilePaused](canusenetworkresourcesforlivestreamingwhilepaused.md) — A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.
