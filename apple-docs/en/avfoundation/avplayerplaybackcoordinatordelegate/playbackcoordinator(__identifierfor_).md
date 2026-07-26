---
title: 'playbackCoordinator(_:identifierFor:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:identifierfor:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:identifierfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator%28_%3Aidentifierfor%3A%29.json'
content_hash: 'sha256:559253634aafbdf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerPlaybackCoordinatorDelegate](../avplayerplaybackcoordinatordelegate.md)

# playbackCoordinator(_:identifierFor:)

<sub>Instance Method</sub>

Returns an identifier for a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func playbackCoordinator(_ coordinator: AVPlayerPlaybackCoordinator, identifierFor playerItem: AVPlayerItem) -> String
```

## Parameters

- `coordinator` — The object coordinating playback.

- `playerItem` — The player item to return an identifier for.

## Return Value

An identifier string.

## Discussion

A coordinator calls this method to identify the items that its player object plays.

Implement this method to enable the coordinator to establish the identity of items that have different URLs. For example, two participants may play the same item, but one plays the item from a remote host and the other from a local version on a device.

If you don’t implement this method, the coordinator derives an identifier from the item’s asset.
