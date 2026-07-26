---
title: 'updateInteractiveTransition(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/updateinteractivetransition(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/updateinteractivetransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/updateinteractivetransition%28_%3A%29.json'
content_hash: 'sha256:fdcde756f3a39d04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# updateInteractiveTransition(_:)

<sub>Instance Method</sub>

Updates the completion percentage of the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateInteractiveTransition(_ percentComplete: CGFloat)
```

## Discussion

While tracking user events, gesture recognizers or your interactive animator objects should call this method regularly to update the progress toward completing the transition. If, during tracking, the interactions cross a threshold that you consider signifies the completion or cancellation of the transition, stop tracking events and call the [- finishInteractiveTransition](<finishinteractivetransition().md>) or [- cancelInteractiveTransition](<cancelinteractivetransition().md>) method.

## See Also

### Reporting the transition progress

- [- completeTransition:](<completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- pauseInteractiveTransition](<pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
- [transitionWasCancelled](transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.
