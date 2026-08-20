---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/RowSelection/RowSelection.html
archived_at: '2026-07-15T07:20:00.049315Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Sorting%20Table%20View%20Rows.md)[Previous](Modifying%20a%20Table%E2%80%99s%20Visual%20Attributes.md)

# Enabling Row Selection and User Actions

Displaying a list of data in a table view is of little use if the user can’t select the rows. Using the methods of the `NSTableView` class, you let users select one or more rows, drag to change a selection, and type to select. In addition, you can enable programmatic selection and display a contextual menu that’s associated with the table.

The `NSTableView` class provides several methods for getting information about a table view’s currently selected rows: [selectedRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes), [selectedRow](https://developer.apple.com/documentation/appkit/nstableview/1535010-selectedrow), [numberOfSelectedRows](https://developer.apple.com/documentation/appkit/nstableview/1527463-numberofselectedrows), and [isRowSelected:](https://developer.apple.com/documentation/appkit/nstableview/1525882-isrowselected).

The [selectedRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes) method provides the full and correct selection whether a single item is selected or multiple items are selected. The method returns an [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset) object containing the indexes of the selected rows.

The [selectedRow](https://developer.apple.com/documentation/appkit/nstableview/1535010-selectedrow) method returns the index of only the last selected row, or -1 if no row is selected. Using this method is the easiest way to get the current selection when multiple selection is disabled.

The [numberOfSelectedRows](https://developer.apple.com/documentation/appkit/nstableview/1527463-numberofselectedrows) method, which returns the number of selected rows, can be used as a shortcut to determine whether any objects are selected when empty selection is permitted. Its value can also be used to determine whether user interface items should be enabled or disabled if they depend upon multiple items being selected in the table view. For example, if the [numberOfSelectedRows](https://developer.apple.com/documentation/appkit/nstableview/1527463-numberofselectedrows) is greater than 1, you can disable the portions of the user interface that are relevant only when a single item is selected.

The [isRowSelected:](https://developer.apple.com/documentation/appkit/nstableview/1525882-isrowselected) method allows an app to find out whether a row at a specific index is selected.

Apps often need to iterate over the selected rows. You can implement this by iterating over the contents of the selection returned by [selectedRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes) or by using the `NSIndexSet` block enumeration method [enumerateIndexesUsingBlock:](https://developer.apple.com/documentation/foundation/nsindexset/1411395-enumerateindexesusingblock). For more information about using these techniques, see [Iterating Through Index Sets](../Collections%20Programming%20Topics/Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrvfvjvona) in _[Collections Programming Topics](../Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)_.

Users can select multiple rows using the Shift key (for continuous selections) or the Command key (for non-contiguous selections). For more information about user selection actions, see Make User Input Convenient in _OS X Human Interface Guidelines_.

As the user selects rows by dragging (using a trackpad or mouse), delegate methods can be informed of the changes in row selection. The delegate receives the following messages as changes in the selection occurs by the user. (Delegates for table views that are managed by Cocoa bindings also receive these messages and can act on them as required.) An app can receive these messages on a continuous basis, so it’s important to create efficient implementations.

- [selectionShouldChangeInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533949-selectionshouldchange)

  This method is usually implemented when it’s necessary to perform validation on editing of a row before allowing the row selection to change.

  For example, if the user is editing a row in the table view and the content of that row doesn’t meet the required criteria, the delegate should return `NO` from this method to prevent the user from changing the selection. If the action was denied, this method is responsible for telling users why the selection change was disallowed and what action they can take to rectify the situation. By default, this method returns `YES`, which allows the selection to be changed.
- [tableViewSelectionIsChanging:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530812-tableviewselectionischanging)

  This method informs the delegate that the row selection is about to change due to interaction with the mouse or trackpad. Keyboard selection does not invoke this method.
- [tableViewSelectionDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange)

  This method informs the delegate that the row selection has changed and that, effectively, the table view selection action is completed. The method is sent to the delegate when the user releases the mouse button, whether selection is limited to a single row or multiple selection is enabled.

The [tableViewSelectionIsChanging:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530812-tableviewselectionischanging) and [tableViewSelectionDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange) messages are notifications. Each is passed an `NSNotification` object. Sending the notification instance an `object` message returns the table view relevant to the selection change.

A table view delegate can also implement the [tableView:selectionIndexesForProposedSelection:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1532829-tableview) delegate method to allow or disallow the selection of a specific set of rows in a table view. The method is passed the indexes of the rows that are proposed to be selected and it returns the rows that will actually be selected. Implementing this method allows the app to selectively allow and disallow row selection as appropriate. For example, if the user clicks in an area of the table row that shouldn’t trigger selection, this method can be used to prevent that selection from taking place.

A table view can be configure selection in three ways:

- Allow a single row to be selected at once
- Allow multiple rows to be selected simultaneously
- Attempt to prevent there from being an empty selection (that is, at least one row is always selected)

These attributes can be configured in Interface Builder or programmatically.

Programmatically, the table view methods for enabling and disabling these options are set using the following methods: [setAllowsMultipleSelection:](https://developer.apple.com/documentation/appkit/nstableview/1532523-allowsmultipleselection) and [setAllowsEmptySelection:](https://developer.apple.com/documentation/appkit/nstableview/1535902-allowsemptyselection).

To select rows programmatically, the `NSTableView` class provides the [selectRowIndexes:byExtendingSelection:](https://developer.apple.com/documentation/appkit/nstableview/1529688-selectrowindexes) instance method.

The [selectRowIndexes:byExtendingSelection:](https://developer.apple.com/documentation/appkit/nstableview/1529688-selectrowindexes) method expects an [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset) containing the indexes (zero-based) of the rows to be selected, and a parameter that specifies whether the current selection should be extended. If the extending selection parameter is `YES`, the specified row indexes are selected in addition to any previously selected rows; if it’s `NO`, the selection is changed to the newly specified rows. When this method is called, the delegate receives only the [tableViewSelectionDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange) notification.

To deselect a row, pass the index of the row to deselect to [deselectRow:](https://developer.apple.com/documentation/appkit/nstableview/1532722-deselectrow). When this method is called the delegate receives only the [tableViewSelectionDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange) notification.

There are also two convenience methods that allow the selection and deselection of all the items in the table view. In general, these methods are connected to the user interface so that users can select or deselect all items in a table. The [deselectAll:](https://developer.apple.com/documentation/appkit/nstableview/1533302-deselectall) method deselects all the selected rows, but only if [allowsEmptySelection](https://developer.apple.com/documentation/appkit/nstableview/1535902-allowsemptyselection) returns `YES`. Similarly, [selectAll:](https://developer.apple.com/documentation/appkit/nstableview/1534002-selectall) selects all the table view rows, but only if [allowsMultipleSelection](https://developer.apple.com/documentation/appkit/nstableview/1532523-allowsmultipleselection) returns `YES`. Unlike the other programmatic methods, these two methods call [selectionShouldChangeInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1533949-selectionshouldchange) on the delegate object, if implemented, followed by [tableViewSelectionDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1528567-tableviewselectiondidchange). If either [deselectAll:](https://developer.apple.com/documentation/appkit/nstableview/1533302-deselectall) or [selectAll:](https://developer.apple.com/documentation/appkit/nstableview/1534002-selectall) is called without the proper `allows...` setting, it is ignored.

To simplify navigation in tables or to allow a user to select items using the keyboard, a table view can support type selection. Using type selection, a user types the first few letters of an entry and the table view content is searched for a matching row. You can use the [setAllowsTypeSelect:](https://developer.apple.com/documentation/appkit/nstableview/1526084-allowstypeselect) method to enable or disable type selection (by default, type selection is enabled).

Type selection uses the delegate method [tableView:typeSelectStringForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530001-tableview) to figure out which rows to match against. This delegate method returns a string that type selection uses for matching.

When the [tableView:typeSelectStringForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1530001-tableview) method is not implemented by the delegate, the behavior is to call [preparedCellAtColumn:row:](https://developer.apple.com/documentation/appkit/nstableview/1534640-preparedcell), passing the column index and row and then returning the `stringValue`. This allows type selection to work on the values in any column and row in the table view. To restrict type selection to specific parts of the table, return `nil` for columns that should be excluded. For example, the following method implementation allows type selection to match values only in the “name” column.

```objc
- (NSString *)tableView:(NSTableView *)tableView typeSelectStringForTableColumn:(NSTableColumn *)tableColumn
                                                                            row:(NSInteger)row
{
    if ([[tableColumn identifier] isEqualToString:@"name"])
    {
        NSUInteger tableColumnIndex=[[tableView tableColumns] indexOfObject:tableColumn];
        return [[tableView preparedCellAtColumn:tableColumnIndex
                                            row:row] stringValue];
    }
    return nil;
}
```

Implementing the delegate method [tableView:nextTypeSelectMatchFromRow:toRow:forString:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1534757-tableview) allows the delegate to further customize type selection to match only a specific range of rows. This method is passed the current type selection string, and it compares the appropriate values within the selected rows, returning the row to select, or -1 if no row matches.

Finally, the [tableView:shouldTypeSelectForEvent:withCurrentSearchString:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1526347-tableview) method gives the delegate the option to allow or disallow type selection for a particular keyboard event. You can implement this method to prevent certain characters from causing type selection. Note that returning `NO` from this method prevents the specified event from being used for type selection; it doesn’t prevent standard event processing. Don’t use `tableView:shouldTypeSelectForEvent:withCurrentSearchString:` to handle your own keyboard shortcuts. If you need to provide custom keyboard shortcut handling, override [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown) instead.

You can use a contextual menu to offer users a convenient way to access a small set of commands that act on one or more items in a table. For example, when users Command-click a song listed in iTunes, a contextual menu appears that makes it easy to (among other things) play, copy, or delete the song.

An easy way to add a contextual menu to a table is to set the [menu](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu) outlet of the table to an [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) object. And if you want to customize the contextual menu, you set an appropriate object as the menu’s delegate and implement the [menuWillOpen:](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518156-menuwillopen) method to customize the menu before it appears.

In the action method for a menu item, determine whether the clicked table row is in the set of indexes returned by [selectedRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/1533844-selectedrowindexes). If it is, apply the action to all indexes in the set; otherwise, apply the action only to the clicked row. Here’s a convenience method that checks the selected row indexes and returns the set of indexes the action method should process:

```objc
- (NSIndexSet *)_indexesToProcessForContextMenu {
    NSIndexSet *selectedIndexes = [_tableViewMain selectedRowIndexes];
    // If the clicked row is in selectedIndexes, then process all selectedIndexes. Otherwise, process only clickedRow.
    if ([_tableViewMain clickedRow] != -1 && ![selectedIndexes containsIndex:[_tableViewMain clickedRow]]) {
        selectedIndexes = [NSIndexSet indexSetWithIndex:[_tableViewMain clickedRow]];
    }
    return selectedIndexes;
}
```

To see an example that uses the `_indexesToProcessForContextMenu` method, download the _[TableViewPlayground: Using View-Based NSTableView and NSOutlineView](../../../samplecode/TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView/TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytanzsg4)_ sample project and look at the `mnuRevealInFinderSelected:` method in `ATComplexTableViewController.m`.

Views or controls in a table sometimes need to respond to incoming events. To determine whether a particular subview should receive the current mouse event, a table view calls [validateProposedFirstResponder:forEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1527066-validateproposedfirstresponder) in its implementation of `hitTest`. If you create a table view subclass, you can override `validateProposedFirstResponder:forEvent:` to specify which views can become the first responder. In this way, you receive mouse events.

The default `NSTableView` implementation of `validateProposedFirstResponder:forEvent:` uses the following logic:

1. Return `YES` for all proposed first responder views unless they are instances or subclasses of `NSControl`.
2. Determine whether the proposed first responder is an `NSControl` instance or subclass.

   - If the control is an `NSButton` object, return `YES`.
   - If the control is not an `NSButton`, call the control’s [hitTestForEvent:inRect:ofView:](https://developer.apple.com/documentation/appkit/nscell/1529601-hittestforevent) to see whether the hit area is trackable (that is, [NSCellHitTrackableArea](https://developer.apple.com/documentation/appkit/nscellhitresult/nscellhittrackablearea)) or is an editable text area (that is, [NSCellHitEditableTextArea](https://developer.apple.com/documentation/appkit/nscell/hitresult/1529959-editabletextarea)), and return the appropriate value. Note that if a text area is hit, `NSTableView` also delays the first responder action.

[Next](Sorting%20Table%20View%20Rows.md)[Previous](Modifying%20a%20Table%E2%80%99s%20Visual%20Attributes.md)

