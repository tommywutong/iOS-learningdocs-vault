---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOSubmitButton.html
archived_at: '2026-07-15T08:09:53.544763Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOSubmitButton

## Element Description

A WOSubmitButton element generates a submit button in an HTML
page. This element is used within HTML forms.

## Synopsis

WOSubmitButton { action=_submitForm_;
value=_aString_; [disabled=_aBoolean_;]
[name=_aName_;] ... };

## Bindings

**action**
: Action method to invoke when the form is submitted.

**value**
: Title of the button.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
the element appears in the page but is not active. That is, clicking
the button does not actually submit the form.

**name**
: Name that uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
