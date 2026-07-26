---
title: sheetPresentationController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/sheetpresentationcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/sheetpresentationcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/sheetpresentationcontroller.json'
content_hash: 'sha256:476529389f159696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# sheetPresentationController

<sub>Instance Property</sub>

The sheet presentation controller for the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sheetPresentationController: UISheetPresentationController? { get }
```

## Discussion

If [modalPresentationStyle](modalpresentationstyle.md) is [UIModalPresentationPageSheet](../uimodalpresentationstyle/pagesheet.md) or [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md), this property contains a sheet presentation controller instance. Access this instance to customize or adjust the sheet before or after it presents.

If [modalPresentationStyle](modalpresentationstyle.md) has a value other than [UIModalPresentationPageSheet](../uimodalpresentationstyle/pagesheet.md) or [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md), the value of this property is `nil`.

## See Also

### Adding a custom transition or presentation

- [transitioningDelegate](transitioningdelegate.md) — The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [transitionCoordinator](transitioncoordinator.md) — Returns the active transition coordinator object.
- [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) — Returns the view controller that responds to the action.
- [presentationController](presentationcontroller.md) — The presentation controller that’s managing the current view controller.
- [popoverPresentationController](popoverpresentationcontroller.md) — The nearest popover presentation controller that is managing the current view controller.
- [activePresentationController](activepresentationcontroller.md) — The presentation controller that’s managing the view controller.
- [restoresFocusAfterTransition](restoresfocusaftertransition.md) — A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md) — Discover how to create a layered and customized sheet experience in UIKit.
