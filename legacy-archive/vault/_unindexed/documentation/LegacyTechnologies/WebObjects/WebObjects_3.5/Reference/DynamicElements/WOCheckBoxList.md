---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOCheckBoxList.html
archived_at: '2026-07-15T07:55:23.336030Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WOExtensionsTOC.md)

## WOCheckBoxList

### Synopsis

__WOCheckBoxList__ __{__ __list__=_anObjectList___;__ __item__=_anIteratedObject___;__ __value__=_displayedValue_; [__index__=_aNumber___;__] [__prefix__=_prefixString___;__] [__suffix__=_suffixString___;__] [__selections__=_selectedValues___;__] [__name__=_fieldName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WOCheckBoxList displays a list of check boxes. The user may select several of the objects in the list, and this sublist is returned as __selections__.

**__list__**
: Array of objects that the WOCheckBoxList will iterate through.

**__item__**
: Current item in the list array. (This attribute's value is updated with each iteration.)

**__value__**
: String to display beside the check box for the current item.

**__index__**
: Index of the current iteration of the WOCheckBoxList.

**__prefix__**
: An arbitrary HTML string inserted before each value.

**__suffix__**
: An arbitrary HTML string inserted after each value.

**__selections__**
: An array of objects that the user chose from the list.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, this element appears in the page but is not active.

### Examples

[A list of options](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=CheckBoxListEx)

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WONestedList.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
