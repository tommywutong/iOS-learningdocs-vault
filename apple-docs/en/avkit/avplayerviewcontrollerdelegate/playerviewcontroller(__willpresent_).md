---
title: 'playerViewController(_:willPresent:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willpresent:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willpresent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Awillpresent%3A%29.json'
content_hash: 'sha256:4878f7967f85bd69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:willPresent:)

<sub>Instance Method</sub>

Tells the delegate when the player view controller is about to start playing a range of interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willPresent interstitial: AVInterstitialTimeRange)
```

## Parameters

- `playerViewController` — The player view controller.

- `interstitial` — The time range of interstitial content that’s about to begin.

## Discussion

Interstitial content is material unrelated to the main content of a presentation that may have special playback options or requirements. For example, implement this method to record when a user begins viewing an advertisement, or to enable the player view controller’s [requiresLinearPlayback](../avplayerviewcontroller/requireslinearplayback.md) property to prevent skipping mandatory legal notices.

Use the [interstitialTimeRanges](../../avfoundation/avplayeritem/interstitialtimeranges.md) property to identify the time ranges of interstitial content in the media timeline.

## See Also

### Responding to Interstitial Content Playback Events

- [- playerViewController:didPresentInterstitialTimeRange:](<playerviewcontroller(__didpresent_).md>) — Tells the delegate when the player view controller finishes playing a range of interstitial content.
