---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOHiddenField.html
archived_at: '2026-07-15T08:09:53.308187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOHiddenField

## Element Description

A WOHiddenField adds hidden text to the HTML page. It corresponds
to the HTML element `<INPUT TYPE="HIDDEN"...>`.
Hidden fields are sometimes used to store application state data
in the HTML page. In WebObjects, the WOStateStorage element is designed
expressly for this purpose.

## Synopsis

WOHiddenField { value=_defaultValue_;
[ name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

**value**
: Value for the hidden text field.

**name**
: Name that uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If disabled evaluates to `true` (or `YES`),
the element appears in the page but is not active.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
