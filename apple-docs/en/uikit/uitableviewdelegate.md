---
title: UITableViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate.json'
content_hash: 'sha256:cb81cfb5be343554'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDelegate

<sub>Protocol</sub>

Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITableViewDelegate : UIScrollViewDelegate
```

## Overview

Use the methods of this protocol to manage the following features:

- Create and manage custom header and footer views.
- Specify custom heights for rows, headers, and footers.
- Provide height estimates for better scrolling support.
- Indent row content.
- Respond to row selections.
- Respond to swipes and other actions in table rows.
- Support editing the table’s content.

The table view specifies rows and sections using [IndexPath](../foundation/indexpath.md). For information about how to interpret row and section indexes, see [Specify the location of rows and sections](uitableviewdatasource.md#Specify-the-location-of-rows-and-sections).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIScrollViewDelegate](uiscrollviewdelegate.md)

- **Conforming Types**: [UITableViewController](uitableviewcontroller.md)

## Topics

### Configuring rows for the table view

- [- tableView:willDisplayCell:forRowAtIndexPath:](<uitableviewdelegate/tableview(__willdisplay_forrowat_).md>) — Tells the delegate the table view is about to draw a cell for a particular row.
- [- tableView:indentationLevelForRowAtIndexPath:](<uitableviewdelegate/tableview(__indentationlevelforrowat_).md>) — Asks the delegate to return the level of indentation for a row in a given section.
- [- tableView:shouldSpringLoadRowAtIndexPath:withContext:](<uitableviewdelegate/tableview(__shouldspringloadrowat_with_).md>) — Called to let you fine tune the spring-loading behavior of the rows in a table.

### Responding to row selections

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md) — Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- tableView:willSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__willselectrowat_).md>) — Tells the delegate a row is about to be selected.
- [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>) — Tells the delegate a row is selected.
- [- tableView:willDeselectRowAtIndexPath:](<uitableviewdelegate/tableview(__willdeselectrowat_).md>) — Tells the delegate that a specified row is about to be deselected.
- [- tableView:didDeselectRowAtIndexPath:](<uitableviewdelegate/tableview(__diddeselectrowat_).md>) — Tells the delegate that the specified row is now deselected.
- [- tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<uitableviewdelegate/tableview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [- tableView:didBeginMultipleSelectionInteractionAtIndexPath:](<uitableviewdelegate/tableview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [- tableViewDidEndMultipleSelectionInteraction:](<uitableviewdelegate/tableviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.

### Providing custom header and footer views

- [- tableView:viewForHeaderInSection:](<uitableviewdelegate/tableview(__viewforheaderinsection_).md>) — Asks the delegate for a view to display in the header of the specified section of the table view.
- [- tableView:viewForFooterInSection:](<uitableviewdelegate/tableview(__viewforfooterinsection_).md>) — Asks the delegate for a view to display in the footer of the specified section of the table view.
- [- tableView:willDisplayHeaderView:forSection:](<uitableviewdelegate/tableview(__willdisplayheaderview_forsection_).md>) — Tells the delegate that the table is about to display the header view for the specified section.
- [- tableView:willDisplayFooterView:forSection:](<uitableviewdelegate/tableview(__willdisplayfooterview_forsection_).md>) — Tells the delegate that the table is about to display the footer view for the specified section.

### Providing header, footer, and row heights

- [- tableView:heightForRowAtIndexPath:](<uitableviewdelegate/tableview(__heightforrowat_).md>) — Asks the delegate for the height to use for a row in a specified location.
- [- tableView:heightForHeaderInSection:](<uitableviewdelegate/tableview(__heightforheaderinsection_).md>) — Asks the delegate for the height to use for the header of a particular section.
- [- tableView:heightForFooterInSection:](<uitableviewdelegate/tableview(__heightforfooterinsection_).md>) — Asks the delegate for the height to use for the footer of a particular section.
- [UITableViewAutomaticDimension](uitableview/automaticdimension.md) — A constant representing the default value for a given dimension.

### Estimating heights for the table’s content

- [- tableView:estimatedHeightForRowAtIndexPath:](<uitableviewdelegate/tableview(__estimatedheightforrowat_).md>) — Asks the delegate for the estimated height of a row in a specified location.
- [- tableView:estimatedHeightForHeaderInSection:](<uitableviewdelegate/tableview(__estimatedheightforheaderinsection_).md>) — Asks the delegate for the estimated height of the header of a particular section.
- [- tableView:estimatedHeightForFooterInSection:](<uitableviewdelegate/tableview(__estimatedheightforfooterinsection_).md>) — Asks the delegate for the estimated height of the footer of a particular section.

### Managing accessory views

- [- tableView:accessoryButtonTappedForRowWithIndexPath:](<uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) — Tells the delegate that the user tapped the detail button for the specified row.

### Managing context menus

- [Adding context menus in your app](adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<uitableviewdelegate/tableview(__contextmenuconfigurationforrowat_point_).md>) — Returns a context menu configuration for the row at a point.
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<uitableviewdelegate/tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — Returns the destination view when dismissing a context menu.
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<uitableviewdelegate/tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — Returns a view to override the default preview the table view created.
- [- tableView:willDisplayContextMenuWithConfiguration:animator:](<uitableviewdelegate/tableview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- tableView:willEndContextMenuInteractionWithConfiguration:animator:](<uitableviewdelegate/tableview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- tableView:willPerformPreviewActionForMenuWithConfiguration:animator:](<uitableviewdelegate/tableview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.

### Responding to row actions

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__leadingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the leading edge of the row.
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__trailingswipeactionsconfigurationforrowat_).md>) — Returns the swipe actions to display on the trailing edge of the row.
- [- tableView:shouldShowMenuForRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldshowmenuforrowat_).md>) — Asks the delegate if the editing menu should be shown for a certain row. _(deprecated)_
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<uitableviewdelegate/tableview(__canperformaction_forrowat_withsender_).md>) — Asks the delegate if the editing menu should omit the Copy or Paste command for a given row. _(deprecated)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<uitableviewdelegate/tableview(__performaction_forrowat_withsender_).md>) — Tells the delegate to perform a copy or paste operation on the content of a given row. _(deprecated)_
- [- tableView:editActionsForRowAtIndexPath:](<uitableviewdelegate/tableview(__editactionsforrowat_).md>) — Asks the delegate for the actions to display in response to a swipe in the specified row. _(deprecated)_

### Managing table view highlights

- [- tableView:shouldHighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldhighlightrowat_).md>) — Asks the delegate if the specified row should be highlighted.
- [- tableView:didHighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__didhighlightrowat_).md>) — Tells the delegate that the specified row was highlighted.
- [- tableView:didUnhighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__didunhighlightrowat_).md>) — Tells the delegate that the highlight was removed from the row at the specified index path.

### Editing table rows

- [- tableView:willBeginEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__willbegineditingrowat_).md>) — Tells the delegate that the table view is about to go into editing mode.
- [- tableView:didEndEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__didendeditingrowat_).md>) — Tells the delegate that the table view has left editing mode.
- [- tableView:editingStyleForRowAtIndexPath:](<uitableviewdelegate/tableview(__editingstyleforrowat_).md>) — Asks the delegate for the editing style of a row at a particular location in a table view.
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<uitableviewdelegate/tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — Changes the default title of the delete-confirmation button.
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldindentwhileeditingrowat_).md>) — Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.

### Reordering table rows

- [- tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:](<uitableviewdelegate/tableview(__targetindexpathformovefromrowat_toproposedindexpath_).md>) — Asks the delegate to return a new index path to retarget a proposed move of a row.

### Tracking the removal of views

- [- tableView:didEndDisplayingCell:forRowAtIndexPath:](<uitableviewdelegate/tableview(__didenddisplaying_forrowat_).md>) — Tells the delegate that the specified cell was removed from the table.
- [- tableView:didEndDisplayingHeaderView:forSection:](<uitableviewdelegate/tableview(__didenddisplayingheaderview_forsection_).md>) — Tells the delegate that the specified header view was removed from the table.
- [- tableView:didEndDisplayingFooterView:forSection:](<uitableviewdelegate/tableview(__didenddisplayingfooterview_forsection_).md>) — Tells the delegate that the specified footer view was removed from the table.

### Managing table view focus

- [- tableView:canFocusRowAtIndexPath:](<uitableviewdelegate/tableview(__canfocusrowat_).md>) — Asks the delegate whether the cell at the specified index path is itself focusable.
- [- tableView:shouldUpdateFocusInContext:](<uitableviewdelegate/tableview(__shouldupdatefocusin_).md>) — Asks the delegate whether the focus update specified by the context is allowed to occur.
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<uitableviewdelegate/tableview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update specified by the context has just occurred.
- [- indexPathForPreferredFocusedViewInTableView:](<uitableviewdelegate/indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the table view’s index path for the preferred focused view.
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<uitableviewdelegate/tableview(__selectionfollowsfocusforrowat_).md>) — Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.

### Performing primary actions

- [- tableView:canPerformPrimaryActionForRowAtIndexPath:](<uitableviewdelegate/tableview(__canperformprimaryactionforrowat_).md>) — Asks the delegate whether to perform a primary action for the row at the specified index path.
- [- tableView:performPrimaryActionForRowAtIndexPath:](<uitableviewdelegate/tableview(__performprimaryactionforrowat_).md>) — Tells the delegate to perform the primary action for the row at the specified index path.

## See Also

### Table management

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md) — Provide height estimates for your table view’s headers, footers, and rows to ensure that scrolling accurately reflects the size of your content.
- [UITableViewController](uitableviewcontroller.md) — A view controller that specializes in managing a table view.
- [UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md) — A context object that provides information relevant to a specific focus update from one view to another.
