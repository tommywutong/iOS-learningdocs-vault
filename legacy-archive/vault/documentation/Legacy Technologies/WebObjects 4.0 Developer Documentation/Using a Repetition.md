---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus12.html
archived_at: '2026-07-18T01:21:24.021351Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](Adding%20a%20Second%20Component.md)

# Using a Repetition

Now you'll create a table to display the entire list of guests in the GuestList component. To do so, you'll use a dynamic element called a _repetition_(an instance of the WORepetition class). Repetitions are one of the most important elements in WebObjects, since it is quite common for applications to display repeated data (often from databases) when the amount of data to be displayed isn't known until run time. Typically, a repetition is used to generate items in a list or a browser, multiple rows in a table, or multiple tables.
A repetition can contain any other elements, either static HTML or dynamic WebObjects elements. In the GuestList component, you'll create a repetition that contains a table row.
You'll bind the __allGuests__ array to the WORepetition's __list__ attribute. This tells WebObjects to generate the elements in the repetition once for each item in the array. Each time WebObjects iterates through the array, it sets the repetition's __item__ attribute to the current array object. You bind __item__ to the variable __currentGuest__ and use __currentGuest__'s fields to bind the elements inside the repetition (such as WOStrings). At run time, the table will consist of one row (displaying name,
e-mail address, and comments) for each guest.

- In WebObjects Builder, make the Main component window active (double-click __Main.wo__).
- Select the table at the bottom of the page by clicking outside it and dragging across it.
- Choose Edit ! Copy.
- Make the GuestList component active.
- Place the cursor at the bottom of the page and choose Edit ! Paste.

You have just copied the table from Main into GuestList. It has all the same properties, including the bindings. The WOStrings in the table are still bound to instance variables of __currentGuest__. Since __currentGuest__ is a component variable defined in Main, it isn't accessible from GuestList. Therefore, you need to declare it here.

- From the pull-down menu at the bottom of the window, choose Add Variable/Method. Enter currentGuest as the name of the variable and Guest as its type, and click Add.
- Choose !from the Elements pop-up list to display the Tables buttons.
- Click somewhere in the table, then click ! in the toolbar to enter structure-editing mode. (Alternatively, Control-click on the table.)
- Click one of the triangles in the second row to select the entire row.
- Choose ! to display Other WebObjects in the toolbar and click !

When you wrap a repetition around a table row in this way, the WORepetition symbol ! doesn't appear in the table. Instead, a blue border appears around the row. For additional examples of using repetitions, see [Creating a WebObjects Database Application](Creating%20a%20WebObjects%20Database%20Application.md#apple-gi3dq).

- In the object browser, select __application__ in the first column.
- In the second column, make a connection from __allGuests__ to the entire row (_not_ a WOString in a cell).

The Inspector window for that element opens. To display the WORepetition bindings click on the ! icon at the top of the inspector. The __list__ attribute is selected by default.

!

- Click Connect to bind __application.allGuests__ to the __list__ attribute.
- Bind __currentGuest__ to the repetition's __item__ attribute.

As a short cut, you can select the row for __item__, then double-click in the Binding column and type currentGuest.

By using the name __currentGuest__ for the __item__ attribute, you are taking advantage of the fact that the strings in your table are already bound to the fields of __currentGuest__.

You now have finished implementing the repetition. When the table is generated, it will have one row for each item in the __allGuests__ array.

- Save the GuestList component.
- Delete the table from the Main component, since you no longer need it.
- Build and launch your application.
- Test your application by entering data for multiple guests and verifying that each guest appears in the table.

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](Adding%20the%20Finishing%20Touches.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
