---
title: Outline View Programming Topics
apple_id: 10000023i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OutlineView/Articles/UsingOutlineDelegate.html
archived_at: '2026-07-15T07:17:40.073646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Outline View Programming Topics](Introduction%20to%20Outline%20Views.md)


[Next](Document%20Revision%20History.md)[Previous](Writing%20an%20Outline%20View%20Data%20Source.md)

# Using an Outline View Delegate

The [NSOutlineViewDelegate](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate) protocol gives the delegate control over the appearance of individual cells in the table, over changes in selection, and over editing of cells.

Delegate methods that request permission to alter the selection or edit a value are invoked during user actions that affect the outline view, but are not invoked by programmatic changes to the view. When making changes programmatically, you decide whether you want the delegate to intervene and, if so, you send the appropriate message (checking first that the delegate responds to that message). Because the delegate methods involve the actual data displayed by the outline view, the delegate is typically the same object as the data source, though this is not a requirement.

The [NSOutlineViewDelegate](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate) protocol defines these delegate messages:

- `outlineView:willDisplayCell:forTableColumn:item:` informs the delegate that the outline view is about to draw the cell specified by the passed column and item. The delegate can modify the instance of [NSCell](https://developer.apple.com/documentation/appkit/nscell) provided to alter the display attributes for that cell; for example, making uneditable values display in italic or gray text.
- `outlineView:shouldSelectItem:` and `outlineView:shouldSelectTableColumn:` give the delegate control over whether the user can select a specified row or column (though the user can still reorder columns). This is useful for disabling a specified row or column. For example, in a database client application, when a user is editing a record you might want to not allow other users to select the same row.
- `selectionShouldChangeInOutlineView:` allows the delegate to deny a change in selection. For example, if the user is editing a cell and enters an improper value, the delegate can prevent the user from selecting or editing any other cells until a proper value has been entered into the original cell.
- `outlineView:shouldEditTableColumn:item:` asks the delegate whether it’s okay to edit the cell specified by the passed column and item. The delegate can approve or deny the request.

The [NSOutlineViewDelegate](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate) protocol defines these additional delegate messages:

- `outlineView:shouldExpandItem:` asks the delegate whether it’s okay to expand the specified item.
- `outlineViewItemWillExpand:` informs the delegate that the outline view is about to expand the specified item.
- `outlineView:shouldCollapseItem:` asks the delegate whether it’s okay to collapse the specified item.
- `outlineViewItemWillCollapse:` informs the delegate that the outline view is about to collapse the specified item.
- `outlineView:willDisplayOutlineCell:forTableColumn:item:` informs the delegate that the outline view is about to display the cell that includes the expansion symbol.

In addition to these methods, the delegate protocol is automatically registered to receive messages corresponding to `NSOutlineView` notifications. These inform the delegate when the selection changes or is about to change, when a column is moved or resized, and when an item is expanded or collapsed:

| Delegate Message | Notification |
| --- | --- |
| `outlineViewColumnDidMove:` | [NSOutlineViewColumnDidMoveNotification](https://developer.apple.com/documentation/appkit/nsoutlineview/1533529-columndidmovenotification) |
| `outlineViewColumnDidResize:` | [NSOutlineViewColumnDidResizeNotification](https://developer.apple.com/documentation/appkit/nsoutlineviewcolumndidresizenotification) |
| `outlineViewSelectionDidChange:` | [NSOutlineViewSelectionDidChangeNotification](https://developer.apple.com/documentation/appkit/nsoutlineviewselectiondidchangenotification) |
| `outlineViewSelectionIsChanging:` | [NSOutlineViewSelectionIsChangingNotification](https://developer.apple.com/documentation/appkit/nsoutlineview/1529181-selectionischangingnotification) |
| `outlineViewItemDidExpand:` | [NSOutlineViewItemDidExpandNotification](https://developer.apple.com/documentation/appkit/nsoutlineviewitemdidexpandnotification) |
| `outlineViewItemDidCollapse:` | [NSOutlineViewItemDidCollapseNotification](https://developer.apple.com/documentation/appkit/nsoutlineview/1526467-itemdidcollapsenotification) |

[Next](Document%20Revision%20History.md)[Previous](Writing%20an%20Outline%20View%20Data%20Source.md)

