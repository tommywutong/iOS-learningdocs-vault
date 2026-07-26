---
title: 'tabBarController(_:animationControllerForTransitionFrom:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:animationcontrollerfortransitionfrom:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:animationcontrollerfortransitionfrom:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Aanimationcontrollerfortransitionfrom%3Ato%3A%29.json'
content_hash: 'sha256:affecd1a0f0d0b96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:animationControllerForTransitionFrom:to:)

<sub>Instance Method</sub>

Called to allow the delegate to return a [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, animationControllerForTransitionFrom fromVC: UIViewController, to toVC: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

## Parameters

- `tabBarController` — The tab bar controller whose view controller is transitioning.

- `fromVC` — The currently visible view controller.

- `toVC` — The view controller intended to be visible after the transition ends.

## Return Value

The [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) delegate object responsible for managing the tab bar view controller transition animation.

## See Also

### Supporting custom tab bar transition animations

- [- tabBarController:interactionControllerForAnimationController:](<tabbarcontroller(__interactioncontrollerfor_).md>) — Called to allow the delegate to return a [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.
