---
title: 'splitViewController(_:topColumnForCollapsingToProposedTopColumn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Atopcolumnforcollapsingtoproposedtopcolumn%3A%29.json'
content_hash: 'sha256:980d248d7a479f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:topColumnForCollapsingToProposedTopColumn:)

<sub>Instance Method</sub>

Asks the delegate to provide the column to display after the split view interface collapses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, topColumnForCollapsingToProposedTopColumn proposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column
```

## Parameters

- `svc` — The split view controller whose interface is collapsing.

- `proposedTopColumn` — The proposed column to display in the collapsed interface.

## Return Value

The column corresponding to the view controller to display in the collapsed interface. This value may be the same as `proposedTopColumn`, or you may return a different value.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When the split view controller transitions from a horizontally regular to a horizontally compact size class, it calls this method and asks you for the column to display when that transition is complete. Use this method to customize the view controller you’re collapsing to. For example, you might use this opportunity to configure the interface in the view controller associated with the [UISplitViewControllerColumnCompact](../uisplitviewcontroller/column/compact.md) column before returning that column.

## See Also

### Collapsing the interface

- [- splitViewController:willHideColumn:](<splitviewcontroller(__willhide_).md>) — Tells the delegate that the specified column is about to be hidden.
- [- splitViewController:didHideColumn:](<splitviewcontroller(__didhide_).md>) — Tells the delegate that the system completed hiding the specified column.
- [- splitViewControllerDidCollapse:](<splitviewcontrollerdidcollapse(__).md>) — Tells the delegate that the split view controller interface has collapsed.
