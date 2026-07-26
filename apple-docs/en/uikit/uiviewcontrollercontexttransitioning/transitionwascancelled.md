---
title: transitionWasCancelled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/transitionwascancelled
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/transitionwascancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/transitionwascancelled.json'
content_hash: 'sha256:ffc5c072fd93b23b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# transitionWasCancelled

<sub>Instance Property</sub>

Returns a Boolean value indicating whether the transition was canceled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transitionWasCancelled: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the transition was canceled or [false](../../swift/false.md) if it is ongoing or finished normally.

## Discussion

You can call this method from your animator object to determine whether the transition has been canceled. Calling the [- cancelInteractiveTransition](<cancelinteractivetransition().md>) method causes this method to return [true](../../swift/true.md).

## See Also

### Reporting the transition progress

- [- completeTransition:](<completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- updateInteractiveTransition:](<updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
