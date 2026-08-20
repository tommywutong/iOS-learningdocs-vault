---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.34.html
archived_at: '2026-07-15T08:10:27.521505Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Working%20With%20Tables.md) [!](Creating%20Tables.md) [!](Modifying%20a%20Cell%27s%20Contents.md)

---

#  Inspecting and Making Selections

When you select the table or a part of it, the selection's HTML properties appear in the Inspector. You can use the Inspector to set these properties (for example, the width and height of a cell.)

Click in a cell to select it. To move to the next cell to the right (or the first cell of the next row if in the rightmost column), press Tab. If you reach the end of the table, pressing Tab will create a new row. Pressing Shift-Tab moves the opposite direction through the table.

An HTML table (<TABLE>) is a hierarchical structure, which contains rows (<TR>). Rows, in turn, contain cells (<TH> and<TD>). When you select a cell, the path view shows the path from the cell up to the page (<BODY>); you can inspect any element in the path by clicking its tag. For example, if you select a table cell, you can inspect the cell, the row (by clicking <TR> in the path view), or the table itself (by clicking <TABLE> in the path view).

!

You can select multiple cells by

- 

  clicking in a cell and dragging across the cells,
- 

  selecting a cell and shift clicking in another cell, or
- 

  command-clicking each cell on Rhapsody or control-clicking each cell on Windows NT.

The first two selection methods ensure that the selected cells form a contiguous region.

Note that selecting all of the cells in a row or table is not the same as selecting the row or table. To select a row, you need to select one or more cells in the row and click the <TR> element in the path view. To select the entire table, you need to select one or more cells in the table and click the <TABLE> element in the path view.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Working%20With%20Tables.md) [!](Creating%20Tables.md) [!](Modifying%20a%20Cell%27s%20Contents.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
