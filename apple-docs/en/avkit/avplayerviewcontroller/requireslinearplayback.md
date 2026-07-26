---
title: requiresLinearPlayback
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/requireslinearplayback
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requireslinearplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/requireslinearplayback.json'
content_hash: 'sha256:0c61772451b09e9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# requiresLinearPlayback

<sub>Instance Property</sub>

A Boolean value that determines whether the player allows the user to skip media content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var requiresLinearPlayback: Bool { get set }
```

## Discussion

If this value is `false` (the default), the controller’s user interface allows a user to fast-forward, scrub, or skip ahead to content later in the player’s presentation. To prevent the user from skipping content—for example, while presenting a legal notice or other mandatory interstitial content—set this property’s value to `true`.

To track when the player is presenting content for which you might require linear playback, use the [interstitialTimeRanges](../../avfoundation/avplayeritem/interstitialtimeranges.md) property of the view controller’s player item to define the time ranges of the interstitial content. The view controller then sends [- playerViewController:willPresentInterstitialTimeRange:](<../avplayerviewcontrollerdelegate/playerviewcontroller(__willpresent_).md>) and [- playerViewController:didPresentInterstitialTimeRange:](<../avplayerviewcontrollerdelegate/playerviewcontroller(__didpresent_).md>) messages to its [delegate](delegate.md) object when the content is playing. Implement these methods to enable or disable the [requiresLinearPlayback](requireslinearplayback.md) property as needed.
