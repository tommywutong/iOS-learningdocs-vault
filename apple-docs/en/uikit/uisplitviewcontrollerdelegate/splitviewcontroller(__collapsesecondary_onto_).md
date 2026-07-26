---
title: 'splitViewController(_:collapseSecondary:onto:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:collapsesecondary:onto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:collapsesecondary:onto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Acollapsesecondary%3Aonto%3A%29.json'
content_hash: 'sha256:a5aeab7cb1389d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:collapseSecondary:onto:)

<sub>Instance Method</sub>

Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ splitViewController: UISplitViewController, collapseSecondary secondaryViewController: UIViewController, onto primaryViewController: UIViewController) -> Bool
```

## Parameters

- `splitViewController` — The split view controller whose interface is collapsing.

- `secondaryViewController` — The secondary view controller of the split view interface.

- `primaryViewController` — The primary view controller of the split view interface. If you implement the [- primaryViewControllerForCollapsingSplitViewController:](<primaryviewcontroller(forcollapsing_).md>) method in your delegate, this object is the one that method returns.

## Return Value

[false](../../swift/false.md) to let the split view controller try to incorporate the secondary view controller’s content into the collapsed interface, or [true](../../swift/true.md) to indicate that you do not want the split view controller to do anything with the secondary view controller.

## Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

This method is your opportunity to perform any necessary tasks related to the transition to a collapsed interface. After this method returns, the split view controller removes the secondary view controller from its [viewControllers](../uisplitviewcontroller/viewcontrollers.md) array, leaving the primary view controller as its only child. In your implementation of this method, you might prepare the primary view controller for display in a compact environment, or you might attempt to incorporate the secondary view controller’s content into the newly collapsed interface.

Returning [false](../../swift/false.md) tells the split view controller to use its default behavior to try to incorporate the secondary view controller into the collapsed interface. When you return [false](../../swift/false.md), the split view controller calls the [- collapseSecondaryViewController:forSplitViewController:](<../uiviewcontroller/collapsesecondaryviewcontroller(__for_).md>) method of the primary view controller, giving it a chance to do something with the secondary view controller’s content. Most view controllers do nothing by default, but the [UINavigationController](../uinavigationcontroller.md) class responds by pushing the secondary view controller onto its navigation stack.

Returning [true](../../swift/true.md) from this method tells the split view controller not to apply any default behavior. You might return [true](../../swift/true.md) in cases where you do not want the secondary view controller’s content incorporated into the resulting interface.

## See Also

### Collapsing and expanding classic split views

- [- primaryViewControllerForCollapsingSplitViewController:](<primaryviewcontroller(forcollapsing_).md>) — Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [- primaryViewControllerForExpandingSplitViewController:](<primaryviewcontroller(forexpanding_).md>) — Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.
- [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<splitviewcontroller(__separatesecondaryfrom_).md>) — Asks the delegate to provide the new secondary view controller for the split view interface.
