---
title: AVPlayer.NetworkResourcePriority.default
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/networkresourcepriority-swift.enum/default
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum/default.json'
content_hash: 'sha256:dc24bd5c269c8131'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [NetworkResourcePriority](../networkresourcepriority-swift.enum.md)

# AVPlayer.NetworkResourcePriority.default

<sub>Case</sub>

The default priority level given to a player for loading network resources. Use this when the player requires an optimal level of network resources and streaming in high-quality resolution is ideal. Players with AVPlayerNetworkResourcePriorityHigh will take precedence over this player. This player will take precedence over players with AVPlayerNetworkResourcePriorityLow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case `default`
```

## See Also

### Priorities

- [AVPlayerNetworkResourcePriorityHigh](high.md) — Indicates a high priority level for loading network resources. Use this when the player requires a high level of network resources and streaming in high-quality resolution is crucial. This player will take precedence over other lower priority players.
- [AVPlayerNetworkResourcePriorityLow](low.md) — Indicates a low priority level for loading network resources. Use this when the player requires minimal network bandwidth and streaming in high-quality resolution is not crucial. Other players with higher priority will take precedence over this player.
