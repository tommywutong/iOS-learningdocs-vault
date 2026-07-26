---
title: pause()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/pause()
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/pause()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/pause%28%29.json'
content_hash: 'sha256:81e7c1006caf0624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# pause()

<sub>Instance Method</sub>

Pauses an interruptible transition animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pause()
```

## Discussion

This is a convenience method that calls through to the [- pauseInteractiveTransition](<../uiviewcontrollercontexttransitioning/pauseinteractivetransition().md>) method of the context object. You might call this method so that you can begin driving an animation interactively. For example, when the user’s finger touches the screen, your gesture handler would call this method to stop the animation and then use changes to the touch location to update the [percentComplete](percentcomplete.md) property.

## See Also

### Managing a transition

- [- updateInteractiveTransition:](<update(__).md>) — Updates the completion percentage of the transition.
- [- cancelInteractiveTransition](<cancel().md>) — Notifies the system that user interactions canceled the transition.
- [- finishInteractiveTransition](<finish().md>) — Notifies the system that user interactions signaled the completion of the transition.
