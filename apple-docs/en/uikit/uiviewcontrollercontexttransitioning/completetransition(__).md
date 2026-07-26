---
title: 'completeTransition(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/completetransition(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/completetransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/completetransition%28_%3A%29.json'
content_hash: 'sha256:b0f51e7bd30fd37b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# completeTransition(_:)

<sub>Instance Method</sub>

Notifies the system that the transition animation is done.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func completeTransition(_ didComplete: Bool)
```

## Parameters

- `didComplete` — [true](../../swift/true.md) if the transition to the presented view controller completed successfully or [false](../../swift/false.md) if the original view controller is still being displayed.

## Discussion

You must call this method after your animations have completed to notify the system that the transition animation is done. The parameter you pass must indicate whether the animations completed successfully. For interactive animations, you must call this method in addition to the [- finishInteractiveTransition](<finishinteractivetransition().md>) or [- cancelInteractiveTransition](<cancelinteractivetransition().md>) method. The best place to call this method is in the completion block of your animations.

The default implementation of this method calls the animator object’s [- animationEnded:](<../uiviewcontrolleranimatedtransitioning/animationended(__).md>) method to give it a chance to perform any last minute cleanup.

## See Also

### Reporting the transition progress

- [- updateInteractiveTransition:](<updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
- [transitionWasCancelled](transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.
