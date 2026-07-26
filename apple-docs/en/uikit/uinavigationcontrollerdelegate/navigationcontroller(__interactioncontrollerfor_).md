---
title: 'navigationController(_:interactionControllerFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller%28_%3Ainteractioncontrollerfor%3A%29.json'
content_hash: 'sha256:110c8e82e80d07f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md)

# navigationController(_:interactionControllerFor:)

<sub>Instance Method</sub>

Allows the delegate to return an interactive animator object for use during view controller transitions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationController(_ navigationController: UINavigationController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

## Parameters

- `navigationController` — The navigation controller whose navigation stack is changing.

- `animationController` — The noninteractive animator object provided by the delegate’s [- navigationController:animationControllerForOperation:fromViewController:toViewController:](<navigationcontroller(__animationcontrollerfor_from_to_).md>) method.

## Return Value

The animator object responsible for managing the transition animations, or `nil` if you want to use the standard navigation controller transitions. The object you return must conform to the [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md) protocol.

## Discussion

Implement this delegate method when you want to provide a custom, interactive transition between view controllers as they are added to or removed from the navigation stack. The object you return should configure the interactivity aspects of the transition and should work with the object in the `animationController` parameter to start the animations.

## See Also

### Supporting custom transition animations

- [- navigationController:animationControllerForOperation:fromViewController:toViewController:](<navigationcontroller(__animationcontrollerfor_from_to_).md>) — Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [- navigationControllerPreferredInterfaceOrientationForPresentation:](<navigationcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [- navigationControllerSupportedInterfaceOrientations:](<navigationcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.
