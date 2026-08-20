---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOSubmitButton.html
archived_at: '2026-07-15T08:14:39.278571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

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

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
