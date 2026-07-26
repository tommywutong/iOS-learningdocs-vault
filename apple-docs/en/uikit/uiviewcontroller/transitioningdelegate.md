---
title: transitioningDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transitioningdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transitioningdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transitioningdelegate.json'
content_hash: 'sha256:80a17e209b6da7ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# transitioningDelegate

<sub>Instance Property</sub>

The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var transitioningDelegate: (any UIViewControllerTransitioningDelegate)? { get set }
```

## Discussion

When the view controller’s [modalPresentationStyle](modalpresentationstyle.md) property is [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md), UIKit uses the object in this property to facilitate transitions and presentations for the view controller. The transitioning delegate object is a custom object that you provide and that conforms to the [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md) protocol. Its job is to vend the animator objects used to animate this view controller’s view onscreen and an optional presentation controller to provide any additional chrome and animations.

## See Also

### Adding a custom transition or presentation

- [transitionCoordinator](transitioncoordinator.md) — Returns the active transition coordinator object.
- [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) — Returns the view controller that responds to the action.
- [presentationController](presentationcontroller.md) — The presentation controller that’s managing the current view controller.
- [popoverPresentationController](popoverpresentationcontroller.md) — The nearest popover presentation controller that is managing the current view controller.
- [sheetPresentationController](sheetpresentationcontroller.md) — The sheet presentation controller for the view controller.
- [activePresentationController](activepresentationcontroller.md) — The presentation controller that’s managing the view controller.
- [restoresFocusAfterTransition](restoresfocusaftertransition.md) — A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md) — Discover how to create a layered and customized sheet experience in UIKit.
