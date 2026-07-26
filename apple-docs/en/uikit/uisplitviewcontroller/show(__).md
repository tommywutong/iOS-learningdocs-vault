---
title: 'show(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/show(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/show(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/show%28_%3A%29.json'
content_hash: 'sha256:75c96bca52a3b2f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# show(_:)

<sub>Instance Method</sub>

Presents the view controller in the specified column of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func show(_ column: UISplitViewController.Column)
```

## Parameters

- `column` — The corresponding column of the split view interface to show. See [Column](column.md) for values.

## Discussion

When you call this method, the split view interface transitions to the closest display mode available for the current split behavior where the specified column is fully visible.

The split view controller chooses the appropriate transition to display the view controller in the specified column. For example, calling this method with [UISplitViewControllerColumnSecondary](column/secondary.md) when the split behavior is [UISplitViewControllerSplitBehaviorDisplace](splitbehavior-swift.enum/displace.md) changes the display mode from [UISplitViewControllerDisplayModeTwoDisplaceSecondary](displaymode-swift.enum/twodisplacesecondary.md) to [UISplitViewControllerDisplayModeOneBesideSecondary](displaymode-swift.enum/onebesidesecondary.md), which hides the primary column to show the unobstructed secondary column.

After you call this method, you can use the split view controller’s [transitionCoordinator](../uiviewcontroller/transitioncoordinator.md) to coordinate any of your animations alongside the transition animation.

## See Also

### Displaying the child view controllers

- [- hideColumn:](<hide(__).md>) — Dismisses the view controller in the specified column of the split view interface.
- [- isShowingColumn:](<isshowing(__).md>) — A Boolean value that indicates whether the split view interface is showing the specified column.
- [- showViewController:sender:](<show(__sender_).md>) — Presents the specified view controller as the primary view controller in the split view interface.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents the specified view controller as the secondary view controller of the split view interface.
