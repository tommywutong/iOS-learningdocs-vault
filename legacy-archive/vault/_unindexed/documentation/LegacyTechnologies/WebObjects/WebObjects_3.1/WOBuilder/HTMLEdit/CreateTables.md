---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/HTMLEdit/CreateTables.html
archived_at: '2026-07-15T07:50:38.446022Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HTMLEdit.book.md)
[!Previous Section](CreateHyperlinks.md)

Creating Tables

# Creating Tables

Create a table just like you would any other type of static HTML element: Place the cursor where the table should appear, and drag the table from the Static Elements palette. (See "[Using the Static Elements Palette](UsingStaticElementsPalette.md#apple-kjcumobrgazti)".)

!

- To edit the table, click inside the table. You will see resize borders and arrows pointing down and to the right.
- To resize the table, drag a resize border. You can drag a column edge to resize one column.
- Add columns by dragging the right arrow.
- Add rows by dragging the down arrow.
- To select a row or column in the table, drag the mouse across it.
- To delete a row or column, select it and press the Delete key.
- To merge cells, select the cells and choose Format->Table->Merge Cells.
- Set the HTML attributes for a table (for example the size of its border, cell padding, and alignment) in the inspector window.
- To add another HTML element inside of a cell, make sure you have the text inside the cell selected rather than the cell itself, then drag the element from the palette.
- You can also add an element outside of a table cell (for example, you can add a WORepetition around a table row) by selecting the row and dragging the element onto it.

  __Tip:__ To set bindings for an element that surrounds a table row, use the inspector interface. Click inside the row, then select the element from the icon path in the inspector. See "[Selecting Elements](SelectElements.md#apple-kjcummrrge4tq)" and "[Binding Elements Using the Inspector](../DynElem/BindInInspector.md)" for more information.

[!Table of Contents](HTMLEdit.book.md)
[!Next Section](CreateImages.md)
