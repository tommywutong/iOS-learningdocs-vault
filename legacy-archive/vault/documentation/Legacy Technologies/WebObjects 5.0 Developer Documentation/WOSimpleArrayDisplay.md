---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOSimpleArrayDisplay.html
archived_at: '2026-07-15T08:14:42.960070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOSimpleArrayDisplay

## Component Description

The WOSimpleArrayDisplay component displays some or all of
an array's objects in a single-column table. If the WOSimpleArrayDisplay
component does not display all of the objects in the array, it displays
a hyperlink with the text `More... (`_x_ `items)`,
which can be linked to a page that displays all of the objects.

![[image: Art/WOExtWOSAD.gif]](Art/WOExtWOSAD.gif)

## Synopsis

WOSimpleArrayDisplay {list=_anArray_;
itemDisplayKey=_aString_; [numberToDisplay=_aNumber_;]
listAction=_aMethod_;
[listActionString=_aString_;] };

## Bindings

**list**
: Array of objects to display.

**itemDisplayKey**
: The key for the displayed attribute of the array's
objects. For example, `roleName`.
If the objects are strings, use `description`.

**numberToDisplay**
: The maximum number of objects to be displayed (defaults
to 5.) If the number of objects exceeds this number, a hyperlink
is displayed.

**listAction**
: The action method that is called when the user clicks
the hyperlink that the component displays when the number of objects
exceeds `numberToDisplay`.

**listActionString**
: This string is appended to the `More
(`_x_ `items)` hyperlink
text that the component displays when the number of objects exceeds `numberToDisplay`.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
