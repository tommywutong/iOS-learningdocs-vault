---
title: 'splitViewController(_:didShow:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Adidshow%3A%29.json'
content_hash: 'sha256:1202930ede58711b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:didShow:)

<sub>Instance Method</sub>

Tells the delegate that the system completed showing the specified column.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, didShow column: UISplitViewController.Column)
```

## Parameters

- `svc` — The split view controller whose column the system completed showing.

- `column` — The column the system completed showing. See [Column](../uisplitviewcontroller/column.md) for possible values.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system completes showing one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you display the column programmatically with [- showColumn:](<../uisplitviewcontroller/show(__).md>). Use this method to perform any updates after  showing the column. You can use the split view controller’s [transitionCoordinator](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## See Also

### Expanding the interface

- [- splitViewController:displayModeForExpandingToProposedDisplayMode:](<splitviewcontroller(__displaymodeforexpandingtoproposeddisplaymode_).md>) — Asks the delegate to provide the display mode to use after the split view interface expands.
- [- splitViewController:willShowColumn:](<splitviewcontroller(__willshow_).md>) — Tells the delegate that the specified column is about to be shown.
- [- splitViewControllerDidExpand:](<splitviewcontrollerdidexpand(__).md>) — Tells the delegate that the split view controller interface has expanded.
