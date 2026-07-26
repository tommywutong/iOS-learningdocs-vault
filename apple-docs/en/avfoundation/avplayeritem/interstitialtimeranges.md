---
title: interstitialTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/interstitialtimeranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/interstitialtimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/interstitialtimeranges.json'
content_hash: 'sha256:70cbc0187f6c61e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# interstitialTimeRanges

<sub>Instance Property</sub>

An array of time ranges that identify interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interstitialTimeRanges: [AVInterstitialTimeRange] { get }
```

<sub>tvOS</sub>

```swift
var interstitialTimeRanges: [AVInterstitialTimeRange] { get set }
```

## Discussion

Interstitial content is material that’s unrelated to a player item’s primary content, such as advertisements and legal notices. If you use [AVPlayerViewController](../../avkit/avplayerviewcontroller.md) to present an item that contains interstitial time ranges, the user interface marks those time ranges differently on the playback timeline. A player view controller can also call your app when it begins and ends playing interstitial content. You can use these events to customize playback behavior, such as preventing viewers from skipping required content.

> [!note] Note
> On iOS, the stream must define the interstitial time ranges, or you must use [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md).

## See Also

### Configuring interstitial events

- [integratedTimeline](integratedtimeline.md) — An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [automaticallyHandlesInterstitialEvents](automaticallyhandlesinterstitialevents.md) — A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [translatesPlayerInterstitialEvents](translatesplayerinterstitialevents.md) — A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [templatePlayerItem](template.md) — The template player item that initializes this instance.
