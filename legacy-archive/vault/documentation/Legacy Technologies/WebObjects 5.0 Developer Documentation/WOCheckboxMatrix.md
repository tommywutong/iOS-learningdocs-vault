---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOCheckboxMatrix.html
archived_at: '2026-07-15T08:14:40.616274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOCheckboxMatrix

## Component Description

The WOCheckboxMatrix component displays a multi-column array
of checkboxes based on a list of objects and allows the user to
select any combination of these objects. This component displays
its content (everything between the `<WEBOBJECT...>` and `</WEBOBJECT...>` tags
in the template file) for each of the items in `list` in
the same order as [WOTable](WOTable.md#apple-ijbesq2fi5cuu).
This component must be embedded within a WOForm.

## Synopsis

WOCheckBoxMatrix { list=_anArray_;
item=_anObject_; selections=_anArray_;
maxColumns=_aNumber_;
};

## Bindings

**list**
: Array of objects from which the checkboxes derive their
values. For example, the array could be named `movieArray` and
contain Movie objects.

**item**
: Identifier for the elements of the list. This attribute
is updated for each iteration through `list`.
For example, `currentMovie` could
represent an object in `movieArray`.

**selections**
: An array of objects the user chooses from the list.
This attribute is updated when the user submits the form containing
the WOCheckboxMatrix. For the movie example, `selections` array
would hold Movie objects.

**maxColumns**
: The number of columns of checkboxes displayed.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
