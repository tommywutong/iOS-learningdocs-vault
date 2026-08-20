---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/EditMode.htm
archived_at: '2026-07-15T07:57:02.932268Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](WrkTabls.md)[Previous
Section](WrkTabls.md) 

## Table Editing Modes

There are two "modes" that you can be in when working
with tables. When you first create a table, you are in "structure editing"
mode, indicated by the gray handles and ! icons.
In this mode, you can select cells, groups of cells, or the entire table,
and perform operations on them.

The other mode is "content editing" mode, in
which you can insert text or other elements (including other tables) inside
table cells. In this mode, the gray handles and !
icons are not present.

To change from structure editing to content editing
mode, double-click in a cell. The cell's contents are selected, and you
can type or select an element from the toolbar to replace them. To change
from content editing to structure editing mode, press Control and click
in any cell other than the one that was selected.

Alternatively, you can switch from one mode
to the other by clicking ! in the toolbar. Also,
after you've clicked anywhere outside a table, clicking in the table puts
you in content editing mode; Control-clicking puts you in structure editing
mode.

In structure editing mode, you can:

- Select an individual cell by clicking it. 
- Select a row by clicking one of the gray handles at the end of the row. 
- Select a column by clicking the top cell in a column and dragging to the
  bottom. 
- Select additional cells by clicking them while holding down the Shift key. 
- Select the entire table, or any group of contiguous cells by clicking and
  dragging. 
- Delete a row by selecting it (or any cell in the row) and clicking !. 
- Delete a column by selecting any cell in the column and clicking !. 
- Split a selected cell horizontally by clicking !
  or vertically by clicking !. 
- Merge a group of selected contiguous cells into a single cell by clicking !.
  __Note:__ This command isn't enabled unless the selected cells make
  up a group that could logically be merged into one cell. 
- Wrap an abstract dynamic element (conditional or repetition) around a selected
  row or cell (see ["Repetitions"](../DynamicElements/Reps.md#apple-geydknjq)) by clicking
  dynamic element's icon in the toolbar.

In content editing mode, you can:

- Type text in the cell. 
- Add another element inside a cell (by clicking its toolbar icon or using
  a menu command).

In either mode, you can press Tab to move to the next
cell to the right (or the first cell of the next row if in the rightmost
column). Pressing Shift-Tab moves in the opposite direction through the
table.

A special case arises when you have embedded
a table within a table cell. In this case:

- To edit text in a cell in the embedded table, just click in the cell. 
- To select the embedded table or one of its elements, first click in the
  cell surrounding the embedded table, and then Control-click the embedded
  table to select it.

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](Sizing.md)[Next
Section](Sizing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
