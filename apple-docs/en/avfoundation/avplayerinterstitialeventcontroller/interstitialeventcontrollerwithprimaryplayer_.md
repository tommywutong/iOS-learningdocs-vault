---
title: 'interstitialEventControllerWithPrimaryPlayer:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerinterstitialeventcontroller/interstitialeventcontrollerwithprimaryplayer:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/interstitialeventcontrollerwithprimaryplayer:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/interstitialeventcontrollerwithprimaryplayer%3A.json'
content_hash: 'sha256:3cd03ce9d20b58b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# interstitialEventControllerWithPrimaryPlayer:

<sub>Type Method</sub>

A convenience initializer that creates an event controller with a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) interstitialEventControllerWithPrimaryPlayer:(AVPlayer *) primaryPlayer;
```

## Parameters

- `primaryPlayer` — A player that plays primary content. The system raises an exception you specify an interstitial player for this argument.

## See Also

### Creating an event controller

- [- initWithPrimaryPlayer:](<init(primaryplayer_).md>) — Creates an event controller with a player item.
