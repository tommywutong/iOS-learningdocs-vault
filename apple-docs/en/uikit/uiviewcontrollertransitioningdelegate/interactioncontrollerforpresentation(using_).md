---
title: 'interactionControllerForPresentation(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerforpresentation(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerforpresentation(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerforpresentation%28using%3A%29.json'
content_hash: 'sha256:d813249324fb9cc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md)

# interactionControllerForPresentation(using:)

<sub>Instance Method</sub>

Asks your delegate for the interactive animator object to use when presenting a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func interactionControllerForPresentation(using animator: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

## Parameters

- `animator` — The transition animator object returned by your [- animationControllerForPresentedController:presentingController:sourceController:](<animationcontroller(forpresented_presenting_source_).md>) method.

## Return Value

The interactive animator object to use to manage the timing of the transition or `nil` if you do not want to support interactive transitions.

## Discussion

Use this method to create and return an object that implements the methods of the [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) protocol. The implementation of that protocol should configure the event-handling code required to manage the appearance of the target view controller. You may return `nil` from this method if you do not want to the animations to be interactive.

> [!important] Important
> If you implement this method, you must also implement the [- animationControllerForPresentedController:presentingController:sourceController:](<animationcontroller(forpresented_presenting_source_).md>) method and use it to return a custom transition animator object. If the [- animationControllerForPresentedController:presentingController:sourceController:](<animationcontroller(forpresented_presenting_source_).md>) method returns `nil`, UIKit does not call this method.

For more information on implementing an interactive animator object, see [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md).

## See Also

### Getting the interactive animator objects

- [- interactionControllerForDismissal:](<interactioncontrollerfordismissal(using_).md>) — Asks your delegate for the interactive animator object to use when dismissing a view controller.
