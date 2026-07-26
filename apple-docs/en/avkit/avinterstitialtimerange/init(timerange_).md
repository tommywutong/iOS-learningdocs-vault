---
title: 'init(timeRange:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterstitialtimerange/init(timerange:)'
source_url: 'https://developer.apple.com/documentation/avkit/avinterstitialtimerange/init(timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterstitialtimerange/init%28timerange%3A%29.json'
content_hash: 'sha256:1cda1d632d9d22a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterstitialTimeRange](../avinterstitialtimerange.md)

# init(timeRange:)

<sub>Initializer</sub>

Initializes an interstitial time range object with the specified time range.

<sub>tvOS</sub>

```swift
init(timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The time range to designate as interstitial content.

## Return Value

A new interstitial time range object.

## Discussion

To associate interstitial time ranges with an asset for playback, use the [interstitialTimeRanges](../../avfoundation/avplayeritem/interstitialtimeranges.md) property of an [AVPlayerItem](../../avfoundation/avplayeritem.md) object.
