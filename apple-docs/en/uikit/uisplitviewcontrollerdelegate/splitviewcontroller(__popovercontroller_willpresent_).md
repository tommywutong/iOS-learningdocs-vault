---
title: 'splitViewController(_:popoverController:willPresent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Apopovercontroller%3Awillpresent%3A%29.json'
content_hash: 'sha256:dfe62645a2821fa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:popoverController:willPresent:)

<sub>Instance Method</sub>

Tells the delegate that the hidden view controller is about to be displayed in a popover.

> [!warning] Deprecated
> Orientation-related delegate methods are no longer supported.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, popoverController pc: UIPopoverController, willPresent aViewController: UIViewController)
```

## Parameters

- `svc` — The split view controller that owns the hidden view controller.

- `pc` — The popover controller that is about to display the view controller.

- `aViewController` — The view controller to be displayed in the popover.

## Discussion

The toolbar button you add to your user interface facilitates the display of the hidden view controller in response to user taps. When the user taps that button, the split view controller calls this method. You can use this method to perform any additional steps prior to displaying the currently hidden view controller.

## See Also

### Deprecated methods

- [- splitViewController:shouldHideViewController:inOrientation:](<splitviewcontroller(__shouldhide_in_).md>) — Asks the delegate whether the first view controller should be hidden for the specified orientation. _(deprecated)_
- [- splitViewController:willHideViewController:withBarButtonItem:forPopoverController:](<splitviewcontroller(__willhide_with_for_).md>) — Tells the delegate that the specified view controller is about to be hidden. _(deprecated)_
- [- splitViewController:willShowViewController:invalidatingBarButtonItem:](<splitviewcontroller(__willshow_invalidating_).md>) — Tells the delegate that the specified view controller is about to be shown again. _(deprecated)_
