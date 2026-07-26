---
title: 'primaryViewController(forExpanding:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/primaryviewcontroller%28forexpanding%3A%29.json'
content_hash: 'sha256:cb27896d8c8fef08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# primaryViewController(forExpanding:)

<sub>Instance Method</sub>

Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func primaryViewController(forExpanding splitViewController: UISplitViewController) -> UIViewController?
```

## Parameters

- `splitViewController` — The split view controller whose interface is expanding.

## Return Value

The view controller to use as the primary view controller, or `nil` to specify the current primary view controller.

## Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When the split view controller transitions from a horizontally compact to a horizontally regular size class, it calls this method and asks you for the view controller to display in the primary position when that transition is complete. The view controller you return becomes the primary view controller of the split view interface. If you do not implement this method, or if your implementation returns `nil`, the split view controller chooses its current primary view controller as the one to use.

If you specified a specific view controller in your [- primaryViewControllerForCollapsingSplitViewController:](<primaryviewcontroller(forcollapsing_).md>) method, use this method to restore the original primary view controller for your split view interface. You can also implement the [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<splitviewcontroller(__separatesecondaryfrom_).md>) method to disentangle your view controllers from one another as needed.

## See Also

### Collapsing and expanding classic split views

- [- primaryViewControllerForCollapsingSplitViewController:](<primaryviewcontroller(forcollapsing_).md>) — Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [- splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:](<splitviewcontroller(__collapsesecondary_onto_).md>) — Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.
- [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<splitviewcontroller(__separatesecondaryfrom_).md>) — Asks the delegate to provide the new secondary view controller for the split view interface.
