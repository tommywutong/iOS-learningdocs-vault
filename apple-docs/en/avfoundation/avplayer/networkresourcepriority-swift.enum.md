---
title: AVPlayer.NetworkResourcePriority
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/networkresourcepriority-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum.json'
content_hash: 'sha256:762ffd72382f6686'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.NetworkResourcePriority

<sub>Enumeration</sub>

This defines the network resource priority for a player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NetworkResourcePriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Priorities

- [AVPlayerNetworkResourcePriorityDefault](networkresourcepriority-swift.enum/default.md) — The default priority level given to a player for loading network resources. Use this when the player requires an optimal level of network resources and streaming in high-quality resolution is ideal. Players with AVPlayerNetworkResourcePriorityHigh will take precedence over this player. This player will take precedence over players with AVPlayerNetworkResourcePriorityLow.
- [AVPlayerNetworkResourcePriorityHigh](networkresourcepriority-swift.enum/high.md) — Indicates a high priority level for loading network resources. Use this when the player requires a high level of network resources and streaming in high-quality resolution is crucial. This player will take precedence over other lower priority players.
- [AVPlayerNetworkResourcePriorityLow](networkresourcepriority-swift.enum/low.md) — Indicates a low priority level for loading network resources. Use this when the player requires minimal network bandwidth and streaming in high-quality resolution is not crucial. Other players with higher priority will take precedence over this player.

### Initializers

- [init(rawValue:)](<networkresourcepriority-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the network resource priority

- [networkResourcePriority](networkresourcepriority-swift.property.md) — Indicates the priority of this player for network bandwidth resource distribution.
