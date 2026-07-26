---
title: 'playerViewController(_:willTransitionToVisibilityOfTransportBar:with:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Awilltransitiontovisibilityoftransportbar%3Awith%3A%29.json'
content_hash: 'sha256:d5a7fbc9cc9b4205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:willTransitionToVisibilityOfTransportBar:with:)

<sub>Instance Method</sub>

Tells the delegate when the transport bar’s visibility is about to change.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willTransitionToVisibilityOfTransportBar visible: Bool, with coordinator: any AVPlayerViewControllerAnimationCoordinator)
```

## Parameters

- `playerViewController` — The player view controller.

- `visible` — The transport bar’s new visibility.

- `coordinator` — The animation coordinator to use to synchronize animations with the transport bar visibility.

## See Also

### Responding to Transport Bar Changes

- [AVPlayerViewControllerAnimationCoordinator](../avplayerviewcontrolleranimationcoordinator.md) — A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.
