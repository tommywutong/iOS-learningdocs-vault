---
title: 'splitViewController(_:willHide:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Awillhide%3A%29.json'
content_hash: 'sha256:f95cdc6589e7e3cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:willHide:)

<sub>Instance Method</sub>

Tells the delegate that the specified column is about to be hidden.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, willHide column: UISplitViewController.Column)
```

## Parameters

- `svc` — The split view controller whose column is being hidden.

- `column` — The column to be hidden. See [Column](../uisplitviewcontroller/column.md) for possible values.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the system is preparing to hide one of its columns; for example, when a person rotates the device. The system doesn’t call this method when you hide a column programmatically with [- hideColumn:](<../uisplitviewcontroller/hide(__).md>). Use this method to perform any customization associated with hiding the column. You can use the split view controller’s [transitionCoordinator](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## See Also

### Collapsing the interface

- [- splitViewController:topColumnForCollapsingToProposedTopColumn:](<splitviewcontroller(__topcolumnforcollapsingtoproposedtopcolumn_).md>) — Asks the delegate to provide the column to display after the split view interface collapses.
- [- splitViewController:didHideColumn:](<splitviewcontroller(__didhide_).md>) — Tells the delegate that the system completed hiding the specified column.
- [- splitViewControllerDidCollapse:](<splitviewcontrollerdidcollapse(__).md>) — Tells the delegate that the split view controller interface has collapsed.
