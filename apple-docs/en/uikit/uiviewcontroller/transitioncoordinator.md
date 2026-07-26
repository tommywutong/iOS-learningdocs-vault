---
title: transitionCoordinator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transitioncoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transitioncoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transitioncoordinator.json'
content_hash: 'sha256:7075571df7b5bf4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# transitionCoordinator

<sub>Instance Property</sub>

Returns the active transition coordinator object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transitionCoordinator: (any UIViewControllerTransitionCoordinator)? { get }
```

## Return Value

The transition coordinator object associated with a currently active transition or `nil` if no transition is in progress.

## Discussion

When a presentation or dismissal is in progress, this method returns the transition coordinator object associated with that transition. If there is no in-progress transition associated with the current view controller, UIKit checks the view controller’s ancestors for a transition coordinator object and returns that object if it exists. You can use this object to create additional animations and synchronize them with the transition animations.

Container view controllers can override this method but in most cases should not need to. If you do override this method, first call `super` to see if there is an appropriate transition coordinator to return, and, if there is, return it.

For more information about the role of transition coordinators, see [UIViewControllerTransitionCoordinator](../uiviewcontrollertransitioncoordinator.md).

## See Also

### Adding a custom transition or presentation

- [transitioningDelegate](transitioningdelegate.md) — The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) — Returns the view controller that responds to the action.
- [presentationController](presentationcontroller.md) — The presentation controller that’s managing the current view controller.
- [popoverPresentationController](popoverpresentationcontroller.md) — The nearest popover presentation controller that is managing the current view controller.
- [sheetPresentationController](sheetpresentationcontroller.md) — The sheet presentation controller for the view controller.
- [activePresentationController](activepresentationcontroller.md) — The presentation controller that’s managing the view controller.
- [restoresFocusAfterTransition](restoresfocusaftertransition.md) — A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md) — Discover how to create a layered and customized sheet experience in UIKit.
