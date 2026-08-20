---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/PageComp.html
archived_at: '2026-07-15T07:51:49.941340Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](RRLoopInfo.md)

## Page Level

At the page level, objects of many classes (most of them private) work together to compose the HTML content of response pages (see [Figure 17](#apple-gi3tama)). Many of the same objects also set their variable values from data entered into request pages and respond to user actions.

!Figure 17. Request-Response Loop: Page Level
Two major branches of these objects descend from WOElement: WOComponent objects, which represent components, and WODynamicElement objects, which represent dynamic HTML elements on the page. For details on how this happens and for more on these classes, see ["How HTML Pages Are Generated"](ComponentElement.md#apple-gy2dsmq).

Four classes are involved at this level:

- WOComponent (in Java, Component)

Represents a integral, reusable page (or portion of a page) for display in a web browser.

- WOElement (in Java, Element)

Declares the three request-handling methods: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__. WOElement is an abstract class. Each node in an object graph, which represents the HTML elements of a component and their relationships, is an object that inherits from WOElement.

- WODynamicElement (in Java, DynamicElement)

An abstract class for subclasses that generate particular dynamic elements.

- WOAssociation (in Java, Association)

Knows how to find and set a value by reference to a key. Instance variables and action methods of dynamic elements are instances of this class.

[!Table of Contents](HowWOWorks.md) [!Next Section](DBIntegration.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
