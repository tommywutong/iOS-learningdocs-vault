---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOTable.html
archived_at: '2026-07-15T08:14:46.202757Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOTable

## Component Description

A WOTable is a container element similar to a WORepetition
that repeats its contents (that is, everything between the `<WEBOBJECT...>
and </WEBOBJECT...>` tags in the template
file) a given number of times. It differs from a WORepetition in
that it displays the contents as a multi-column table. You can use
a WOTable to create dynamically generated banks of check boxes or
radio buttons. The WOTable displays the items in `list` from
left to right and wraps around to the next line when the number
of columns reaches `maxColumns`.

![[image: Art/WOExtWOTable.gif]](Art/WOExtWOTable.gif)

## Synopsis

WOTable {list=_anObjectList_;
[item=_anIteratedObject_;] maxColumns=_aNumber_;
[index=_aNumber_;] [col=_aNumber_;]
[row=_aNumber_;] [tableBackgroundColor=_hexString_;]
[border=_aNumber_;] [cellpadding=_aString_;]
[cellspacing=_aString_;]
[rowBackgroundColor=_hexString_;]
[cellBackgroundColor=_hexString_;]
[cellAlign=_aString_;]
[cellVAlign=aString;] };

## Bindings

**list**
: Array of objects through which the WOTable iterates.

**item**
: Current item in the list array. (This attribute's
value is updated with each iteration.)

**maxColumns**
: Number of columns in the table.

**index**
: Index of the current iteration of the WOTable. (This
attribute's value is updated with each iteration.)

**col**
: Current column in the table. (This attribute's value
is updated with each iteration.)

**row**
: Current row in the table. (This attribute's value
is updated with each iteration.)

**tableBackgroundColor**
: Specifies the background color of the table. This attribute
is passed to the `TABLE` HTML
tag.

**border**
: Specifies the width, in pixels, of the table border.
This attribute is passed to the `TABLE` HTML tag.

**cellpadding**
: Specifies the spacing between cells of the table. This
attribute is passed to the `TABLE` HTML tag.

**cellspacing**
: Specifies the spacing within cells of the table. This
attribute is passed to the `TABLE` HTML
tag.

**rowBackgroundColor**
: Specifies the background color for each row. This attribute
is passed to each `TR` HTML
tag in the table.

**cellBackgroundColor**
: Specifies the background color for the cells. This attribute
is passed to each `TD` HTML
tag in the table.

**cellAlign**
: Specifies the horizontal alignment of each cell. This
attribute is passed to each `TD` HTML
tag in the table.

**cellVAlign**
: Specifies the vertical alignment of each cell. This
attribute is passed to each `TD` HTML
tag in the table.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
