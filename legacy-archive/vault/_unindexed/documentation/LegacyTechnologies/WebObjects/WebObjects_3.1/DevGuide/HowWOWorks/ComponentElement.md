---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/ComponentElement.html
archived_at: '2026-07-15T07:46:51.697748Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](AppendToResponse.md)

# __Component and Element__

So how exactly are request-handling messages propagated from a component to its HTML elements? This question begs another: What is the relationship between component and HTML element?

Both WOComponent objects and HTML elements (static and dynamic) share a common ancestor, WOElement. WOElement declares, but does not implement, the three request-handling messages: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__. This common inheritance, of course, makes it possible for both components and HTML elements to participate in request handling. But there the inherited similarities end. Although components can generate HTML content, this capability is not a essential characteristic, as it is with objects on the other branch of the inheritance tree.

Components are reusable pages, or portions of pages, displayed in a World Wide Web browser. As with all objects, components contain a unique set of data, although the structure of that data is the same for each component instance. Through a script or compiled code, components also include logic that manipulates the data and otherwise affects behavior, especially the behavior of returning another page based on a user's request. Finally, each component is associated with a template.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](Templates.md)
