---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/BindInInspector.html
archived_at: '2026-07-15T07:50:20.385679Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](BindElements.md)

Binding Elements Using the Inspector

# Binding Elements Using the Inspector

Select the element.

Select a variable or method in the object browser.

In the bindings inspector, select the attribute you want to bind to. (Click the inspector button to display the [inspector window](../HTMLEdit/Inspectors.md).)

Click the Current Variable button.

_OR:_

Select the element.

In the bindings inspector, select the attribute you want to bind to.

Type a value in the inspector's text field. __Note:__ If the value is a string constant, you must put it in quotation marks.

Press Connect.

!

Usually, you don't need to use the inspector window to bind elements. Instead you can just select the element and double-click a variable. See "[Binding Elements](BindElements.md#apple-kjcumnbxgq3dk)" for more information on how this works and for a list of cases where you might need to bind using the inspector.

Sometimes, it's difficult to select the element you want to bind. For example, if you have a WORepetition that surrounds a table row, the WORepetition doesn't appear in the component window, and you can't select it. In this case, you can select the table row and then use the inspector's icon path to navigate to the WORepetition's bindings inspector. See "[Selecting Elements](../HTMLEdit/SelectElements.md)" for more information.

[!Table of Contents](DynElem.book.md)
[!Next Section](DisplayBindings.md)
