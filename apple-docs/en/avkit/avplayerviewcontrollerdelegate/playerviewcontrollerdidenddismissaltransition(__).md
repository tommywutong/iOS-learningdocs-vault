---
title: 'playerViewControllerDidEndDismissalTransition(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition%28_%3A%29.json'
content_hash: 'sha256:10f079514756ca93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerDidEndDismissalTransition(_:)

<sub>Instance Method</sub>

Tells the delegate when the player view controller ends its dismissal transition.

<sub>tvOS</sub>

```swift
optional func playerViewControllerDidEndDismissalTransition(_ playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController` — The player view controller.

## See Also

### Dismissing the Player View Controller

- [- playerViewControllerShouldDismiss:](<playerviewcontrollershoulddismiss(__).md>) — Asks the delegate object whether the player view controller dismisses itself upon request.
- [- playerViewControllerWillBeginDismissalTransition:](<playerviewcontrollerwillbegindismissaltransition(__).md>) — Tells the delegate when the player view controller is about to start its dismissal transition.
