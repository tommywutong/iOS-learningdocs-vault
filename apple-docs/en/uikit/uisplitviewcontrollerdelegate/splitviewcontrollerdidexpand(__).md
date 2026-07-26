---
title: 'splitViewControllerDidExpand(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand%28_%3A%29.json'
content_hash: 'sha256:d7295b64e2d2ce20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerDidExpand(_:)

<sub>Instance Method</sub>

Tells the delegate that the split view controller interface has expanded.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewControllerDidExpand(_ svc: UISplitViewController)
```

## Parameters

- `svc` — The split view controller whose interface has expanded.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method after its interface has expanded, meaning that [collapsed](../uisplitviewcontroller/iscollapsed.md) is [false](../../swift/false.md). Use this method to perform any customization associated with the expanded interface.

## See Also

### Expanding the interface

- [- splitViewController:displayModeForExpandingToProposedDisplayMode:](<splitviewcontroller(__displaymodeforexpandingtoproposeddisplaymode_).md>) — Asks the delegate to provide the display mode to use after the split view interface expands.
- [- splitViewController:willShowColumn:](<splitviewcontroller(__willshow_).md>) — Tells the delegate that the specified column is about to be shown.
- [- splitViewController:didShowColumn:](<splitviewcontroller(__didshow_).md>) — Tells the delegate that the system completed showing the specified column.
