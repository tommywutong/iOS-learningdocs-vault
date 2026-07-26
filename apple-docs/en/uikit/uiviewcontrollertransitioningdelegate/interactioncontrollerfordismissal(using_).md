---
title: 'interactionControllerForDismissal(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerfordismissal(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerfordismissal(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerfordismissal%28using%3A%29.json'
content_hash: 'sha256:2227c5a39814a987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md)

# interactionControllerForDismissal(using:)

<sub>Instance Method</sub>

Asks your delegate for the interactive animator object to use when dismissing a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func interactionControllerForDismissal(using animator: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

## Parameters

- `animator` — The transition animator object returned by your [- animationControllerForDismissedController:](<animationcontroller(fordismissed_).md>) method.

## Return Value

The animator object that implements the code needed specifically to manage interactive transitions or `nil` if you do not want to support interactive transitions.

## Discussion

Use this method to create and return an object that implements the methods of the [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) protocol. The implementation of that protocol should configure the event-handling code required to manage the disappearance of the target view controller. You may return `nil` from this method if you do not want to the animations to be interactive.

> [!important] Important
> If you implement this method, you must also implement the [- animationControllerForDismissedController:](<animationcontroller(fordismissed_).md>) method and use it to return a custom transition animator object. If the [- animationControllerForDismissedController:](<animationcontroller(fordismissed_).md>) method returns `nil`, UIKit does not call this method.

For more information on implementing an interactive animator object, see [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md).

## See Also

### Getting the interactive animator objects

- [- interactionControllerForPresentation:](<interactioncontrollerforpresentation(using_).md>) — Asks your delegate for the interactive animator object to use when presenting a view controller.
