---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WORadioButton.html
archived_at: '2026-07-15T07:49:43.717414Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOPopUpButton.md)

---

# __WORadioButton__

### Synopsis

__WORadioButton__ __{__[__value__=_`defaultValue`___;__ [__selection__=_`selectedValue`_]]__;__ [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};__

__WORadioButton__ __{__[__checked__=YES|NO__;__] [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

WORadioButton represents itself as an on-off switch. Radio buttons are normally grouped, since the most important aspect of their behavior is that they allow the user to select no more than one of several choices. If the user selects one button, the previously selected button (if any) becomes deselected.

Since radio buttons normally appear as a group, WORadioButton is commonly found within a WORepetition.

**__checked__**
: During page generation, if __checked__ evaluates to YES, the radio button appears in the selected state. During request handling, __checked__ reflects the state the user left the radio button in: YES if checked; NO if not.

**__value__**
: Value of this input element. If not specified, WebObjects provides a default value.

**__selection__**
: If __selection__ and __value__ are equal when the page is generated, the radio button is selected. When the page is submitted, __selection__ is assigned the value of the radio button.

**__name__**
: Name that identifies the radio button's group. Only one radio button at a time can be selected within a group.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active.

Note that either __checked__ or __value__ is required in a WORadioButton declaration, but that they are mutually exclusive.

### Examples

[Radio buttons](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=RepetitionEx2)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WORepetition.md)
