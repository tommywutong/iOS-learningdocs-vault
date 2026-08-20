---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/Response_Generation.html
archived_at: '2026-07-15T08:12:56.244566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Build_and_R_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Maintaining_e_Component.md)

## Response Generation

When you run the DateDisplay application, the page displayed
by your browser has replaced the WOString you added to the Main
component with the current date and time. If you reload the page,
the date and time changes. WebObjects assembles the page dynamically
during the request-response cycle.

When your browser requests the URL corresponding to your WebObjects
application, your __Web server__ hands control to
the WebObjects __adaptor__. This program goes through several
steps in generating the response it returns.

1. Reading the
   HTML file

   Much like a regular Web server, WebObjects first
   reads an HTML file. Unlike a regular Web server, though, WebObjects
   parses a `<WEBOBJECT>` tag
   before returning it to the Web server.
2. Merging the WOD file

   When a `<WEBOBJECT>` tag
   is encountered, the WOD file for the component is consulted. All
   the WebObjects tags in an HTML file are named, and each one is listed
   by its name in the WOD file.

   Each `<WEBOBJECT>` tag
   represents a WebObjects component. When a `<WEBOBJECT>` tag needs
   to be evaluated, the entire response generation process is invoked
   recursively on the new component, continuing as many times as necessary.
   The Main component was added to your project automatically by the
   Project Builder Assistant. You can create and use your own components
   (pages) as you'll see later in ["Defining a New Component"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iDefining_a_New_Component.html).
3. Accessing Java methods

   Each type of WebObjects component
   has special logic for constructing the HTML code to return to the
   Web server. Customization of this process is done with attributes defined
   by the component's developer. Each binding in a WOD file can be
   either static or dynamic. If a binding is static, the value supplied
   is used directly.

   If a binding is dynamic—that is,
   an attribute is bound to a Java method or instance variable—then
   WebObjects invokes the method or accesses the instance variable
   to obtain the value at runtime. In the example above, when the WOString
   is evaluated, it calls the method named in its `value` binding
   (currentTime ) to get the value to
   display. The implementation of WOString turns the NSTimestamp object
   into a string and displays it in your Web browser.

This process takes place each time your browser requests the
Main component. If you reload the page, the method is invoked again
and a new date and time value is displayed.

For more information on the request-response loop, see ["Request Processing"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iRequest_Processing.html).

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Build_and_R_Application.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Maintaining_e_Component.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
