---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOCheckBox.html
archived_at: '2026-07-15T07:49:37.401379Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOBrowser.md)

---

# __WOCheckBox__

### Synopsis

__WOCheckBox__ __{__[__value__=_`defaultValue`___;__ [__selection__=_`selectedValue`___;__]] [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};__

__WOCheckBox__ __{__[__checked__=YES|NO__;__] [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

A WOCheckBox object displays itself in the HTML page as its namesake, a check box user interface control. It corresponds to the HTML element <INPUT TYPE="CHECKBOX"...>.

**__value__**
: Value of this input element. If not specified, WebObjects provides a default value.

**__selection__**
: If __selection__ and __value__ are equal when the page is generated, the check box is checked. When the page is submitted, __selection__ is assigned the value of the check box.

**__checked__**
: During page generation, if __checked__ evaluates to YES, the check box appears in the checked state. During request handling, checked reflects the state the user left the check box in: YES if checked; NO if not.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOConditional.md)
