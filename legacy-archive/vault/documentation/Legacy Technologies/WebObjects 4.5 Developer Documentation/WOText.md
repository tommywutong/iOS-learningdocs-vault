---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOText.html
archived_at: '2026-07-15T08:09:53.567042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

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

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
