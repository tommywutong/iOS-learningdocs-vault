---
title: networkResourcePriority
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/networkresourcepriority-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/networkresourcepriority-swift.property.json'
content_hash: 'sha256:0dc6d117e2535662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# networkResourcePriority

<sub>Instance Property</sub>

Indicates the priority of this player for network bandwidth resource distribution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var networkResourcePriority: AVPlayer.NetworkResourcePriority { get set }
```

## Discussion

This value determines the priority of the player during network resource allocation among all other players within the same application process. The default value for this is AVPlayerNetworkResourcePriorityDefault.

## See Also

### Configuring the network resource priority

- [NetworkResourcePriority](networkresourcepriority-swift.enum.md) — This defines the network resource priority for a player.
