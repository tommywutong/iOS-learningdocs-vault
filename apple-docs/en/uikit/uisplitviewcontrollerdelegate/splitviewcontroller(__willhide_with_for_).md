---
title: 'splitViewController(_:willHide:with:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Awillhide%3Awith%3Afor%3A%29.json'
content_hash: 'sha256:2e88be24be8ec0bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:willHide:with:for:)

<sub>Instance Method</sub>

Tells the delegate that the specified view controller is about to be hidden.

> [!warning] Deprecated
> Implement the [- splitViewController:willChangeToDisplayMode:](<splitviewcontroller(__willchangeto_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, willHide aViewController: UIViewController, with barButtonItem: UIBarButtonItem, for pc: UIPopoverController)
```

## Parameters

- `svc` — The split view controller that owns the specified view controller.

- `aViewController` — The view controller being hidden.

- `barButtonItem` — A button you can add to your toolbar.

- `pc` — The popover controller that uses taps in `barButtonItem` to display the specified view controller.

## Discussion

When the split view controller rotates from a landscape to portrait orientation, it typically hides one of its view controllers. When that happens, it calls this method to coordinate the addition of a button to the toolbar (or navigation bar) of the remaining custom view controller. If you want the soon-to-be hidden view controller to be displayed in a popover, you must implement this method and use it to add the specified button to your interface.

## See Also

### Deprecated methods

- [- splitViewController:shouldHideViewController:inOrientation:](<splitviewcontroller(__shouldhide_in_).md>) — Asks the delegate whether the first view controller should be hidden for the specified orientation. _(deprecated)_
- [- splitViewController:willShowViewController:invalidatingBarButtonItem:](<splitviewcontroller(__willshow_invalidating_).md>) — Tells the delegate that the specified view controller is about to be shown again. _(deprecated)_
- [- splitViewController:popoverController:willPresentViewController:](<splitviewcontroller(__popovercontroller_willpresent_).md>) — Tells the delegate that the hidden view controller is about to be displayed in a popover. _(deprecated)_
