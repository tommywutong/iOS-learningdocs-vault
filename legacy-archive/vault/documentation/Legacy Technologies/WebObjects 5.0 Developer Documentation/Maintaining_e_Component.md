---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/Maintaining_e_Component.html
archived_at: '2026-07-15T08:12:53.284914Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Response_Generation.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

## Maintaining State in the Component

Understanding the connection between a component and its Java
class file is an important part of WebObjects development. Not only
do you associate methods with the component to create dynamic content
in this fashion, but you can also use the methods provided by the
WOComponent class to maintain state for a component.

When you add methods to a component in WebObjects Builder,
you are actually editing the component's Java file. When you modify
how the component looks or add display elements, you are editing
HTML code. A WebObjects component is a high-level view of both the
HTML code and the Java class that describe a Web page, or part of
one. After using WebObjects Builder to define the major parts of
a component, you can add details by editing the HTML code manually
and by modifying its Java file.

When your application runs, components are instantiated as
needed. That is, each component is also an object in your application.
For example, when the DateDisplay application launches, a Main object
is created. As the component's content is determined by WebObjects,
methods in Main.java are used to provide
the data for its dynamic elements, in this case the WOString that
displays the current time. When it's time for WebObjects to add
the content for the WOString, it looks up the element's `value` binding. In
the example, `value` is
bound to the `currentTime` method.
WebObjects then invokes the currentTime method,
which returns the current time.

An instance of a component "survives" at least for two
cycles of the request-response loop: in the first cycle the page
is rendered while in the second cycle the component determines which
component to display next. If the component to be displayed is different
from the first one, the latter is discarded while an instance of
the new component is created. However, if the component to display
is the same one, then the instance "lives on." You can use instance
variables in your component's class to store information and keep
track of the user's behavior as she interacts with your application.

In this case, you'll add a variable to the Main component
and add code to increment it each time the page is displayed. You
can use this variable to show the number times the page has been
loaded by a specific user in the __session__.

To keep track of the number of times the `currentTime` method
has been called, you need to add an integer instance variable to
the Main.java file, increment it each time
the page is loaded, and add a means of telling the page to refresh
itself.

### Adding the Variable to Count Method Calls

1. Open `Main.wo` in
   WebObjects Builder (if it's not already open) by double-clicking
   it in Project Builder's main window.
2. Choose Add Key from the Edit Source menu at the bottom-left
   corner of the `Main.wo` window.
3. Add a key of type `int` named `loadCount`.
   ![[image: ../Art/dynamicaddkey.gif]](../Art/dynamicaddkey.gif)
4. Examine the Java file in Project Builder to confirm that the
   variable was added.

   ```
   public class Main extends WOComponent {
       protected int loadCount;
   ```

### Displaying the Count

To display the load count on the component, you need to add
another WOString to the component.

1. Add a label
   and a WOString to the component.
   1. Enter "`Page
      load count:` " below the line that displays
      the current time.
   2. Add a WOString to the right of the label.
2. Bind the `loadCount` variable
   to the new WOString's `value` attribute.

 ![[image: ../Art/wobdatedisplaycount.gif]](../Art/wobdatedisplaycount.gif)

### Increasing the Variable's Value

Modify the `currentTime` method
so it increments the `loadCount` variable
each time it is called. Since WebObjects calls the method each time
the page needs to be displayed, `loadCount` is
increased by one each time.

```
public NSTimestamp currentTime() {
    loadCount++;
    return new NSTimestamp();
}
```


### Refreshing the Page

Finally, you need to add a way to reload the page. In WebObjects,
regular hyperlinks (WOHyperlinks) can call Java methods on your
components. Action methods are covered in greater detail in ["Request Processing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iRequest_Processing.html).
For now, you only need to add a method that simply reloads the current
page.

1. Add the action
   method.

   Open the Main component in WebObjects Builder and choose
   Add Action from the Edit Source menu.

   1. Name the action `refreshTime`.
   2. Select `null` from
      the "Page returned" pop-up menu.

      The value returned by
      an action method represents the next page (component) to be displayed.
      When you return `null`,
      the current page is redrawn. In a later task, you learn how to return
      a new component.
   3. Click Add.
    ![[image: ../Art/dynamicaddaction.gif]](../Art/dynamicaddaction.gif)
2. Add a hyperlink.

   Position the cursor below the line where
   the load count is displayed.

   Choose WebObjects >
   WOHyperlink, or click ![[image: ../Art/wohyperlinkbtn.gif]](../Art/wohyperlinkbtn.gif)
   .

   By
   default, the text for a new link is "Hyperlink". You can replace
   this by selecting the text and typing something more appropriate
   over it, such as `"Refresh Time"`.
3. Connect the `refreshTime` method
   to the WOHyperlink.

   Much like a WOString, a WOHyperlink has
   several attributes. In this case, you bind the refreshTime method
   to the `action` attribute
   of the WOHyperlink.

    ![[image: ../Art/dynamicbindaction.gif]](../Art/dynamicbindaction.gif)

   Drag from the `refreshTime` method
   in the Main list to the WOHyperlink. When you release the mouse
   button, you will see a pop-up list of attributes. Choose the `action` attribute
   to indicate that you want the `refreshTime` method
   called when the link is clicked.
4. Save `Main.wo`.

### The Counter in Action

Build and run the DateDisplay application. When your browser
loads the page, you'll see that the counter has been increased
to 1. If you click Refresh Page, the time and the load count are
updated.

 ![[image: ../Art/iedatedisplayloadcount.gif]](../Art/iedatedisplayloadcount.gif)

This same counter instance variable is increased by one each
time you use the link because WebObjects created a Main object and
associated it with your browser window. Each time you interact with
the application, by clicking Refresh Page, the same object is used.
If you open another browser window and connect to the application
again using the URL shown in Project Builder's Run pane, a separate
instance of Main is created and associated with that window. From
then on you can work with both windows individually. As a matter
of fact, not only is a new instance of Main created, a new Session
object is created as well.

WebObjects determines that a new Session object needs to be
created when the incoming URL does not contain a session ID. The
first time you connect to the application using a URL like the one
in [Listing 4-2](#apple-ijauurkiifbum), WebObjects
creates a Session object and assigns it a session ID and other information.
That information is added to the URL returned to your browser together
with the Web page to be displayed (see [Listing 4-3](#apple-ijauuskfjbbum)). When you send another request
from your browser (by clicking Refresh Page, for example) WebObjects
uses the session ID encoded in the URL to locate the Session object
that is to process the request. This is the default mechanism WebObjects
uses to keep track of the state of each user. For more on state
management see ["Client-Server Applications"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/Introduction/iWebObjects_Features.html).

__Listing
4-2 URL that generates a new Session object__

```
http://foo.com:49361/cgi-bin/WebObjects/DateDisplay
```


__Listing
4-3 URL with session ID__

```
http://foo.com:49361/cgi-bin/WebObjects/DateDisplay.woa/wo/whcV5sauLNtG8Tfh6xCuvM/ 0.1
```

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Response_Generation.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
