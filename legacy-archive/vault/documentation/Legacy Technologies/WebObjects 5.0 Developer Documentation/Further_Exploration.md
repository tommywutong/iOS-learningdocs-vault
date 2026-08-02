---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/Further_Exploration.html
archived_at: '2026-07-15T08:12:53.223834Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Maintaining_e_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/index.html)

## Further Exploration

You've learned how to use some of WebObjects's tools,
and how to add elements and bind them to your Java code using WebObjects
Builder. You also learned how to display dynamic content based on
Java code, and maintain state data from one request to the next. Feel
free to explore WebObjects Builder to learn more. Here are a few
suggested exercises:

- All the usual
  attributes of a Web page—title, background color, font size, and the
  like–can be maintained in WebObjects Builder. Make the DateDisplay
  application a bit smoother around the edges by setting the page
  title and customizing the text displayed. If a WOString is inside
  another HTML tag, the WOString is affected just like ordinary text.
- The NSTimestamp class displays as an ANSI standard date by
  default. If you examine the WOString element in the Inspector, you'll
  see a binding called `dateFormat`,
  which you can use to control how the time and date are displayed.
- What happens if the WOString that displays the value of the `loadCount` instance variable
  is placed before the WOString that displays the time (and updates `loadCount`)? WebObjects
  parses the WOStrings in the order in which they appear, so `loadCount` is
  0 the first time it is displayed.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Maintaining_e_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
