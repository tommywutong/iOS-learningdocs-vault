---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOText.html
archived_at: '2026-07-15T08:14:39.318473Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOText

## Element Description

WOText generates a multi-line field for text input and display.
It corresponds to the HTML element `<TEXTAREA>`.

## Synopsis

WOText { value=_defaultValue_;
[name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

**value**
: During page generation, __value__ specifies
the text that is displayed in the text field. During request handling, __value__ contains
the text as the user left it.

**name**
: The name that uniquely identifies this element within
the form. You may specify a name or let WebObjects automatically
assign one at runtime.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
the text area appears in the page but is not active. That is, __value__ does
not contain the user's input when the page is submitted.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
