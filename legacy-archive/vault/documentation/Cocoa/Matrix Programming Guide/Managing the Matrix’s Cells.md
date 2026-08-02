---
title: Matrix Programming Guide
apple_id: 10000022i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Tasks/ManagingMatrixCells.html
archived_at: '2026-07-15T07:16:39.675682Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Matrix Programming Guide](Introduction%20to%20Matrices.md)


[Next](Setting%20a%20Matrix%E2%80%99s%20Appearance.md)[Previous](Matrix%20Selection%20Modes.md)

# Managing the Matrix’s Cells

These methods dynamically add and remove columns:

- To add a column of empty cells beyond the last column, use `addColumn`.
- To add a column of filled cells beyond the last column, use `addColumnWithCells:`.
- To insert a column of empty cells at a specified location, use `insertColumn:`.
- To insert a column of filled cells at a specified location, use `insertColumn:withCells:`.
- To remove a column of cells, use `removeColumn:`.

These methods dynamically add and remove rows:

- To add a row of empty cells below the last row, use `addRow`.
- To add a row of filled cells below the last row, use `addRowWithCells:`.
- To insert a row of empty cells at a specified location, use `insertRow:`.
- To insert a row of filled cells at a specified location, use `insertRow:withCells:`.
- To remove a row of cells, use `removeRow:`.

This method creates individual cells:

- To replace an specific cell with a new cell, use `putCell:atRow:column:`.

This method retrieves information about individual cells:

- To get the frame of a specified cell, use `cellFrameAtRow:column:`.

These methods retrieve information about the matrix:

- To get the numbers of rows and columns, use `numberOfColumns` and `numberOfRows`.

These methods locate particular cells:

- To find a cell at a particular location, use `cellAtRow:column:`.
- To find a cell with a particular tag, use `cellWithTag:`.
- To get a list of all the cells, use `cells`.

These methods manage the selection:

- To retrieve the current selection, use `selectedCell` or `selectedCells`.
- To select a particular cell, use `selectCellAtRow:column:` or `selectCellWithTag`.
- To select a range of cells, use `selectAll:` or `setSelectionFrom:to:anchor:highlight:`.
- To deselect cells, use `deselectAllCells` or `deselectSelectedCell`.
- To retrieve the column and row number for the selection, use `selectedColumn` and `selectedRow`.
- To select the text in a cell (for a matrix that contains text fields), use `selectTextAtRow:column:`.

[Next](Setting%20a%20Matrix%E2%80%99s%20Appearance.md)[Previous](Matrix%20Selection%20Modes.md)

