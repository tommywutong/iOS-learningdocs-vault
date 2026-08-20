---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WONestedList.html
archived_at: '2026-07-15T07:55:29.314181Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WOCheckBoxList.md)

## WONestedList

### Synopsis

__WONestedList__ __{__ __list__=_anObjectList___;__ __item__=_anIteratedObject___;__ __value__=_displayedValue_; __sublist__ = _aSubarray___;__ __action__=_aMethod_; __selection__=_selectedValue___;__ [__index__=_aCurrentIndex___;__] [__level__=_aCurrentLevel___;__] [__isOrdered__=YES|NO__;__] [__prefix__=_prefixString___;__] [__suffix__=_suffixString___;__] ... __};__

### Description

WONestedList recursively displays a hierarchical, ordered (numbered) or unordered (bulleted) list of hyperlinks. This element is useful when you want to display hierarchical lists. When the user clicks one of the objects in the list, it is returned in __selection__ and the __action__ method is invoked.
At any point during iteration of the list, the method specified by the __sublist__ attribute returns the current list's sublist (if any), __level__ specifies the current nesting level (where the topmost level is zero), __index__ gives index of the current item within that nesting level (__item__ returns the actual item), and __isOrdered__ specifies whether the current sublist should be a numbered list or a bulleted list.

**__list__**
: Hierarchical array of objects that the WONestedList will iterate through.

**__item__**
: Current item in the list array. (This attribute's value is updated with each iteration.)

**__value__**
: String to display as a hyperlink for the current item.

**__sublist__**
: Method that returns the sublist of the current item or __nil__ if the current item is a leaf.

**__action__**
: Action method to invoke when the element is activated. This method must return a WOElement.

**__selection__**
: When the page is submitted, __selection__ contains the item that the user clicked.

**__index__**
: Index of the current iteration of the WONestedList. The index is unique to each level-that is, it starts at 0 for each sublist.

**__level__**
: Nesting level of the current iteration of the WONestedList. The topmost level is level 0.

**__isOrdered__**
: If __isOrdered__ evaluates to YES, the current sublist is rendered as an ordered list. The default is to render as an unordered list.

**__prefix__**
: An arbitrary HTML string inserted before each value.

**__suffix__**
: An arbitrary HTML string inserted after each value.

### Examples

[Nested lists](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=NestedListEx)

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WORadioButtonList.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
