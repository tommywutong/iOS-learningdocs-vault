---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WORadioButtonList.html
archived_at: '2026-07-15T07:55:31.287718Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WONestedList.md)

## WORadioButtonList

### Synopsis

__WORadioButtonList__ __{__ __list__=_anObjectList___;__ __item__=_anIteratedObject___;__ __value__=_displayedValue_; [__index__=_aNumber___;__] [__prefix__=_prefixString___;__] [__suffix__=_suffixString___;__] [__selection__=_selectedValue___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WORadioButtonList displays a list of radio buttons. The user may select one of the objects in the list, and this object is returned as __selection__.

**__list__**
: Array of objects that the WORadioButtonList will iterate through.

**__item__**
: Current item in the list array. (This attribute's value is updated with each iteration.)

**__value__**
: String to display beside the radio button for the current item.

**__index__**
: Index of the current iteration of the WORadioButtonList.

**__prefix__**
: An arbitrary HTML string inserted before each value.

**__suffix__**
: An arbitrary HTML string inserted after each value.

**__selection__**
: An object that the user chose from the list.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active.

### Examples

[Radio button list](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=RadioButtonListEx)

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WORedirect.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
