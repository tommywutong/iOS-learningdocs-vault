---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/DynElem.book.html
archived_at: '2026-07-15T07:50:27.971483Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../WOBuilderTOC.md)

Using Dynamic Elements in WebObjects Builder

# Using Dynamic Elements in WebObjects Builder

A dynamic element is an element that is replaced with dynamically generated HTML when the application runs. For example, WOString specifies a dynamic string element---the actual string it displays is determined at run time.

For a dynamic element to be fully functional, you must create the element and then bind it to some value. Usually, this value is a variable in a script file. If you bind the element to a variable, you must then write a script that sets the value of the variable (see "[Writing WebScript in WebObjects Builder](../Script/Script.book.md)").

**Creating dynamic elements**
: [Form-based elements](CreateForms.md)

[Abstract elements](CreateAbstractElements.md)

[Reusing components](ReuseComponents.md)

**[Binding Elements](BindElements.md#apple-kjcumnbxgq3dk)**
: [Using Inspector](BindInInspector.md)

[WOConditional](CreateWOConditional.md)

[WOHyperlink](CreateWOHyperlink.md)

[WORepetition](CreateWORepetition.md)

[Custom Element](CustomElement.md)

[Displaying Bindings](DisplayBindings.md#apple-kjcumnjtga4to): [Undoing a Binding](UndoBinding.md#apple-kjcummrwha4dg)

**[Resizing Elements](ResizeElements.md#apple-kjcumnzsgyztq)**

For more information on dynamic elements, see the chapter "[How WebObjects Works](../../DevGuide/HowWOWorks/HowWOWorks.md)" in the _WebObjects Developer's Guide_. Or look up individual dynamic elements in the [Dynamic Elements](../../Reference/DynamicElements/DynamicElements.book.md) section of the _WebObjects Reference_ to learn more about them.

[!First Section](CreateForms.md)
