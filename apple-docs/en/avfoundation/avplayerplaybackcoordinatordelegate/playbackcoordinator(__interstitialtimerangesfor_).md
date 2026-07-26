---
title: 'playbackCoordinator(_:interstitialTimeRangesFor:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 15.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:interstitialtimerangesfor:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:interstitialtimerangesfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator%28_%3Ainterstitialtimerangesfor%3A%29.json'
content_hash: 'sha256:3b07df6e22e65542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerPlaybackCoordinatorDelegate](../avplayerplaybackcoordinatordelegate.md)

# playbackCoordinator(_:interstitialTimeRangesFor:)

<sub>Instance Method</sub>

Asks the delegate for time ranges in a player item that don’t correspond to the primary content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func playbackCoordinator(_ coordinator: AVPlayerPlaybackCoordinator, interstitialTimeRangesFor playerItem: AVPlayerItem) -> [NSValue]
```

## Parameters

- `coordinator` — The object coordinating playback.

- `playerItem` — The player item for which to retrieve interstitial time ranges.

## Return Value

An array of [NSValue](../../foundation/nsvalue.md) objects that contain the interstitial time ranges.

## Discussion

Implementing this method enables the coordinator to synchronize playback between participants that have different interstitials stitched into the primary content timeline.

If you don’t implement this method, the coordinator assumes that the entire item corresponds to the primary content.
