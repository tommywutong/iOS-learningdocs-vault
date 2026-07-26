---
title: hasSufficientMediaDataForReliablePlaybackStart
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+（27.0 起废弃）, iPadOS 14.5+（27.0 起废弃）, Mac Catalyst 14.5+（27.0 起废弃）, macOS 11.3+（27.0 起废弃）, tvOS 14.5+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.4+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.json'
content_hash: 'sha256:7e55164f9589206a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# hasSufficientMediaDataForReliablePlaybackStart

<sub>Instance Property</sub>

A Boolean value that indicates whether the enqued media meets the required preroll level for reliable playback.

> [!warning] Deprecated
> For smooth playback, attach the renderer to a render synchronizer and set the synchronizer's delaysRateChangeUntilHasSufficientMediaData property to true instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

## Discussion

Starting playback when this property is [false](../../swift/false.md) may prevent smooth playback following an immediate start.
