---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses19.html
archived_at: '2026-07-15T08:06:15.620499Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses18.md)

# How HTML Pages Are Generated

So how exactly are request-handling messages propagated from a component to its HTML elements? To answer this, we must understand the relationship between a component and an HTML element.
Both components and HTML elements (static and dynamic) share a common ancestor, WOElement. WOElement declares, but does not implement, the three component action request-handling messages: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__. This common inheritance, of course, makes it possible for both components and HTML elements to participate in request handling. But there the inherited similarities end. Although components can generate HTML content, this capability is not an essential characteristic, as it is with objects on the other branch of the inheritance tree.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses20.md)
