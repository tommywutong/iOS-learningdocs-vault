---
title: 'dragInteraction(_:willAnimateLiftWith:session:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:willanimateliftwith:session:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:willanimateliftwith:session:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Awillanimateliftwith%3Asession%3A%29.json'
content_hash: 'sha256:5ac3f07a64ce751e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:willAnimateLiftWith:session:)

<sub>Instance Method</sub>

Tells the delegate the system’s lift animation is about to start.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, willAnimateLiftWith animator: any UIDragAnimating, session: any UIDragSession)
```

## Parameters

- `interaction` — The interaction that called this method.

- `animator` — The animator that provides custom animations to run alongside the system’s lift animation. You can also use it to add a completion block that runs after the animations have finished.

- `session` — The current drag session.

## Discussion

To add a custom animation block that runs during the lift animation, pass the block to the animator’s [- addAnimations:](<../uidraganimating/addanimations(__).md>) method.

To add a completion block that runs after the lift animation has finished, pass the block to the animator’s [- addCompletion:](<../uidraganimating/addcompletion(__).md>) method.

## See Also

### Animating the drag behaviors

- [- dragInteraction:item:willAnimateCancelWithAnimator:](<draginteraction(__item_willanimatecancelwith_).md>) — Tells the delegate the system’s cancellation animation is about to start.
