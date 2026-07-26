---
title: cancelInteractiveTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/cancelinteractivetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/cancelinteractivetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/cancelinteractivetransition%28%29.json'
content_hash: 'sha256:f8af412aeaba5efe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# cancelInteractiveTransition()

<sub>Instance Method</sub>

Notifies the system that user interactions canceled the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancelInteractiveTransition()
```

## Discussion

While tracking user interactions, gesture recognizers or your interactive animator object should call this method when interactions suggest that the user wants to cancel or abort the view controller transition. For example, if the user reverses the swipe direction and touch events end, suggesting that the user decided against the transition, you would call this method.

Always follow calls to this method with a call to the [- completeTransition:](<completetransition(__).md>) method to finalize the transition.

## See Also

### Reporting the transition progress

- [- completeTransition:](<completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- updateInteractiveTransition:](<updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [transitionWasCancelled](transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.
