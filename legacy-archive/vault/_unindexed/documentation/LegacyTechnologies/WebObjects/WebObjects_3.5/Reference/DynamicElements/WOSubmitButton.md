---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOSubmitButton.html
archived_at: '2026-07-15T07:55:35.914725Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOString.md)

## WOSubmitButton

### Synopsis

__WOSubmitButton__ __{__ __action__=_submitForm___;__ __value__=_aString___;__ [__disabled__=YES|NO__;__] [__name__=_aName___;__] ... __};__

### Description

A WOSubmitButton element generates a submit button in an HTML page. This element is used within HTML forms.

**__action__**
: Action method to invoke when the form is submitted.

**__value__**
: Title of the button.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active. That is, clicking the button does not actually submit the form.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOSwitchComponent.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
