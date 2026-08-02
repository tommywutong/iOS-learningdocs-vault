---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/Associations.html
archived_at: '2026-07-15T07:51:46.301179Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](Templates.md)

## Associations and the Current Component

A dynamic HTML element, such as a text field or a pop-up button, differs from a static HTML element, such as a heading, in that its attributes can change over a cycle of the request-response loop. These attributes can include values that determine behavior or appearance (a "disabled" attribute, for instance), values that users enter into a field, values that are returned from a method, and actions to invoke when users click or otherwise activate the element. Each dynamic element stores its attributes as instance variables of type WOAssociation (in Java, Association). WOAssociation objects know how to obtain and set the value they represent. They generally do this using key-value coding.
The key to a value can be represented as a sequence of keys separated by periods. The resolution of a key by yielding its value makes possible the resolution of the next key. For instance:

```
    self.aRepetition.list.item
```


means that __self__ (identifying the current component) has a WORepetition named __aRepetition__. The __list__ key denotes the list of elements displayed by the WORepetition, and the __item__ is the key to the current item in that list. Keys (including actions) are WOAssociations defined for each dynamic element. The values for these keys are constants assigned in the __.wod__ file, or they derive from bindings to variables, to methods, or to entities retrieved through a WODisplayGroup (for applications that access a database).
WOAssociation objects refer to the _current component_ for the initial value of this sequence. They get this object from the cycle's WOContext object. Often the current component is the request or response page of the cycle, but it can be a reusable component embedded in a page, or even a component incorporated by one of those subcomponents. See ["Subcomponents and Component References"](Subcomponents.md#apple-gy4timi) for more on this. WOContext stores the current component on a stack, "pushing" and "popping" components onto and off of the stack as necessary.

Depending on the phase of the request-response loop, a dynamic element uses its WOAssociations to "pull" values from the request (that is, set its values to what the user specifies) or to "push" its values onto the response page. When a dynamic element that can respond to user actions (such as WOSubmitButton) requests the value of its "action" WOAssociation, the appropriate action method in the current component is invoked and the response page is returned.
The exchange of data through an association that binds an attribute of a parent component to an attribute of a child component is two-way. This two-way binding allows the synchronization of state between the two components. Consider this declaration in __Main.wod__ of the TimeOff example:

```
    START:Calendar {
        selectedDate = startDate;
        callBack = "mainPage";
    };
```


In this example, Main is the parent component and Calendar is the child component. The __startDate__ variable belongs to the parent component while __selectedDate__ is a variable of the child component. A change in the parent component instance variable is automatically communicated through the association to the child variable. Conversely, a change in value in the child component variable is communicated to the parent variable. Component synchronization occurs at the beginning and end of each of the three request-handling phases of a component (__takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__). Synchronization is performed through the accessor methods of both components.
This aspect of synchronization has implications for developers. Because WebObjects invokes explicitly implemented accessor methods many times during the same request-response loop, your accessor methods must have no side effects. Instead, they should simply set a variable's value or return a value. And if they return a value, there should be some way for WebObjects to set the value.
This rule applies also when the binding involves a parent or a child component's method instead of an instance variable. To illustrate this, assume that __startDate__ is a method of the Main component instead of an instance variable. Even in this case, WebObjects attempts to synchronize __startDate__ with the __selectedDate__ value. In other words, WebObjects attempts to invoke a __setStartDate:__ method and raises an exception if such a method does not exist.
See the chapter ["Creating Reusable Components"](../Reuse/ReuseTOC.md#apple-gizdsmi) for more on state synchronization between child and parent components.

[!Table of Contents](HowWOWorks.md) [!Next Section](ClientSideAssociations.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
