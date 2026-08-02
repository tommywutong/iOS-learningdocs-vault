---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOPasswordField.html
archived_at: '2026-07-15T08:14:39.132007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOPasswordField

## Element Description

A WOPasswordField represents itself as a text field that doesn't
echo the characters that a user enters. It corresponds to the HTML
element `<INPUT TYPE="PASSWORD"...>`.

## Synopsis

WOPasswordField { value=_defaultValue_;
[name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

**value**
: During page generation, __value__ sets
the default value of the text field. This value is not displayed
to the user. During request handling, __value__ holds
the value the user entered into the field, or the default value
if the user left the field untouched.

**name**
: This name uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
the element appears in the page but is not active. That is, __value__ does
not contain the user's input when the page is submitted.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
