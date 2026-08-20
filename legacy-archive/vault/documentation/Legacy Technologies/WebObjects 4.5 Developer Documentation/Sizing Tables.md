---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.37.html
archived_at: '2026-07-15T08:10:33.024626Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Working%20With%20Tables.md) [!](Changing%20the%20Table%20Structure.md) [!](Setting%20Page%20Attributes.md)

---

#  Sizing Tables

By default, the size of a table is determined by the contents of the table's cells. If you type text (or insert other elements) inside a table cell, the cell's width expands as necessary to fit the data. The width of any column, therefore, will be that of the widest cell in the column. __Note:__
In WebObjects Builder, a cell does not resize until you have finished editing the cell and tabbed to another cell or moved out of the table. To update the cell immediately, press the Escape key.

If you want to set the size of a table or cell explicitly, use the Inspector:

- 

  To set the width or height of a table, select the table and use the Table Inspector. You can enter values that correspond to HTML attributes controlling the size of the table.
- 

  To set the width or height of a cell, select the cell and use the Table Data Inspector. Changing a cell's size affects the size of the column or row containing the cell.

__Warning:__ WebObjects Builder allows you to set sizing specifications that may be impossible, for example, percentages that add to more than 100% or cells in the same column with different widths. The way such tables appear depends on the browser.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Working%20With%20Tables.md) [!](Changing%20the%20Table%20Structure.md) [!](Setting%20Page%20Attributes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
