---
title: UISplitViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate.json'
content_hash: 'sha256:80ae911f94665a7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISplitViewControllerDelegate

<sub>Protocol</sub>

The methods adopted by the object you use to manage changes to a split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISplitViewControllerDelegate
```

## Overview

Use the methods of this protocol to respond to changes in the current display mode and to the current interface orientation. When the split view interface collapses and expands, or when a new view controller is added to the interface, you can also use these methods to configure the child view controllers.

The methods of this protocol are all optional. If you don’t implement any of the methods, the split view controller provides default behavior to handle the collapsing and expanding transitions.

For more information, see [UISplitViewController](uisplitviewcontroller.md).

### Column-style split views

In a column-style split view interface, you use these delegate methods to customize interface transition behavior:

- [- splitViewController:topColumnForCollapsingToProposedTopColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__topcolumnforcollapsingtoproposedtopcolumn_).md>)
- [- splitViewController:willHideColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willhide_).md>)
- [- splitViewController:didHideColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__didhide_).md>)
- [- splitViewControllerDidCollapse:](<uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(__).md>)
- [- splitViewController:displayModeForExpandingToProposedDisplayMode:](<uisplitviewcontrollerdelegate/splitviewcontroller(__displaymodeforexpandingtoproposeddisplaymode_).md>)
- [- splitViewController:willShowColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willshow_).md>)
- [- splitViewController:didShowColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__didshow_).md>)
- [- splitViewControllerDidExpand:](<uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(__).md>)

### Classic split views

In a classic split view interface, you use these delegate methods to customize interface transition behavior:

- [- primaryViewControllerForCollapsingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing_).md>)
- [- splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__collapsesecondary_onto_).md>)
- [- primaryViewControllerForExpandingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding_).md>)
- [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__separatesecondaryfrom_).md>)
- [- splitViewController:showViewController:sender:](<uisplitviewcontrollerdelegate/splitviewcontroller(__show_sender_).md>)
- [- splitViewController:showDetailViewController:sender:](<uisplitviewcontrollerdelegate/splitviewcontroller(__showdetail_sender_).md>)

At the end of a collapse transition, the split view controller typically shows only the content from its primary view controller. You can change this behavior by implementing the [- primaryViewControllerForCollapsingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing_).md>) method in your split view controller delegate. You might use that method to specify the secondary view controller or an entirely different view controller—perhaps one better suited for display in a horizontally compact environment.

If you want to perform any additional adjustments of the view controllers and view hierarchy, you can also implement the [- splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__collapsesecondary_onto_).md>) method in your delegate.

The expansion process reverses the collapsing process by asking the delegate to designate which view controller becomes the primary view controller and to give the delegate a chance to perform the transition itself. If you implement the delegate methods for collapsing your split view interface, you should also implement the [- primaryViewControllerForExpandingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding_).md>) and [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__separatesecondaryfrom_).md>) methods for expanding that interface.

## Topics

### Specifying the interface orientations

- [- splitViewControllerPreferredInterfaceOrientationForPresentation:](<uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Asks the delegate for the orientation to use when presenting the split view controller.
- [- splitViewControllerSupportedInterfaceOrientations:](<uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(__).md>) — Asks the delegate to specify the interface orientations that the split view controller supports.

### Responding to display mode changes

- [- splitViewController:willChangeToDisplayMode:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willchangeto_).md>) — Tells the delegate that the display mode for the split view controller is about to change.
- [- targetDisplayModeForActionInSplitViewController:](<uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in_).md>) — Asks the delegate to provide the display mode to apply when a split view controller action occurs.

### Collapsing the interface

- [- splitViewController:topColumnForCollapsingToProposedTopColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__topcolumnforcollapsingtoproposedtopcolumn_).md>) — Asks the delegate to provide the column to display after the split view interface collapses.
- [- splitViewController:willHideColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willhide_).md>) — Tells the delegate that the specified column is about to be hidden.
- [- splitViewController:didHideColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__didhide_).md>) — Tells the delegate that the system completed hiding the specified column.
- [- splitViewControllerDidCollapse:](<uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(__).md>) — Tells the delegate that the split view controller interface has collapsed.

### Expanding the interface

- [- splitViewController:displayModeForExpandingToProposedDisplayMode:](<uisplitviewcontrollerdelegate/splitviewcontroller(__displaymodeforexpandingtoproposeddisplaymode_).md>) — Asks the delegate to provide the display mode to use after the split view interface expands.
- [- splitViewController:willShowColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willshow_).md>) — Tells the delegate that the specified column is about to be shown.
- [- splitViewController:didShowColumn:](<uisplitviewcontrollerdelegate/splitviewcontroller(__didshow_).md>) — Tells the delegate that the system completed showing the specified column.
- [- splitViewControllerDidExpand:](<uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(__).md>) — Tells the delegate that the split view controller interface has expanded.

### Handling the presentation gesture

- [- splitViewControllerInteractivePresentationGestureWillBegin:](<uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(__).md>) — Tells the delegate that the interactive presentation gesture is about to begin.
- [- splitViewControllerInteractivePresentationGestureDidEnd:](<uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend(__).md>) — Tells the delegate when the interactive presentation gesture ends.

### Collapsing and expanding classic split views

- [- primaryViewControllerForCollapsingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing_).md>) — Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [- splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__collapsesecondary_onto_).md>) — Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.
- [- primaryViewControllerForExpandingSplitViewController:](<uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding_).md>) — Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.
- [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__separatesecondaryfrom_).md>) — Asks the delegate to provide the new secondary view controller for the split view interface.

### Overriding the presentation behavior

- [- splitViewController:showViewController:sender:](<uisplitviewcontrollerdelegate/splitviewcontroller(__show_sender_).md>) — Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.
- [- splitViewController:showDetailViewController:sender:](<uisplitviewcontrollerdelegate/splitviewcontroller(__showdetail_sender_).md>) — Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.

### Deprecated methods

- [- splitViewController:shouldHideViewController:inOrientation:](<uisplitviewcontrollerdelegate/splitviewcontroller(__shouldhide_in_).md>) — Asks the delegate whether the first view controller should be hidden for the specified orientation. _(deprecated)_
- [- splitViewController:willHideViewController:withBarButtonItem:forPopoverController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willhide_with_for_).md>) — Tells the delegate that the specified view controller is about to be hidden. _(deprecated)_
- [- splitViewController:willShowViewController:invalidatingBarButtonItem:](<uisplitviewcontrollerdelegate/splitviewcontroller(__willshow_invalidating_).md>) — Tells the delegate that the specified view controller is about to be shown again. _(deprecated)_
- [- splitViewController:popoverController:willPresentViewController:](<uisplitviewcontrollerdelegate/splitviewcontroller(__popovercontroller_willpresent_).md>) — Tells the delegate that the hidden view controller is about to be displayed in a popover. _(deprecated)_

## See Also

### Customizing the split view transitions

- [delegate](uisplitviewcontroller/delegate.md) — The delegate you use to manage changes to a split view interface.
