---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOTextField.html
archived_at: '2026-07-15T07:55:37.484052Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOText.md)

## WOTextField

### Synopsis

__WOTextField__ __{__ __value__=_aValue___;__ [__dateformat__=_dateFormatString_;] [__numberformat__=_numberFormatString___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

A WOTextField represents itself as a text input field. It corresponds to the HTML element <INPUT TYPE="TEXT"...>.

**__value__**
: During page generation, __value__ sets the default value displayed in the single-line text field. During request handling, it holds the value the user entered into the field, or the default value if the user left the field untouched.

**__dateformat__**
: A format string that specifies how __value__ should be formatted as a date. If a date format is used, __value__ must be assigned an NSCalendarDate object. If __value__ can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSCalendarDate class specification for a description of the date format syntax.

**__numberformat__**
: A format string that specifies how __value__ should be formatted as a number. If a number format is used, __value__ must be assigned an NSNumber object. If the element's value can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSNumberFormatter class specification for a description of the number format syntax.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active. That is, __value__ does not contain the user's input when the page is submitted.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOVBScript.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
