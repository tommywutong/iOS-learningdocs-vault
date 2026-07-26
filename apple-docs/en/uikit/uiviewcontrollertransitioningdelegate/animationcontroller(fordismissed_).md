---
title: 'animationController(forDismissed:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioningdelegate/animationcontroller%28fordismissed%3A%29.json'
content_hash: 'sha256:8d6680ee893dc9d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md)

# animationController(forDismissed:)

<sub>Instance Method</sub>

Asks your delegate for the transition animator object to use when dismissing a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func animationController(forDismissed dismissed: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

## Parameters

- `dismissed` — The view controller object that is about to be dismissed.

## Return Value

The animator object to use when dismissing the view controller or `nil` if you do not want to dismiss the view controller using a custom transition. The object you return should be capable of performing a fixed-length animation that is not interactive.

## Discussion

Use this method to create and return an object that implements the methods of the [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) protocol. Your implementation of that protocol must animate the disappearance of the `dismissed` view controller’s view from the screen. Use the `dismissed` parameter to initialize your object or perform any tasks necessary to prepare the transition animations. You may return `nil` from this method if you do not want to implement a custom transition animation when dismissing view controllers.

> [!note] Note
> You must implement this method if you also plan to use an interactive animator object to manage the disappearance of the view controller. The animator object returned by this method is responsible for executing the animations. The interactive animator object manages only the timing of the animation, not the animations themselves.

For more information on implementing a transition animator object, see [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md).

## See Also

### Getting the transition animator objects

- [- animationControllerForPresentedController:presentingController:sourceController:](<animationcontroller(forpresented_presenting_source_).md>) — Asks your delegate for the transition animator object to use when presenting a view controller.
