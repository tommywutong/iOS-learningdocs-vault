---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOPasswordField.html
archived_at: '2026-07-15T07:49:42.778437Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOJavaScript.md)

---

# __WOPasswordField__

### Synopsis

__WOPasswordField__ __{__ __value__=_`defaultValue`___;__ [ __name__=_`fieldName`___;__] [__disabled__ =YES|NO__;__] ... __};

### Description__

A WOPasswordField represents itself as a text field that doesn't echo the characters that a user enters. It corresponds to the HTML element <INPUT TYPE="PASSWORD"...>.

**__value__**
: During page generation, value sets the default value of the text field. This value is not displayed to the user. During request handling, value holds the value the user entered into the field, or the default value if the user left the field untouched.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOPopUpButton.md)
