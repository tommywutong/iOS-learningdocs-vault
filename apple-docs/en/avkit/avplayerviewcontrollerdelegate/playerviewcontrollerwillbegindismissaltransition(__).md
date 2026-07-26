---
title: 'playerViewControllerWillBeginDismissalTransition(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition%28_%3A%29.json'
content_hash: 'sha256:10884a68c185b0aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerWillBeginDismissalTransition(_:)

<sub>Instance Method</sub>

Tells the delegate when the player view controller is about to start its dismissal transition.

<sub>tvOS</sub>

```swift
optional func playerViewControllerWillBeginDismissalTransition(_ playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController` — The player view controller.

## See Also

### Dismissing the Player View Controller

- [- playerViewControllerShouldDismiss:](<playerviewcontrollershoulddismiss(__).md>) — Asks the delegate object whether the player view controller dismisses itself upon request.
- [- playerViewControllerDidEndDismissalTransition:](<playerviewcontrollerdidenddismissaltransition(__).md>) — Tells the delegate when the player view controller ends its dismissal transition.
