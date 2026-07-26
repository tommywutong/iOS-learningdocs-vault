---
title: 'previousChannelInterstitialViewController(for:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller%28for%3A%29.json'
content_hash: 'sha256:7593762fd487177d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# previousChannelInterstitialViewController(for:)

<sub>Instance Method</sub>

Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.

<sub>tvOS</sub>

```swift
optional func previousChannelInterstitialViewController(for playerViewController: AVPlayerViewController) -> UIViewController
```

## Parameters

- `playerViewController` — The player view controller.

## Discussion

The framework calls this method when the user initiates, but hasn’t yet committed, a change in channel. The framework may call this method while a previous channel’s interstitial view is visible (on screen, or transitioning).

> [!important] Important
> Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## See Also

### Responding to Channel Changes

- [- playerViewController:skipToNextChannel:](<playerviewcontroller(__skiptonextchannel_).md>) — Tells the delegate when the user wants to skip to the next channel.
- [- playerViewController:skipToPreviousChannel:](<playerviewcontroller(__skiptopreviouschannel_).md>) — Tells the delegate when the user wants to skip to the previous channel.
- [- nextChannelInterstitialViewControllerForPlayerViewController:](<nextchannelinterstitialviewcontroller(for_).md>) — Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
