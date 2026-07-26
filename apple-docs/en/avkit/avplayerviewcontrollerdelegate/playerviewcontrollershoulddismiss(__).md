---
title: 'playerViewControllerShouldDismiss(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss%28_%3A%29.json'
content_hash: 'sha256:98fcfe693b5b0458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerShouldDismiss(_:)

<sub>Instance Method</sub>

Asks the delegate object whether the player view controller dismisses itself upon request.

<sub>tvOS</sub>

```swift
optional func playerViewControllerShouldDismiss(_ playerViewController: AVPlayerViewController) -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

## Return Value

`true` if the player view controller should dismiss itself; otherwise `false`.

## Discussion

If allowed, the player view controller dismisses itself with animation. If you’ve embedded the player view controller in another view, the delegate may need to manually dismiss the view controller.

## See Also

### Dismissing the Player View Controller

- [- playerViewControllerWillBeginDismissalTransition:](<playerviewcontrollerwillbegindismissaltransition(__).md>) — Tells the delegate when the player view controller is about to start its dismissal transition.
- [- playerViewControllerDidEndDismissalTransition:](<playerviewcontrollerdidenddismissaltransition(__).md>) — Tells the delegate when the player view controller ends its dismissal transition.
