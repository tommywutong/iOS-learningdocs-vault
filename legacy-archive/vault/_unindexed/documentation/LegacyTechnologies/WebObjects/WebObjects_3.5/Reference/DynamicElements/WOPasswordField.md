---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOPasswordField.html
archived_at: '2026-07-15T07:55:29.787626Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOJavaScript.md)

## WOPasswordField

### Synopsis

__WOPasswordField__ __{__ __value__=_defaultValue___;__ [__name__=_fieldName___;__] [__disabled__ =YES|NO__;__] ... __};__

### Description

A WOPasswordField represents itself as a text field that doesn't echo the characters that a user enters. It corresponds to the HTML element <INPUT TYPE="PASSWORD"...>.

**__value__**
: During page generation, __value__ sets the default value of the text field. This value is not displayed to the user. During request handling, __value__ holds the value the user entered into the field, or the default value if the user left the field untouched.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active. That is, __value__ does not contain the user's input when the page is submitted.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOPopUpButton.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
