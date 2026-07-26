---
title: 'tabBarController(_:interactionControllerFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:interactioncontrollerfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:interactioncontrollerfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Ainteractioncontrollerfor%3A%29.json'
content_hash: 'sha256:d98300eed61248d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:interactionControllerFor:)

<sub>Instance Method</sub>

Called to allow the delegate to return a [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

## Parameters

- `tabBarController` — The tab bar controller participating in the interactive, animated transition.

- `animationController` — The noninteractive animation controller

## Return Value

The [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) delegate object responsible for managing the user interaction in an animated tab bar transition.

## See Also

### Supporting custom tab bar transition animations

- [- tabBarController:animationControllerForTransitionFromViewController:toViewController:](<tabbarcontroller(__animationcontrollerfortransitionfrom_to_).md>) — Called to allow the delegate to return a [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.
