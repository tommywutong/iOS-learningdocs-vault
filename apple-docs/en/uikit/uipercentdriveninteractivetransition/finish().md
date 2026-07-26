---
title: finish()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/finish()
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/finish%28%29.json'
content_hash: 'sha256:c15bd497271d6caa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# finish()

<sub>Instance Method</sub>

Notifies the system that user interactions signaled the completion of the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finish()
```

## Discussion

This is a convenience method that calls through to the [- finishInteractiveTransition](<../uiviewcontrollercontexttransitioning/finishinteractivetransition().md>) method of the context object.

While tracking user interactions, your gesture recognizer or event-handling code should call this methods when the interactions suggest that the transition is now complete. For example, if the user swipes a finger, and the touch events indicate that the swipe distance crossed the threshold needed to complete the gesture, call this method when the corresponding touch events end to let the system know that it can now complete the transition.

## See Also

### Managing a transition

- [- updateInteractiveTransition:](<update(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pause().md>) — Pauses an interruptible transition animation.
- [- cancelInteractiveTransition](<cancel().md>) — Notifies the system that user interactions canceled the transition.
