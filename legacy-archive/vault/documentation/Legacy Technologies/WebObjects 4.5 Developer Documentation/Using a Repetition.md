---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.21.html
archived_at: '2026-07-15T08:07:21.134717Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Enhancing%20Your%20Application.md) [!](Adding%20a%20Second%20Component.md) [!](Adding%20the%20Finishing%20Touches.md)

---

#  Using a Repetition

Now you'll create a table to display the entire list of guests in the GuestList component. To do so, you'll use a dynamic element called a _repetition_ (an instance of the WORepetition class). Repetitions are one of the most important elements in WebObjects, since it is quite common for applications to display repeated data (often from databases) when the amount of data to be displayed isn't known until runtime. Typically, a repetition is used to generate items in a list or a browser, multiple rows in a table, or multiple tables.

A repetition can contain any other elements--either static HTML or dynamic WebObjects elements. In the GuestList component, you'll create a repetition that contains a table row.

You'll bind the __allGuests__ array to the WORepetition's __list__ attribute. This tells WebObjects to generate the elements in the repetition once for each item in the array. Each time WebObjects iterates through the array, it sets the repetition's __item__ attribute to the current array object. You bind __item__ to the variable __currentGuest__ and use __currentGuest__'s fields to bind the elements inside the repetition (such as WOStrings). At runtime, the table will consist of one row (displaying name, e-mail address, and comments) for each guest.

1. 

   In WebObjects Builder, make the Main component window active (double-click __Main.wo__).
2. 

   Select the table at the bottom of the page by pressing outside it and dragging across it.
3. 

   Choose Edit ! Copy.
4. 

   Make the GuestList component active.
5. 

   Place the cursor at the bottom of the page and choose Edit ! Paste.

   You have just copied the table from Main into GuestList. It has all the same properties, including the bindings. The WOStrings in the table are still bound to instance variables of __currentGuest__. Since __currentGuest__ is a component variable defined in Main, it isn't accessible from GuestList. Therefore, you need to declare it here.
6. 

   From the pull-down list at the bottom of the window, choose Add Key. Enter currentGuest as the name of the variable and Guest as its type, and click Add.
7. 

   Click in one of the cells in the second row. Click <TR> in the path view to select the entire row.!
8. 

   Click ! in the toolbar.

   When you wrap a repetition around a table row in this way, the WORepetition symbol ! doesn't appear in the table. Instead, the row appears in blue. For additional examples of using repetitions, see Chapter 3, [Creating a WebObjects Database Application](Creating%20a%20WebObjects%20Database%20Application.md#apple-gmztkmzq)
   .
9. 

   In the object browser, select __application__ in the first column.
10. 

    In the second column, make a connection from __allGuests__ to the <WORepetition> tag in the path view.
11. 

    In the attribute menu that appears, click __list__. This binds __application.allGuests__ to the WORepetition's __list__ attribute.!
12. 

    Bind __currentGuest__ to the repetition's __item__ attribute.

    By using the name __currentGuest__ for the __item__ attribute, you are taking advantage of the fact that the strings in your table are already bound to the fields of __currentGuest__.

    You now have finished implementing the repetition. When the table is generated, it will have one row for each item in the __allGuests__ array.
13. 

    Save the GuestList component.
14. 

    Delete the table from the Main component, since you no longer need it.
15. 

    Test your application.

    __Note:__ In this case, you don't have to rebuild or relaunch your application in order to test it. Building is required only when you have made changes to Java or Objective-C code. If you modify a component or WebScript code only, the changes take effect even if the application is already running.
16. 

    Try entering data for multiple guests and verifying that each guest appears in the table.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Enhancing%20Your%20Application.md) [!](Adding%20a%20Second%20Component.md) [!](Adding%20the%20Finishing%20Touches.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
