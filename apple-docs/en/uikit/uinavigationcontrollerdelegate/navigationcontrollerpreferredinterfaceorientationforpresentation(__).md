---
title: 'navigationControllerPreferredInterfaceOrientationForPresentation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation%28_%3A%29.json'
content_hash: 'sha256:8ceba97c2daf5812'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md)

# navigationControllerPreferredInterfaceOrientationForPresentation(_:)

<sub>Instance Method</sub>

Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func navigationControllerPreferredInterfaceOrientationForPresentation(_ navigationController: UINavigationController) -> UIInterfaceOrientation
```

## Parameters

- `navigationController` — The navigation controller

## Return Value

The preferred orientation for presenting the navigation controller.

## See Also

### Supporting custom transition animations

- [- navigationController:animationControllerForOperation:fromViewController:toViewController:](<navigationcontroller(__animationcontrollerfor_from_to_).md>) — Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [- navigationController:interactionControllerForAnimationController:](<navigationcontroller(__interactioncontrollerfor_).md>) — Allows the delegate to return an interactive animator object for use during view controller transitions.
- [- navigationControllerSupportedInterfaceOrientations:](<navigationcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.
