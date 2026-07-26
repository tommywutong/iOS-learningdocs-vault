---
title: 'animateTransition(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrolleranimatedtransitioning/animatetransition(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/animatetransition(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrolleranimatedtransitioning/animatetransition%28using%3A%29.json'
content_hash: 'sha256:bb87b7871f94e803'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md)

# animateTransition(using:)

<sub>Instance Method</sub>

Tells your animator object to perform the transition animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func animateTransition(using transitionContext: any UIViewControllerContextTransitioning)
```

## Parameters

- `transitionContext` — The context object containing information about the transition.

## Discussion

UIKit calls this method when presenting or dismissing a view controller. Use this method to configure the animations associated with your custom transition. You can use view-based animations or Core Animation to configure your animations.

All animations must take place in the view specified by the [containerView](../uiviewcontrollercontexttransitioning/containerview.md) property of `transitionContext`. Add the view being presented (or revealed if the transition involves dismissing a view controller) to the container view’s hierarchy and set up any animations you want to make that view move into position. If you want to draw to the screen directly without a view, use this method to configure a [CADisplayLink](../../quartzcore/cadisplaylink.md) object instead.

You can retrieve the view controllers involved in the transition from the [- viewControllerForKey:](<../uiviewcontrollercontexttransitioning/viewcontroller(forkey_).md>) method of `transitionContext`. For more information about the information provided by the context object, see [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md).

## See Also

### Performing a transition

- [- animationEnded:](<animationended(__).md>) — Tells your animator object that the transition animations have finished.
