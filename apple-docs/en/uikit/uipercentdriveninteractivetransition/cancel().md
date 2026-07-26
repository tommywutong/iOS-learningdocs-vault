---
title: cancel()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/cancel()
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/cancel%28%29.json'
content_hash: 'sha256:b09654e0a20f4d00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# cancel()

<sub>Instance Method</sub>

Notifies the system that user interactions canceled the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancel()
```

## Discussion

This is a convenience method that calls through to the [- cancelInteractiveTransition](<../uiviewcontrollercontexttransitioning/cancelinteractivetransition().md>) method of the context object.

While tracking user interactions, your gesture recognizer or event-handling code would call this method when interactions suggest that the user wants to cancel or abort the view controller transition. For example, if the user reverses the swipe direction and then touch events end, suggesting that the user decided against the transition, you would call this method.

## See Also

### Managing a transition

- [- updateInteractiveTransition:](<update(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pause().md>) — Pauses an interruptible transition animation.
- [- finishInteractiveTransition](<finish().md>) — Notifies the system that user interactions signaled the completion of the transition.
