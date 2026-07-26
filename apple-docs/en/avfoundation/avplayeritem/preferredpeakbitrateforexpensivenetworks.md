---
title: preferredPeakBitRateForExpensiveNetworks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/preferredpeakbitrateforexpensivenetworks
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredpeakbitrateforexpensivenetworks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/preferredpeakbitrateforexpensivenetworks.json'
content_hash: 'sha256:97b8fb8534742224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# preferredPeakBitRateForExpensiveNetworks

<sub>Instance Property</sub>

A limit of network bandwidth consumption by the item when connecting over expensive networks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var preferredPeakBitRateForExpensiveNetworks: Double { get set }
```

## Discussion

When this value is nonzero, the player attempts to limit item playback by the specified bit rate when streaming over an expensive network, such as a cellular data plan. If the system can’t reduce the bit rate to meet this value, it reduces it as much as possible while it continues to play the item.

> [!note] Note
> The value of the [preferredPeakBitRate](preferredpeakbitrate.md) property applies unconditionally. This property value has no effect if this property value is less restrictive than the [preferredPeakBitRate](preferredpeakbitrate.md) value.

## See Also

### Configuring expensive network behavior

- [preferredMaximumResolutionForExpensiveNetworks](preferredmaximumresolutionforexpensivenetworks.md) — An upper limit on the resolution of video to download when connecting over expensive networks.
