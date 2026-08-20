---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/Managing_User_Input.html
archived_at: '2026-07-15T08:13:34.297286Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/iFurther_Exploration.html)[![Next](attachments/DiscoveringWO/Images/next.gif)](Request_Processing.md)

# Managing User Input

WebObjects's ability to dynamically display
information is sufficient for some Web applications, but most require
more complex interaction with the user.

WebObjects provides a system for associating display and user
input elements on a Web page with your Java variables and methods.
You've seen how easy it is to display your dynamic data in Web
pages. In this chapter, you learn how to take data from your application's
users.

In this chapter, you

- learn the
  system WebObjects uses to take in user input
- take input from the user via form elements like WOForm and
  WOTextField
- use WOConditionals for the conditional display of elements
- learn to construct derived properties with custom logic

User input in WebObjects is based on the basic HTML input
elements—forms, text input fields, and so on. Connecting these
elements to variables and methods is very similar to the process
used to bind the `value` attribute
of WOStrings.

You place components that mirror HTML form elements into your
components. These components use your Java code to generate HTML
code that Web browsers can interpret and display, and are programmed
to translate user inputs or selections back into Java variables.
The system by which values are taken from these elements and communicated to
your Java code is called request processing.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/iFurther_Exploration.html)[![Next](attachments/DiscoveringWO/Images/next.gif)](Request_Processing.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
