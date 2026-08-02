---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOCheckBox.html
archived_at: '2026-07-15T08:14:38.889433Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOCheckBox

## Element Description

A WOCheckBox object displays itself in the HTML page as its
namesake, a check box user interface control. It corresponds to
the HTML element `<INPUT TYPE="CHECKBOX"...>`.

If you want to create a list of check boxes, use [WOCheckBoxList](WOCheckBoxList.md#apple-ineesr2jijbuu) instead of this element.

## Synopsis

WOCheckBox {value=_defaultValue_;
[selection=_selectedValue_;] [name=_fieldName_;] [disabled=_aBoolean_;]
... };
WOCheckBox {checked=_aBoolean_;
[name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

**value**
: Value of this input element. If not specified, WebObjects
provides a default value.

**selection**
: If selection and value are equal when the page is generated,
the check box is checked. When the page is submitted, selection
is assigned the value of the check box.

**checked**
: During page generation, if checked evaluates to `true` (or `YES`),
the check box appears in the checked state. During request handling,
checked reflects the state the user left the check box in: `true` (or `YES`)
if checked; `false` (or `NO`)
if not.

**name**
: Name that uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If disabled evaluates to `true` (or `YES`),
this element appears in the page but is not active. That is, selection
won't contain the user's selection when the page is submitted.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
