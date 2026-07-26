---
title: 'startInteractiveTransition(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerinteractivetransitioning/startinteractivetransition%28_%3A%29.json'
content_hash: 'sha256:fc4847389ac41515'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md)

# startInteractiveTransition(_:)

<sub>Instance Method</sub>

Called when the system needs to set up the interactive portions of a view controller transition and start the animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startInteractiveTransition(_ transitionContext: any UIViewControllerContextTransitioning)
```

## Parameters

- `transitionContext` — The context object containing information about the transition.

## Discussion

Your implementation of this method should use the data in the `transitionContext` parameter to configure user interactivity for the transition and then start the animations. While tracking user interactions, your event handling code should regularly call the context object’s [- updateInteractiveTransition:](<../uiviewcontrollercontexttransitioning/updateinteractivetransition(__).md>) method to report on how much of the transition is now complete. If events indicate that the user has canceled the transition, call the [- cancelInteractiveTransition](<../uiviewcontrollercontexttransitioning/cancelinteractivetransition().md>) method. If events indicate that the transition has finished, call the [- finishInteractiveTransition](<../uiviewcontrollercontexttransitioning/finishinteractivetransition().md>) method.

## See Also

### Starting an interactive transition

- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the transition is interactive when it starts.
