---
title: 'splitViewController(_:shouldHide:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（8.0 起废弃）, iPadOS 5.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Ashouldhide%3Ain%3A%29.json'
content_hash: 'sha256:d881d45a25ecea10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:shouldHide:in:)

<sub>Instance Method</sub>

Asks the delegate whether the first view controller should be hidden for the specified orientation.

> [!warning] Deprecated
> Orientation-related delegate methods are no longer supported.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, shouldHide vc: UIViewController, in orientation: UIInterfaceOrientation) -> Bool
```

## Parameters

- `svc` — The split view controller that owns the first view controller.

- `vc` — The first view controller in the array of view controllers.

- `orientation` — The orientation being considered.

## Return Value

[true](../../swift/true.md) if the view controller should be hidden in the specified orientation or [false](../../swift/false.md) if it should be visible. If you do not implement this method, a value of [true](../../swift/true.md) is assumed for portrait orientations and [false](../../swift/false.md) is assumed for landscape orientations.

## Discussion

The split view controller calls this method only for the first child view controller in its array. The second view controller always remains visible regardless of the orientation.

Prior to iOS 5.0, the first view controller was always hidden in portrait orientations and always shown in landscape orientations. If you do not implement this method in your delegate object, that default behavior remains in effect.

## See Also

### Deprecated methods

- [- splitViewController:willHideViewController:withBarButtonItem:forPopoverController:](<splitviewcontroller(__willhide_with_for_).md>) — Tells the delegate that the specified view controller is about to be hidden. _(deprecated)_
- [- splitViewController:willShowViewController:invalidatingBarButtonItem:](<splitviewcontroller(__willshow_invalidating_).md>) — Tells the delegate that the specified view controller is about to be shown again. _(deprecated)_
- [- splitViewController:popoverController:willPresentViewController:](<splitviewcontroller(__popovercontroller_willpresent_).md>) — Tells the delegate that the hidden view controller is about to be displayed in a popover. _(deprecated)_
