---
title: 'splitViewController(_:willShow:invalidating:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Awillshow%3Ainvalidating%3A%29.json'
content_hash: 'sha256:db32cec21e3c479e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:willShow:invalidating:)

<sub>Instance Method</sub>

Tells the delegate that the specified view controller is about to be shown again.

> [!warning] Deprecated
> Implement the [- splitViewController:willChangeToDisplayMode:](<splitviewcontroller(__willchangeto_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, willShow aViewController: UIViewController, invalidating barButtonItem: UIBarButtonItem)
```

## Parameters

- `svc` — The split view controller that owns the specified view controller.

- `aViewController` — The view controller being hidden.

- `barButtonItem` — The button used to display the view controller while it was hidden.

## Discussion

When the view controller rotates from a portrait to landscape orientation, it shows its hidden view controller once more. If you added the specified button to your toolbar to facilitate the display of the hidden view controller in a popover, you must implement this method and use it to remove that button.

## See Also

### Deprecated methods

- [- splitViewController:shouldHideViewController:inOrientation:](<splitviewcontroller(__shouldhide_in_).md>) — Asks the delegate whether the first view controller should be hidden for the specified orientation. _(deprecated)_
- [- splitViewController:willHideViewController:withBarButtonItem:forPopoverController:](<splitviewcontroller(__willhide_with_for_).md>) — Tells the delegate that the specified view controller is about to be hidden. _(deprecated)_
- [- splitViewController:popoverController:willPresentViewController:](<splitviewcontroller(__popovercontroller_willpresent_).md>) — Tells the delegate that the hidden view controller is about to be displayed in a popover. _(deprecated)_
