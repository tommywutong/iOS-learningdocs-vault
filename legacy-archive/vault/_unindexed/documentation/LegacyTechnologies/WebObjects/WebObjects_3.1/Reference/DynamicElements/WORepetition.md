---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WORepetition.html
archived_at: '2026-07-15T07:49:44.198894Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WORadioButton.md)

---

# __WORepetition__

### Synopsis

__WORepetition__ __{list__=_`anObjectList`___;__ __item__=_`anIteratedObject`___;__ [__index__=_`aNumber`_;] [__identifier__=_`aString`___;__] ... __};__

__WORepetition__ __{count__=_`aNumber`___;__ [__index__=_`aNumber`___;__] ... __};

### Description__

A WORepetition is a container element that repeats its contents (that is, everything between the <WEBOBJECT...> and </WEBOBJECT...> tags in the template file) a given number of times. You can use a WORepetition to create dynamically generated ordered and unordered lists or banks of check boxes or radio buttons.

**__list__**
: Array of objects that the WORepetition will iterate through.

**__item__**
: Current item in the list array.

**__index__**
: Index of the current iteration of the WORepetition.

**__identifier__**
: Value used to uniquely identify this item in the list array. Typically it is the primary key of an enterprise object.

**__count__**
: Number of times this element will repeat its contents.

### Examples

[Nested lists](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=RepetitionEx1)

[Radio buttons](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=RepetitionEx2)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOResetButton.md)
