---
title: integratedTimeline
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/integratedtimeline
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/integratedtimeline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/integratedtimeline.json'
content_hash: 'sha256:0da7c45e8d8ffc45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# integratedTimeline

<sub>Instance Property</sub>

An integrated timeline that represents the player item timing including its scheduled interstitial events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var integratedTimeline: AVPlayerItemIntegratedTimeline { get }
```

## Discussion

The value is `nil` for player items in an interstitial player.

## See Also

### Configuring interstitial events

- [automaticallyHandlesInterstitialEvents](automaticallyhandlesinterstitialevents.md) — A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [translatesPlayerInterstitialEvents](translatesplayerinterstitialevents.md) — A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [interstitialTimeRanges](interstitialtimeranges.md) — An array of time ranges that identify interstitial content.
- [templatePlayerItem](template.md) — The template player item that initializes this instance.
