---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOTextField.html
archived_at: '2026-07-15T07:49:47.253060Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOText.md)

---

# __WOTextField__

### Synopsis

__WOTextField__ __{__ __value__=_`aValue`___;__ [__dateformat__=_`dateFormatString`_;] [__numberformat__=_`numberFormatString`___;__] [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

A WOTextField represents itself as a text input field. It corresponds to the HTML element <INPUT TYPE="TEXT"...>.

**__value__**
: During page generation, __value__ sets the default value displayed in the single-line text field. During request handling, it holds the value the user entered into the field, or the default value if the user left the field untouched.

**__dateformat__**
: A format string that specifies how __value__ should be formatted as a date. If a date format is used, __value__ must be assigned an NSCalendarDate object. If __value__ can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSCalendarDate class specification for a description of the date format syntax.

**__numberformat__**
: A format string that specifies how __value__ should be formatted as a number. If a number format is used, __value__ must be assigned an NSDecimalNumber object. If the element's value can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSNumberFormatter class specification for a description of the number format syntax.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active.

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOVBScript.md)
