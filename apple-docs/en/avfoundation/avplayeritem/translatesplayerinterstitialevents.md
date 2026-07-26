---
title: translatesPlayerInterstitialEvents
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/translatesplayerinterstitialevents
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/translatesplayerinterstitialevents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/translatesplayerinterstitialevents.json'
content_hash: 'sha256:422520319ed4b44a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# translatesPlayerInterstitialEvents

<sub>Instance Property</sub>

A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.

<sub>tvOS</sub>

```swift
var translatesPlayerInterstitialEvents: Bool { get set }
```

## Discussion

Enable this property value to support using interstitial events, or set it to [false](../../swift/false.md) to perform your own interstitial management.

## See Also

### Configuring interstitial events

- [integratedTimeline](integratedtimeline.md) — An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [automaticallyHandlesInterstitialEvents](automaticallyhandlesinterstitialevents.md) — A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [interstitialTimeRanges](interstitialtimeranges.md) — An array of time ranges that identify interstitial content.
- [templatePlayerItem](template.md) — The template player item that initializes this instance.
