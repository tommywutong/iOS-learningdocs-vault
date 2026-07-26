---
title: primaryItem
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/primaryitem
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/primaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/primaryitem.json'
content_hash: 'sha256:05cb4f3202909a51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# primaryItem

<sub>Instance Property</sub>

The player item that represents the primary content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var primaryItem: AVPlayerItem? { get }
```

## Discussion

The item must contain an [AVAsset](../avasset.md) that provides intrinsic mappings from its timeline to realtime dates.

## See Also

### Accessing player items

- [templateItems](templateitems.md) — An array of player item configurations to use as templates for player items that play interstitial content.
