---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.19.html
archived_at: '2026-07-15T08:07:14.127972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Binding%20the%20Class%27s%20Instance%20Variables%20to%20the%20Form%20Elements.md) [!](Adding%20Dynamic%20Elements%20to%20Table%20Cells.md)

---

#  Creating a Table to Display the Output

In the first chapter, you created three WOString elements to display the information the guest entered. In this tutorial, you'll create a different type of element, an HTML table, to display the information. In later tasks, you'll display data for multiple users in the table.

1. 

   Delete the WOString elements below the horizontal line in the Main component, because you'll be replacing them with a table. Select the WOString elements and choose Cut from the Edit menu to delete them.
2. 

   Click the ! button.

   The New Table panel appears. On the right is the Preview pane, which displays what your table will look like.

   !
3. 

   In the Columns field, type 3 and press Enter. A third column appears in the preview pane.
4. 

   In the Border field, enter 1. A border appears around the table in the preview pane.
5. 

   Click "First row cells are header cells (<TH>)". The top row text becomes bold in the preview pane.
6. 

   Click OK. The table appears in your page.
7. 

   Select the upper-left cell of the table by clicking it.
8. 

   Change the text in the cell to Name.
9. 

   Open the Inspector if it is not already open.

The Inspector presents a number of modifiable settings that apply to the table cell you've selected.

!10. 

    Select pixels from the Width pop-up list. Enter 150 in the Width field.

The width of the column is set to 150 pixels.

11. 

    Click in the component window, then press Tab.

Pressing Tab when editing a table causes the contents of the next cell to the right to be selected (or the first cell of the next row if in the rightmost column). Pressing Shift-Tab moves in the opposite direction through the table.

12. 

    Repeat steps 8 through 11 for the second and third cells of the top row. Label the middle column E-mail and set its width to 150 pixels. Label the third column Comments and leave its width unset. (The comments field takes up the remainder of the width of the table.)

__Note:__ It isn't necessary to adjust the height of the columns--if left unset, they'll expand at runtime to accommodate the size of the text being displayed.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Binding%20the%20Class%27s%20Instance%20Variables%20to%20the%20Form%20Elements.md) [!](Adding%20Dynamic%20Elements%20to%20Table%20Cells.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
