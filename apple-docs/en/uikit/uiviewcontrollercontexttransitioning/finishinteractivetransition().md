---
title: finishInteractiveTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/finishinteractivetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/finishinteractivetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/finishinteractivetransition%28%29.json'
content_hash: 'sha256:9e9c7769f56b840a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# finishInteractiveTransition()

<sub>Instance Method</sub>

Notifies the system that user interactions signaled the completion of the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finishInteractiveTransition()
```

## Discussion

While tracking user interactions, gesture recognizers or your interactive animator object should call this method when the interactions suggest that the transition is now complete. For example, if the user swipes a finger, and the touch events indicate that the swipe distance crossed the threshold needed to complete the gesture, call this method when the corresponding touch events end to let the system know that it can now complete the transition.

Always follow calls to this method with a call to the [- completeTransition:](<completetransition(__).md>) method to finalize the transition.

## See Also

### Reporting the transition progress

- [- completeTransition:](<completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- updateInteractiveTransition:](<updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
- [transitionWasCancelled](transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.
