---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus4.html
archived_at: '2026-07-18T01:21:36.909358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](GuestBookPlus3.md)

## Creating a Table to Display the Output

In the first chapter, you created three WOString elements to display the information the guest entered. In this tutorial, you'll create a different type of element, an HTML table, to display the information. In later tasks, you'll display data for multiple users in the table.

- Delete the WOStrings below the horizontal line in the Main component, because you'll be replacing them with a table. Select the WOStrings and choose Cut from the Edit menu to delete them.
- Choose ! from the Elements pop-up list to display table elements.
- Click the ! button.

A table with two rows and two columns appears.

!

- Click the ! icon at the upper right of the table.

A third column appears, and the columns are equally spaced.

- Select the upper-left cell of the table by clicking it.

There are two modes for table editing: _content-editing_mode, which lets you change the text in a cell and add other elements to it; and _structure-editing_ mode, which lets you perform operations on a cell such as splitting it in two. The cell you just selected is now in structure-editing mode.

- Double-click the upper-left cell.

You can now edit the contents of the cell. If you want to resume structure editing, click ! in the toolbar, which allows you to toggle between modes. (Alternatively, you can hold down the Control key and click in a different cell to enter structure-editing mode.)

- Change the text in the cell to Name.
- Open the Inspector.

The Inspector presents a number of modifiable settings that apply to the table cell you've selected. Note also that the top row of the Inspector window shows the element path, which includes the cell, the row it is contained in, and the table itself. Selecting any of those allows you to set specific properties of the selected element.

!

- Click the Header Cell checkbox.

The text in the cell becomes bold and centered.

- In the Width box, enter 150 in the field marked "pixels" and press Enter.

The width of the column is set to 150 pixels.

- Click in the component window, then press Tab.

Pressing Tab when editing a table causes the contents of the next cell to the right to be selected (or the first cell of the next row if in the rightmost column). Pressing Shift-Tab moves in the opposite direction through the table.

- Repeat steps 7 through 11 for the second and third cells of the top row. Label the middle column E-mail and set its width to 150 pixels. Label the third column Comments and leave its width unset. (The comments field takes up the remainder of the width of the table.)

__Note:__ It isn't necessary to adjust the height of the columns-if left unset, they'll expand at run time to accommodate the size of the text being displayed.

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](GuestBookPlus5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
