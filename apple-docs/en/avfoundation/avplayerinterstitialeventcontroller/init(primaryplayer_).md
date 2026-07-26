---
title: 'init(primaryPlayer:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerinterstitialeventcontroller/init(primaryplayer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/init(primaryplayer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/init%28primaryplayer%3A%29.json'
content_hash: 'sha256:97e855da26371746'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# init(primaryPlayer:)

<sub>Initializer</sub>

Creates an event controller with a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(primaryPlayer: AVPlayer)
```

## Parameters

- `primaryPlayer` — A player that plays primary content. The system raises an exception you specify an interstitial player for this argument.
