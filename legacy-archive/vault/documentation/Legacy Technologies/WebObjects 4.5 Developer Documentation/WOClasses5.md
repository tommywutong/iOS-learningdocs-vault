---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses5.html
archived_at: '2026-07-15T08:06:21.637854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses4.md)

## Page Level

At the page level, objects of many classes (most of them private) work together to compose the HTML content of response pages (see [Figure 18](#apple-gi3tama)). Many of the same objects also set their variable values from data entered into request pages and respond to user actions.

!

Figure 18. Request-Response Loop: Page Level

Two major branches of these objects descend from WOElement: WOComponent objects, which represent components, and WODynamicElement objects, which represent dynamic HTML elements on the page. For details on how this happens and for more on these classes, see ["How HTML Pages Are Generated"](How%20HTML%20Pages%20Are%20Generated.md#apple-haytioa).

Four classes are involved at this level. Of these four, most developers only interact with WOComponent.

- WOComponent

Represents an integral, reusable page (or portion of a page) for display in a web browser.

- WOElement

Declares the three component action request-handling methods: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__. WOElement is an abstract class. Each node in an object graph, which represents the HTML elements of a component and their relationships, is an object that inherits from WOElement.

- WODynamicElement

An abstract class for subclasses that generate particular dynamic elements.

- WOAssociation

Knows how to find and set a value by reference to a key. WODynamicElement objects generally have WOAssociation instance variables.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses6.md)
