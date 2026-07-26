---
title: pauseInteractiveTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/pauseinteractivetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/pauseinteractivetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/pauseinteractivetransition%28%29.json'
content_hash: 'sha256:1f38e39d9582f08a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# pauseInteractiveTransition()

<sub>Instance Method</sub>

Tells the system to pause the animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pauseInteractiveTransition()
```

## Discussion

You can call this method in the middle of an interruptible animation to pause it.

## See Also

### Reporting the transition progress

- [- completeTransition:](<completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- updateInteractiveTransition:](<updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
- [transitionWasCancelled](transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.
