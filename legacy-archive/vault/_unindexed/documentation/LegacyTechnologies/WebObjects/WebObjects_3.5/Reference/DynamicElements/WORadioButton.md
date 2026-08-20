---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WORadioButton.html
archived_at: '2026-07-15T07:55:30.855665Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOPopUpButton.md)

## WORadioButton

### Synopsis

__WORadioButton__ __{value__=_defaultValue___;__ [__selection__=_selectedValue___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__
__WORadioButton__ __{checked__=YES|NO__;__ [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WORadioButton represents itself as an on-off switch. Radio buttons are normally grouped, since the most important aspect of their behavior is that they allow the user to select no more than one of several choices. If the user selects one button, the previously selected button (if any) becomes deselected.
Since radio buttons normally appear as a group, WORadioButton is commonly found within a WORepetition. Alternatively, you can use the [WORadioButtonList](WORadioButtonList.md) element in the WOExtensions framework.

**__value__**
: Value of this input element. If not specified, WebObjects provides a default value.

**__selection__**
: If __selection__ and __value__ are equal when the page is generated, the radio button is selected. When the page is submitted, __selection__ is assigned the value of the radio button.

**__checked__**
: During page generation, if __checked__ evaluates to YES, the radio button appears in the selected state. During request handling, __checked__ reflects the state the user left the radio button in: YES if checked; NO if not.

**__name__**
: Name that identifies the radio button's group. Only one radio button at a time can be selected within a group.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active. That is, __selection__ does not contain the user's selection when the page is submitted.

Note that either __checked__ or __value__ is required in a WORadioButton declaration, but that they are mutually exclusive.

### Examples

[Radio buttons](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=RepetitionEx2)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WORepetition.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
