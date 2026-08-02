---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/CreateWORepetition.html
archived_at: '2026-07-15T07:50:25.886107Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](CreateWOHyperlink.md)

Binding to WORepetitions

# Binding to WORepetitions

Select the WORepetition.

Double-click an array variable in the object browser.

!

[WORepetition](../../Reference/DynamicElements/WORepetition.md) has two attributes that you must bind to: __list__ and __item__. The __list__ attribute must be bound to an array. The __item__ attribute is bound automatically when you bind the __list__ attribute.

A WORepetition is like a loop in a structured programming language. It uses __item__ to iterate through the __list__. Creating a WORepetition is equivalent to saying "for each __item__ in the array __list__, display the contents."

__Tip:__ It's common to use WORepetitions with tables. To learn how to bind a WORepetition that has a table row as its contents, see "[Binding Elements Using the Inspector](BindInInspector.md#apple-kjcumobtha3tm)."

[!Table of Contents](DynElem.book.md)
[!Next Section](CreateWOConditional.md)
