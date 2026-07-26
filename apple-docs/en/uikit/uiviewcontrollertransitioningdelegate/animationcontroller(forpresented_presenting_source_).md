---
title: 'animationController(forPresented:presenting:source:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller(forpresented:presenting:source:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller(forpresented:presenting:source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller%28forpresented%3Apresenting%3Asource%3A%29.json'
content_hash: 'sha256:ed67d2636b215bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md)

# animationController(forPresented:presenting:source:)

<sub>Instance Method</sub>

Asks your delegate for the transition animator object to use when presenting a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func animationController(forPresented presented: UIViewController, presenting: UIViewController, source: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

## Parameters

- `presented` — The view controller object that is about to be presented onscreen.

- `presenting` — The view controller that is presenting the view controller in the `presented` parameter. The object in this parameter could be the root view controller of the window, a parent view controller that is marked as defining the current context, or the last view controller that was presented. This view controller may or may not be the same as the one in the `source` parameter.

- `source` — The view controller whose [- presentViewController:animated:completion:](<../uiviewcontroller/present(__animated_completion_).md>) method was called.

## Return Value

The animator object to use when presenting the view controller or `nil` if you do not want to present the view controller using a custom transition. The object you return should be capable of performing a fixed-length animation that is not interactive.

## Discussion

Use this method to create and return an object that implements the methods of the [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) protocol. Your implementation of that protocol must animate the appearance of the `presented` view controller’s view onscreen. Use the `presented`, `presenting`, and `source` parameters to initialize your animator object or perform any tasks necessary to prepare the transition animations. You may return `nil` from this method if you do not want to implement a custom transition animation for the specified set of view controllers.

> [!note] Note
> You must implement this method if you also plan to use an interactive animator object to manage the appearance of the view controller. The animator object returned by this method is responsible for executing the animations. The interactive animator object manages only the timing of the animation, not the animations themselves.

For information on implementing your transition animator object, see [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md).

## See Also

### Getting the transition animator objects

- [- animationControllerForDismissedController:](<animationcontroller(fordismissed_).md>) — Asks your delegate for the transition animator object to use when dismissing a view controller.
