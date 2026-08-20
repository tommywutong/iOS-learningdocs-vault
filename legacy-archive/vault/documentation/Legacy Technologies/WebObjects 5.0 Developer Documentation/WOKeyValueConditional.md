---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOKeyValueConditional.html
archived_at: '2026-07-15T08:14:42.852227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOKeyValueConditional

## Component Description

A WOKeyValueConditional component displays its contents (that
is, everything between the `<WEBOBJECT...>` and `</WEBOBJECT...>` tags
in the template file) if the result of the parent component's __valueForKey__ method
matches a particular value. Raises an exception if the parent component's dictionary
does not contain `key`.
This component is very similar to the WOConditional dynamic element
and is usually used in conjunction with the [WOTabPanel](WOTabPanel.md#apple-indekqskifdec) component.

## Synopsis

WOKeyValueConditional { key=_aString_;
value=_anObject_; };

## Bindings

**key**
: The key whose value is compared.

**value**
: The value that must match the result of the parent's __valueForKey__ method.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
