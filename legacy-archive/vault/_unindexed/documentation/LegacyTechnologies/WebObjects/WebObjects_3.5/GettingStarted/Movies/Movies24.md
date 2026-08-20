---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies24.html
archived_at: '2026-07-15T07:54:24.710650Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies23.md)

## Optional Exercise

You can tidy up the user interface even further by putting the query part of the page in a table to match the editing part of the page. Also, you should consider capitalizing __Main.wo__'s text field labels.
To put the query part of the page in a table, follow these steps:

- Put the cursor inside the form element before the "title" text field.
- In the Tables toolbar, click the ! button to add a table.

A table with two rows and two columns appears. Initially the table spans the entire width of the page. You'll resize it later.

When the table is first added, it's in structure-editing mode. You can tell it's in structure-editing mode because it has ! buttons for adding rows and columns and because it has ! and ! icons around each of the table's rows.

- Inspect the new table.
!- In the Table Inspector, choose Unspecified for the table width.

The table resizes to just fit its contents. When you change the cell contents later, the table will resize again to accommodate the new values.

- Also in the Table Inspector, set the border to 0 to remove the appearance of a border.
- Click the ! button in the lower left of the table to add a new row to the table.
- Type the labels Title:, Category:, and Rating: in the cells in the first column.

Recall that to put the table into content-editing mode, click the ! button or double-click in one of the table's cells.

The table doesn't resize to accommodate new cell content until you're done typing; that is, until you move the cursor out of the edited cell.

- Cut and paste the query text fields into their corresponding table cells.

Just click on a text field to select it. When a text field is selected, it displays with a gray "shadow."

- Delete the old query field labels.

When you're done, the query part should look like this:!
Now edit the text labels in the editing part of the page and put any other finishing touches on the page that you want. The finished component might look something like this:!

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies25.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
