---
title: 'update(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipercentdriveninteractivetransition/update(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/update(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/update%28_%3A%29.json'
content_hash: 'sha256:cd7c835d26110002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# update(_:)

<sub>Instance Method</sub>

Updates the completion percentage of the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func update(_ percentComplete: CGFloat)
```

## Parameters

- `percentComplete` — The percentage of the transition that is currently complete, specified as a floating-point number in the range `0.0` to `1.0`. If you specify a value less than `0.0`, this method changes it to `0.0`. Specifying a value greater than `1.0` would cause the animation to appear complete already.

## Discussion

This is a convenience method that calls through to the [- updateInteractiveTransition:](<../uiviewcontrollercontexttransitioning/updateinteractivetransition(__).md>) method of the context object.

While tracking user events, your code should call this method regularly to update the current progress toward completing the transition. If, during tracking, the interactions cross a threshold that you consider signifies the completion or cancellation of the transition, stop tracking events and call the [- finishInteractiveTransition](<finish().md>) or [- cancelInteractiveTransition](<cancel().md>) method.

## See Also

### Managing a transition

- [- pauseInteractiveTransition](<pause().md>) — Pauses an interruptible transition animation.
- [- cancelInteractiveTransition](<cancel().md>) — Notifies the system that user interactions canceled the transition.
- [- finishInteractiveTransition](<finish().md>) — Notifies the system that user interactions signaled the completion of the transition.
