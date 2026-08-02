---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/PageComp.html
archived_at: '2026-07-15T07:46:54.240284Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](RRLoopInfo.md)

# __Page Composition__

Objects of many classes (most of them private) work together to compose the HTML content of response pages. Many of the same objects also set their variable values from data entered into request pages and respond to user actions. Two major branches of these objects descend from WOElement: WOComponent objects, which usually represent pages, and WODynamicElement objects, which represent dynamic HTML elements on the page (that is, elements with changeable state or the ability to trigger actions). For details on how this happens and for more on these classes, see "[Component and Element](ComponentElement.md#apple-kjcumnbwgy4ds)".

!

Figure 1: The Parts of a WebObjects Application

**- WOComponent**
: An object that represents a integral, reusable page (or portion of a page) for display in a web browser.

**- WOElement**
: An abstract class that declares the three request-handling methods: __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__. Each node in an object graph, which represents the HTML elements of a component and their relationships, is an object that inherits from WOElement.

**- WODynamicElement**
: An abstract class for subclasses that generate particular dynamic elements.

**- WOAssociation**
: An object that knows how to find and set a value by reference to a key. Instance variables and action methods of dynamic elements are WOAssociations.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](DBIntegration.md)
