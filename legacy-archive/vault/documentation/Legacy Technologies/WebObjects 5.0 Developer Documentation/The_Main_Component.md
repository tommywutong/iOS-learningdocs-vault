---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/The_Main_Component.html
archived_at: '2026-07-15T08:12:56.264028Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Components_and_Classes.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](HTML_and_WOD_Files.md)

## The Main Component

By default, every WebObjects application includes a Main component.
This component, initially empty, is the first page displayed to
users unless you arrange otherwise. It can be used as the login
page for the rest of your application.

The initial Main component is entirely empty. In this section,
you add a method that calculates the date to the Java class, add
a WOElement to the page, and use the WOD file to bind it all together.

### Adding Java methods

First, you add a Java method to the `Main.java` file.
This method simply returns the current date when it is called.

1. Create a
   WebObjects application project and name it DateDisplay.

   For
   details on how to create a new project see ["Hello WebObjects"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/IntroductionToWO/iHello_WebObjects.html).
2. Select `Main.java` from
   the Groups & Files list in Project Builder's main window.
   ![[image: ../Art/pbdatedisplaymainjava.gif]](../Art/pbdatedisplaymainjava.gif)
3. Add the following code to the Main.java file.
   This is a public method that returns the current date using the
   NSTimestamp class.

   ```
   public NSTimestamp currentTime() {
       // by default, a new NSTimestamp object is initialized
       // to the current date and time
       return new NSTimestamp();
   }
   ```

   Notice
   that the Main class inherits from WOComponent.

   The WOComponent
   class defines dozens of methods needed by WebObjects. Many of these
   methods are introduced later in this book.
4. Save the `Main.java` file
   by choosing File > Save.

### Adding a WOString

To display dynamic text, you add a WebObjects element to the
Main component. This element is the WOString, which is used to display
dynamic string data in a page. Such strings can be the output of
a Java method that returns a String object or another object that can
be converted to a String object.

1. Open the
   Main component with WebObjects Builder by double-clicking `Main.wo` in Project
   Builder.
2. Add text and a WOString.

   Enter "`The
   current time is` " in the content editor
   in WebObjects Builder's main window.

   With the cursor
   at the end of the new text, press the Space bar and click
   ![[image: ../Art/wostringbtn.gif]](../Art/wostringbtn.gif)
   .

   ![[image: ../Art/wobdatedisplaytext.gif]](../Art/wobdatedisplaytext.gif)
3. Open the WOString Binding Inspector.

   Select the WOString
   element and click ![[image: ../Art/inspectorbutton.gif]](../Art/inspectorbutton.gif)
   .
   The WOString Binding Inspector appears.

    ![[image: ../Art/dynamicwostringinspector.gif]](../Art/dynamicwostringinspector.gif)

   If the Inspector
   appears, but doesn't look like the one shown, click the WOString
   you just inserted. The Inspector displays information about the
   element that is currently selected.

   The Inspector displays
   the attributes for WOString elements. Each of them can be set, either
   to static values or by binding them to instance variables or methods
   in your code, which provide a value at runtime.

   Notice
   that the `value` attribute
   is displayed in red. This means that this binding is required. In
   this case, the `value` attribute's
   binding produces the text that the WOString displays, and the other
   attributes affect how the string is displayed. You use this WOString
   to display the current time.
4. Bind the WOString's `value` attribute
   to the `currentTime` method.

   Notice
   that the name of the `currentTime` method
   you entered in `Main.java` is
   listed in the Main list, in the bottom-left corner of the `Main.wo` window.

   Drag
   a connection from the `currentTime` method
   to the WOString element in the content editor.

   ![[image: ../Art/wobdatedisplaydragbind.gif]](../Art/wobdatedisplaydragbind.gif)

   While
   WOString has several attributes, WebObjects Builder assumes you
   want to bind the `value` attribute
   because it's the one most commonly used in WOStrings.
5. Save `Main.wo`.

The `currentTime` method is now bound
to the WOString on the page. This connection is recorded in the
WOD file. See [Listing 4-1](HTML_and_WOD_Files.md#apple-ijauurkcjfceg).

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Components_and_Classes.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](HTML_and_WOD_Files.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
