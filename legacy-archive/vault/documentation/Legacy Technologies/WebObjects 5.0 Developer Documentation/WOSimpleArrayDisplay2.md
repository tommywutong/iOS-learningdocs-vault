---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOSimpleArrayDisplay2.html
archived_at: '2026-07-15T08:14:43.206414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOSimpleArrayDisplay2

## Component Description

The WOSimpleArrayDisplay2 component displays some or all of
an array's objects in a single-column table. Each object has a
hyperlink that can be used to jump to an edit page for the object.
If the WOSimpleArrayDisplay2 component does not display all of the
objects in the array, it displays an inspect image hyperlink, which
can be linked to a page that displays all of the objects.

![[image: Art/WOExtWOSAD2.gif]](Art/WOExtWOSAD2.gif)

## Synopsis

WOSimpleArrayDisplay2 {list=_anArray_;
[itemDisplayKey=_aString_;]
[numberToDisplay=_aNumber_;]
listAction=_aMethod_; [listTarget=_aString_;]
item=_anObject_;
[itemTarget=_aString_;]
displayItemAction=_aMethod_; };

## Bindings

**list**
: Array of objects to display.

**itemDisplayKey**
: The key for the displayed attribute of the array's
objects. For example, `roleName`.
Use `description` if the
objects are strings.

**numberToDisplay**
: The maximum number of objects to be displayed (defaults
to 5.) If the number of objects exceeds this number, a hyperlink
is displayed.

**listAction**
: The action method invoked when the user clicks the hyperlink
that the component displays when the number of objects exceeds `numberToDisplay`.

**item**
: The selected object. This attribute is updated when
the user clicks one of the object hyperlinks.

**listTarget**
: The target frame for the hyperlink that the component
displays when the number of objects exceeds `numberToDisplay`.

**itemTarget**
: The target frame for the object hyperlinks.

**displayItemAction**
: The action invoked when the user clicks an object hyperlink.
The item attribute contains the object.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
