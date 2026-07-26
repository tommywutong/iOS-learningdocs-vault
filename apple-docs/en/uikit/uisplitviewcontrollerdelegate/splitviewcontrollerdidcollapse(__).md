---
title: 'splitViewControllerDidCollapse(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse%28_%3A%29.json'
content_hash: 'sha256:0ec25d749f11f2b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerDidCollapse(_:)

<sub>Instance Method</sub>

Tells the delegate that the split view controller interface has collapsed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewControllerDidCollapse(_ svc: UISplitViewController)
```

## Parameters

- `svc` — The split view controller whose interface has collapsed.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method after its interface has collapsed, meaning that [collapsed](../uisplitviewcontroller/iscollapsed.md) is [true](../../swift/true.md). Use this method to perform any customization associated with the collapsed interface.

## See Also

### Collapsing the interface

- [- splitViewController:topColumnForCollapsingToProposedTopColumn:](<splitviewcontroller(__topcolumnforcollapsingtoproposedtopcolumn_).md>) — Asks the delegate to provide the column to display after the split view interface collapses.
- [- splitViewController:willHideColumn:](<splitviewcontroller(__willhide_).md>) — Tells the delegate that the specified column is about to be hidden.
- [- splitViewController:didHideColumn:](<splitviewcontroller(__didhide_).md>) — Tells the delegate that the system completed hiding the specified column.
