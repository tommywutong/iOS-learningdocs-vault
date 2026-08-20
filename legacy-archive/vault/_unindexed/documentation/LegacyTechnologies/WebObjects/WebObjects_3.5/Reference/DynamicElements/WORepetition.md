---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WORepetition.html
archived_at: '2026-07-15T07:55:32.582202Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WORadioButton.md)

## WORepetition

### Synopsis

__WORepetition__ __{list__=_anObjectList___;__ __item__=_anIteratedObject___;__ [__index__=_aNumber_;] [__identifier__=_aString___;__] ... __};__
__WORepetition__ __{count__=_aNumber___;__ [__index__=_aNumber___;__] ... __};__

### Description

A WORepetition is a container element that repeats its contents (that is, everything between the <WEBOBJECT...> and </WEBOBJECT...> tags in the template file) a given number of times. You can use a WORepetition to create dynamically generated ordered and unordered lists or banks of check boxes or radio buttons.

**__list__**
: Array of objects that the WORepetition will iterate through.

**__item__**
: Current item in the list array. (This attribute's value is updated with each iteration.)

**__index__**
: Index of the current iteration of the WORepetition.

**__identifier__**
: Value used to uniquely identify this item in the list array. Typically it is the primary key of an enterprise object.

**__count__**
: Number of times this element will repeat its contents.

### Examples

[Nested lists](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=RepetitionEx1)

[Radio buttons](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=RepetitionEx2)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOResetButton.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
