---
title: 'playerViewController(_:skipToNextChannel:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptonextchannel:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptonextchannel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Askiptonextchannel%3A%29.json'
content_hash: 'sha256:6a44a72ae2d0d988'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:skipToNextChannel:)

<sub>Instance Method</sub>

Tells the delegate when the user wants to skip to the next channel.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, skipToNextChannel completion: @escaping @Sendable (Bool) -> Void)
```

<sub>tvOS</sub>

```swift
optional func playerViewControllerSkipToNextChannel(_ playerViewController: AVPlayerViewController) async -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

- `completion` — A completion callback to invoke to dismiss the channel’s interstitial view.

## Discussion

To enable channel skipping, adopt this method and replace the current player item with one that reflects the next channel’s content, and call the completion handler to dismiss the channel’s interstitial view. Each call to this method should advance one channel, relative to the previous request, even if the prior request hasn’t yet completed.

> [!important] Important
> Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## See Also

### Responding to Channel Changes

- [- playerViewController:skipToPreviousChannel:](<playerviewcontroller(__skiptopreviouschannel_).md>) — Tells the delegate when the user wants to skip to the previous channel.
- [- nextChannelInterstitialViewControllerForPlayerViewController:](<nextchannelinterstitialviewcontroller(for_).md>) — Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [- previousChannelInterstitialViewControllerForPlayerViewController:](<previouschannelinterstitialviewcontroller(for_).md>) — Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.
