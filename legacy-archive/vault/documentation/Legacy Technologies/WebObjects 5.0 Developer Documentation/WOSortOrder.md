---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOSortOrder.html
archived_at: '2026-07-15T08:14:43.711055Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOSortOrder

## Component Description

A WOSortOrder component enables the user to sort the objects
displayed by a WODisplayGroup. It displays an icon representing
the current sorting order (![[image: Art/WOExtWOSOUnordered.gif]](Art/WOExtWOSOUnordered.gif)
unsorted, ![[image: Art/WOExtWOSOAscending.gif]](Art/WOExtWOSOAscending.gif)
ascending,
or ![[image: Art/WOExtWOSODescending.gif]](Art/WOExtWOSODescending.gif)
descending.) When
the user clicks the icon, the component modifies the display group's
sort orderings and redisplays the display group's objects.

## Synopsis

WOSortOrder { displayGroup=_aDisplayGroup_;
key=_aString_; [displayKey=_aString_;]
};

## Bindings

**displayGroup**
: The display group that receives the new sort order specification.

**key**
: The key corresponding to the attribute to sort by.

**displayKey**
: A user presentable string corresponding to `key`.
The user's browser displays a tooltip above the sort order icon:
"Push to toggle sorting order according to _displayKey_."
Defaults to `key`.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
