---
title: activePresentationController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/activepresentationcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/activepresentationcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/activepresentationcontroller.json'
content_hash: 'sha256:2bdf70854c6a2671'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# activePresentationController

<sub>Instance Property</sub>

The presentation controller that’s managing the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var activePresentationController: UIPresentationController? { get }
```

## Discussion

If the original presentation controller hasn’t adapted, the value of this property is [presentationController](presentationcontroller.md). If the original presentation controller has adapted to a different presentation controller, the value of this property is the adaptive presentation controller.

If the view controller hasn’t presented yet, this property returns `nil`.

## See Also

### Adding a custom transition or presentation

- [transitioningDelegate](transitioningdelegate.md) — The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [transitionCoordinator](transitioncoordinator.md) — Returns the active transition coordinator object.
- [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) — Returns the view controller that responds to the action.
- [presentationController](presentationcontroller.md) — The presentation controller that’s managing the current view controller.
- [popoverPresentationController](popoverpresentationcontroller.md) — The nearest popover presentation controller that is managing the current view controller.
- [sheetPresentationController](sheetpresentationcontroller.md) — The sheet presentation controller for the view controller.
- [restoresFocusAfterTransition](restoresfocusaftertransition.md) — A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md) — Discover how to create a layered and customized sheet experience in UIKit.
