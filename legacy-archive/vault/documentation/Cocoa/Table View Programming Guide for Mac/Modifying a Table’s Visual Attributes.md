---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/VisualAttributes/VisualAttributes.html
archived_at: '2026-07-15T07:20:02.235115Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Enabling%20Row%20Selection%20and%20User%20Actions.md)[Previous](Populating%20a%20Table%20View%20Using%20Cocoa%20Bindings.md)

# Modifying a Table’s Visual Attributes

A table’s appearance is highly customizable. You can customize the color of the background, rows, and grid lines, the selection highlight style, and the row height. In most cases, you can use either table view methods or Interface Builder settings to customize a table’s appearance.

The background color specifies the color OS X uses to draw the background of the table view. To set the background color of a table view in Interface Builder, use the Table View Attributes inspector. To programmatically set the background color, use the [setBackgroundColor:](https://developer.apple.com/documentation/appkit/nstableview/1527806-backgroundcolor) and [backgroundColor](https://developer.apple.com/documentation/appkit/nstableview/1527806-backgroundcolor) methods.

If your app needs to display a transparent table view, set the background color of the table view to be clear and set the enclosing scroll view to not draw its background. The following code snippet shows one way to display a transparent table:

```
[theTableView setBackgroundColor:[NSColor clearColor];
[[theTableView enclosingScrollView] setDrawsBackground:NO];
```

By default, a table view uses the [NSCompositeSourceOver](https://developer.apple.com/documentation/appkit/nscompositesourceover) style when drawing the background color. The default background color is returned by the [NSColor](https://developer.apple.com/documentation/appkit/nscolor) method [controlBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/1531948-controlbackgroundcolor). Because this color is defined by the system, any view or control that needs to draw its background will do so in a consistent manner.

Using alternating colors can make it easier for users to visually match the data in one column with the data in another column. The Alternating Rows checkbox in the Table View Attributes inspector lets you specify whether all table rows use the same background color, or if alternating rows use the color returned by the [NSColor](https://developer.apple.com/documentation/appkit/nscolor) method [controlAlternatingRowBackgroundColors](https://developer.apple.com/documentation/appkit/nscolor/1530934-controlalternatingrowbackgroundc). To set alternating background colors programmatically, use [setUsesAlternatingRowBackgroundColors:](https://developer.apple.com/documentation/appkit/nstableview/1533967-usesalternatingrowbackgroundcolo) and [usesAlternatingRowBackgroundColors](https://developer.apple.com/documentation/appkit/nstableview/1533967-usesalternatingrowbackgroundcolo).

The Highlight pop-up menu in the Table View Attributes inspector lets you choose the highlighting style used when users select row items. Setting the Highlight attribute provides a different background color for the table view and a corresponding highlight color. You can choose None, Regular, or Source List (the Finder sidebar and the iTunes playlist view both use a source list).

To achieve the same behavior programmatically, implement the following code fragment:

```
[theTableView setSelectionHighlightStyle: NSTableViewSelectionHighlightStyleSourceList]
```

This code fragment sets the background color and highlight colors that are appropriate for the source list style. To specify the regular highlighting style, use the same method, but pass [NSTableViewSelectionHighlightStyleRegular](https://developer.apple.com/documentation/appkit/nstableview/selectionhighlightstyle/regular) as the parameter.

Use the Horizontal and Vertical Grid pop-up menus in the Table View Attributes inspector to enable or disable the drawing of grid lines between columns and rows. To set the grid line color, use the Grid Color pop-up menu.

To set grid lines programmatically, use the [setGridStyleMask:](https://developer.apple.com/documentation/appkit/nstableview/1528689-gridstylemask) method with the constants [NSTableViewSolidHorizontalGridLineMask](https://developer.apple.com/documentation/appkit/nstableview/gridlinestyle/1530960-solidhorizontalgridlinemask), [NSTableViewSolidVerticalGridLineMask](https://developer.apple.com/documentation/appkit/nstableview/gridlinestyle/1530626-solidverticalgridlinemask) and `NSTableViewDashedHorizontalGridLineMask`. To display both horizontal and vertical lines, combine the constants using the bitwise C operator. To disable grid line drawing entirely, pass [NSTableViewGridNone](https://developer.apple.com/documentation/appkit/nstableviewgridlinestyle/nstableviewgridnone) as the parameter.

To programmatically set and retrieve the color of the grid lines, use the [setGridColor:](https://developer.apple.com/documentation/appkit/nstableview/1524620-gridcolor) and [gridColor](https://developer.apple.com/documentation/appkit/nstableview/1524620-gridcolor) methods.

The row height, as expected, specifies the height of a table view’s rows. This value can be set using the method [setRowHeight:](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight) and retrieved using the method [rowHeight](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight).

When [setRowHeight:](https://developer.apple.com/documentation/appkit/nstableview/1529148-rowheight) is called, the table view invokes the [tile](https://developer.apple.com/documentation/appkit/nstableview/1528077-tile) method. The `tile` method properly resizes the rows and the header view, and it marks the table view as needing display. Another effect of setting the row height is that it modifies the line scroll amount in the enclosing scroll view so that scrolling by line continues to provide the expected results.

The `NSTableViewDelegate` method [tableView:heightOfRow:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1529684-tableview) allows you to customize the height of rows on a row-by-row basis.

[Next](Enabling%20Row%20Selection%20and%20User%20Actions.md)[Previous](Populating%20a%20Table%20View%20Using%20Cocoa%20Bindings.md)

