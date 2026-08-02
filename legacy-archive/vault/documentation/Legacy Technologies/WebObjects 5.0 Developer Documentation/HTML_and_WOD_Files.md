---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/HTML_and_WOD_Files.html
archived_at: '2026-07-15T08:12:53.259618Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Main_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Build_and_R_Application.md)

## HTML and WOD Files

The connection you just made on the WOString element is implemented
in the WOD file. You can examine the HTML code and WOD files in
Project Builder, within the `Main.wo` subgroup.

In the HTML file, the `<WEBOBJECT>` tag
after your static text represents the location where the WOString
inserts the value returned from your method. This is a simple behavior,
but some WebObjects elements offer much more complex logic.

```
<BODY BGCOLOR=#FFFFFF>
    The current time is <WEBOBJECT NAME=String1></WEBOBJECT>
</BODY>
```

Notice that the tag reads `<WEBOBJECT
NAME=String1>`. The only entry in the WOD
file has the same name.

__Listing
4-1 WOString's value binding to the currentTime
method in Main.wod__

```
String1: WOString {
    value = currentTime;
}
```

The entry has only one listed binding: the connection between
the `value` attribute and
the `currentTime` method. This method is
called whenever the WOString needs to determine what value to display.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Main_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Build_and_R_Application.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
