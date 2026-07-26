---
title: 'splitViewController(_:displayModeForExpandingToProposedDisplayMode:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Adisplaymodeforexpandingtoproposeddisplaymode%3A%29.json'
content_hash: 'sha256:7e344d9e91b74480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:displayModeForExpandingToProposedDisplayMode:)

<sub>Instance Method</sub>

Asks the delegate to provide the display mode to use after the split view interface expands.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, displayModeForExpandingToProposedDisplayMode proposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode
```

## Parameters

- `svc` — The split view controller whose interface is expanding.

- `proposedDisplayMode` — The proposed display mode to expand the interface to.

## Return Value

The display mode to expand the interface to. This value may be the same as `proposedDisplayMode`, or you may return a different value.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When the split view controller transitions from a horizontally compact to a horizontally regular size class, it calls this method and asks you for the display mode to use when that transition is complete. Use this method to customize the display mode you’re expanding to. For example, you might use this opportunity to adjust column widths before returning the display mode to use.

## See Also

### Expanding the interface

- [- splitViewController:willShowColumn:](<splitviewcontroller(__willshow_).md>) — Tells the delegate that the specified column is about to be shown.
- [- splitViewController:didShowColumn:](<splitviewcontroller(__didshow_).md>) — Tells the delegate that the system completed showing the specified column.
- [- splitViewControllerDidExpand:](<splitviewcontrollerdidexpand(__).md>) — Tells the delegate that the split view controller interface has expanded.
