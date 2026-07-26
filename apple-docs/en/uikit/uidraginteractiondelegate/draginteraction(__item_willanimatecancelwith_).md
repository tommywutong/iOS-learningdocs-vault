---
title: 'dragInteraction(_:item:willAnimateCancelWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:item:willanimatecancelwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:item:willanimatecancelwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Aitem%3Awillanimatecancelwith%3A%29.json'
content_hash: 'sha256:7c9c2a34331bfd55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:item:willAnimateCancelWith:)

<sub>Instance Method</sub>

Tells the delegate the system’s cancellation animation is about to start.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, item: UIDragItem, willAnimateCancelWith animator: any UIDragAnimating)
```

## Parameters

- `interaction` — The interaction that called this method.

- `item` — The current drag item.

- `animator` — The animator that provides custom animations to run alongside the system’s animation. You can also use it to add a completion block that runs after the animations have finished.

## Discussion

This method is called for each drag item, whether it is visible or not.

To add a custom animation block that runs during the cancellation animation, pass the block to the animator’s [- addAnimations:](<../uidraganimating/addanimations(__).md>) method.

To add a completion block that runs after the cancellation animation has finished, pass the block to the animator’s [- addCompletion:](<../uidraganimating/addcompletion(__).md>) method.

## See Also

### Animating the drag behaviors

- [- dragInteraction:willAnimateLiftWithAnimator:session:](<draginteraction(__willanimateliftwith_session_).md>) — Tells the delegate the system’s lift animation is about to start.
