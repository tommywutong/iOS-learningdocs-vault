---
title: 'navigationController(_:animationControllerFor:from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller%28_%3Aanimationcontrollerfor%3Afrom%3Ato%3A%29.json'
content_hash: 'sha256:9ab26dc55b79afe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md)

# navigationController(_:animationControllerFor:from:to:)

<sub>Instance Method</sub>

Allows the delegate to return a noninteractive animator object for use during view controller transitions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationController(_ navigationController: UINavigationController, animationControllerFor operation: UINavigationController.Operation, from fromVC: UIViewController, to toVC: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

## Parameters

- `navigationController` — The navigation controller whose navigation stack is changing.

- `operation` — The type of transition operation that is occurring. For a list of possible values, see the [Operation](../uinavigationcontroller/operation.md) constants.

- `fromVC` — The currently visible view controller.

- `toVC` — The view controller that should be visible at the end of the transition.

## Return Value

The animator object responsible for managing the transition animations, or `nil` if you want to use the standard navigation controller transitions. The object you return must conform to the [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) protocol.

## Discussion

Implement this delegate method when you want to provide a custom animated transition between view controllers as they are added to or removed from the navigation stack. The object you return should be capable of configuring and performing noninteractive animations for the specified view controllers for the specified type of operation over a fixed period of time.

If you want to allow the user to perform interactive transitions, you must _also_ implement the [- navigationController:interactionControllerForAnimationController:](<navigationcontroller(__interactioncontrollerfor_).md>) method.

## See Also

### Supporting custom transition animations

- [- navigationController:interactionControllerForAnimationController:](<navigationcontroller(__interactioncontrollerfor_).md>) — Allows the delegate to return an interactive animator object for use during view controller transitions.
- [- navigationControllerPreferredInterfaceOrientationForPresentation:](<navigationcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [- navigationControllerSupportedInterfaceOrientations:](<navigationcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.
