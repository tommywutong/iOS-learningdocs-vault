---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOText.html
archived_at: '2026-07-15T07:55:36.955945Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOSwitchComponent.md)

## WOText

### Synopsis

__WOText {__ __value__=_defaultValue___;__ [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WOText generates a multi-line field for text input and display. It corresponds to the HTML element <TEXTAREA>.

**__value__**
: During page generation, __value__ specifies the text that is displayed in the text field. During request handling, __value__ contains the text as the user left it.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the text area appears in the page but is not active. That is, __value__ does not contain the user's input when the page is submitted.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOTextField.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
