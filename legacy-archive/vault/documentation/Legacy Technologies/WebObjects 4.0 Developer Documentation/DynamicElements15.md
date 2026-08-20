---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements15.html
archived_at: '2026-07-18T01:25:39.618650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements14.md)

## Repetitions

A repetition (WORepetition) is a container element that repeats its contents a certain number of times. It is like a loop in a structured programming language. Repetitions are one of the most important elements in WebObjects, since it is quite common for applications to display repeated data (often from databases) when the amount of data to be displayed isn't known until run time. Typically, a repetition is used to generate items in a list, multiple rows in a table, or multiple tables.
To create a repetition:

- Click !.

The repetition appears in the component window.

!

- Add elements inside the repetition (replacing the word "Repetition").

A repetition can contain any other elements, either static HTML or dynamic WebObjects elements.

- Alternatively, you can select existing elements, then click ! to wrap the repetition around the elements. This is necessary in some cases, such as wrapping a repetition around a table row.

You usually bind two attributes of a repetition: __list__ and __item__. The __list__ attribute must be bound to an array. WebObjects generates the elements in the repetition once for each item in the array. Each time through the array, the __item__ attribute points to the current array object. Typically, you bind __item__ to a variable and then use that variable in the bindings of the elements inside the repetition.
When you drag an item from the object browser to the WORepetition to bind it, the default attribute shown in the Inspector depends on whether the item is an array. If it is, __list__ is the default attribute; otherwise, __item__ is the default attribute.
In addition, as with WOStrings, WebObjects Builder provides a shortcut for binding repetitions so that you don't have to use the Inspector. Drag to the first binding box to bind the __list__ attribute; drag to the second box to bind the __item__ attribute.
When you wrap a repetition around a table row, the repetition symbol doesn't appear. Instead, a shaded background appears behind the row. To bind the repetition, drag from the object browser to anywhere in the row (but not to a dynamic element inside the row). The Inspector appears, allowing you to complete the binding as usual.

!

__Note:__ You can also wrap a repetition around a single cell in a table. In addition, this same procedure of wrapping a repetition around a table row or cell also works for conditionals (see next section).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements16.md)
