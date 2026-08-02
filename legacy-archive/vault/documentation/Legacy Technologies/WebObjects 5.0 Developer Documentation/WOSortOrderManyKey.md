---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOSortOrderManyKey.html
archived_at: '2026-07-15T08:14:45.286234Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOSortOrderManyKey

## Component Description

The WOSortOrderManyKey component provides a user interface
to specify the sort ordering of the objects displayed by a WODisplayGroup.
The user specifies the key on which to sort using a popup button
and the order (ascending or descending). The WOSortOrderManyKey
component updates the display group's displayed objects accordingly.
This component must be placed in a WOForm.

![[image: Art/WOExtWOSOMK.gif]](Art/WOExtWOSOMK.gif)

## Synopsis

WOSortOrderManyKey { displayGroup=_aDisplayGroup_;
keyList=_anArray_; };

## Bindings

**displayGroup**
: The display group that receives the new sorting order
specification.

**keyList**
: Array of keys for the attribute that can be used to
sort the objects. This array appears in the popup button.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
