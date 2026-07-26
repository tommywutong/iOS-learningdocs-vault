---
title: restoresFocusAfterTransition
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/restoresfocusaftertransition
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/restoresfocusaftertransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/restoresfocusaftertransition.json'
content_hash: 'sha256:715d31b096570b3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# restoresFocusAfterTransition

<sub>Instance Property</sub>

A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var restoresFocusAfterTransition: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the item that was last focused automatically becomes focused when its view controller becomes visible and focusable. For example, if an item in the view controller is focused and a second view controller is presented, the original item becomes focused again when the second view controller is dismissed. The default value of this property is [true](../../swift/true.md).

## See Also

### Adding a custom transition or presentation

- [transitioningDelegate](transitioningdelegate.md) — The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [transitionCoordinator](transitioncoordinator.md) — Returns the active transition coordinator object.
- [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) — Returns the view controller that responds to the action.
- [presentationController](presentationcontroller.md) — The presentation controller that’s managing the current view controller.
- [popoverPresentationController](popoverpresentationcontroller.md) — The nearest popover presentation controller that is managing the current view controller.
- [sheetPresentationController](sheetpresentationcontroller.md) — The sheet presentation controller for the view controller.
- [activePresentationController](activepresentationcontroller.md) — The presentation controller that’s managing the view controller.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md) — Discover how to create a layered and customized sheet experience in UIKit.
