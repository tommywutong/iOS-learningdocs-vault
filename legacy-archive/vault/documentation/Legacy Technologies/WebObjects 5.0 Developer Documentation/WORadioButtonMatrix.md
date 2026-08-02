---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WORadioButtonMatrix.html
archived_at: '2026-07-15T08:14:42.896846Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WORadioButtonMatrix

## Component Description

The WORadioButtonMatrix displays a multi-column array of radio
buttons based on a list of objects and allows the user to select
one of these objects. This component displays its content (everything between
the `<WEBOBJECT...>` and `</WEBOBJECT...>` tags
in the template file) for each of the items in `list` from
left to right, and wraps around to the next line when the number
of columns reaches `maxColumns`. This
component must be embedded within a WOForm.

## Synopsis

WORadioButtonMatrix { list=_anArray_;
item=_anObject_; selection=_theSelection_;
maxColunms=_aNumber_;
};

## Bindings

**list**
: Array of objects from which the radio buttons derive
their values. For example, the array could be named `movieArray` and
contain Movie objects.

**item**
: Identifier for the elements of the list. This attribute
is updated for each iteration through `list`.
For example, `currentMovie` could
represent an object in `movieArray`.

**selection**
: Object that the user chooses from the selection list.
This attribute is updated when the user submits the form containing
the WORadioButtonMatrix. For the movie example, __selection__ would
be a Movie object.

**maxColumns**
: The number of columns of radio buttons displayed.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
