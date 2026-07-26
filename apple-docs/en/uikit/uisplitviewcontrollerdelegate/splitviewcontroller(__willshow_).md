---
title: 'splitViewController(_:willShow:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Awillshow%3A%29.json'
content_hash: 'sha256:737739091aaaf29c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:willShow:)

<sub>Instance Method</sub>

Tells the delegate that the specified column is about to be shown.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, willShow column: UISplitViewController.Column)
```

## Parameters

- `svc` — The split view controller whose column is being shown.

- `column` — The column to be shown. See [Column](../uisplitviewcontroller/column.md) for possible values.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system is preparing to show one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you display the column programmatically with [- showColumn:](<../uisplitviewcontroller/show(__).md>). Use this method to perform any customization associated with showing the column. You can use the split view controller’s [transitionCoordinator](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## See Also

### Expanding the interface

- [- splitViewController:displayModeForExpandingToProposedDisplayMode:](<splitviewcontroller(__displaymodeforexpandingtoproposeddisplaymode_).md>) — Asks the delegate to provide the display mode to use after the split view interface expands.
- [- splitViewController:didShowColumn:](<splitviewcontroller(__didshow_).md>) — Tells the delegate that the system completed showing the specified column.
- [- splitViewControllerDidExpand:](<splitviewcontrollerdidexpand(__).md>) — Tells the delegate that the split view controller interface has expanded.
