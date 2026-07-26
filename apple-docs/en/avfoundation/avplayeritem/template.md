---
title: template
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/template
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/template'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/template.json'
content_hash: 'sha256:b6122d1f47cfa85c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# template

<sub>Instance Property</sub>

The template player item that initializes this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var template: AVPlayerItem? { get }
```

## See Also

### Configuring interstitial events

- [integratedTimeline](integratedtimeline.md) — An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [automaticallyHandlesInterstitialEvents](automaticallyhandlesinterstitialevents.md) — A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [translatesPlayerInterstitialEvents](translatesplayerinterstitialevents.md) — A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [interstitialTimeRanges](interstitialtimeranges.md) — An array of time ranges that identify interstitial content.
