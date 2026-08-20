---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses21.html
archived_at: '2026-07-15T08:06:18.161980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses20.md)

## Associations and the Current Component

A dynamic HTML element, such as a text field or a pop-up button, differs from a static HTML element, such as a heading, in that its attributes can change over a cycle of the request-response loop. These attributes can include values that determine behavior or appearance (a "disabled" attribute, for instance), values that users enter into a field, values that are returned from a method, and actions to invoke when users click or otherwise activate the element. Each dynamic element stores its attributes as instance variables of type WOAssociation. WOAssociation objects know how to obtain and set the value they represent. They generally do this using key-value coding.
Keys (including actions) are WOAssociations defined for each dynamic element. The values for these keys are constants assigned in the __.wod__ file, or they derive from bindings to variables, to methods, or to entities retrieved through a WODisplayGroup (for applications that access a database).
WOAssociation objects refer to the _current component_ for the initial value of this sequence. They get this object from the cycle's WOContext object. Often the current component is the request or response page of the cycle, but it can be a reusable component embedded in a page, or even a component incorporated by one of those subcomponents. See ["Subcomponents and Component References"](WOClasses22.md#apple-gy4timi) for more on this.

A dynamic element uses its WOAssociations to "pull" values from the request (that is, set its values to what the user specifies) or to "push" its values onto the response page. When a dynamic element that can respond to user actions (such as WOSubmitButton) requests the value of its "action" association, the appropriate action method is invoked and the response page is returned.
The exchange of data through an association that binds an attribute of a parent component to an attribute of a child component can be two-way. This two-way binding allows the synchronization of state between the two components. Consider this declaration in __Main.wod__:

```
START:Calendar {
    selectedDate = startDate;
    callBack = "mainPage";
};
```


In this example, Main is the parent component and Calendar is the child component. The __startDate__ variable (or method) belongs to the parent component while __selectedDate__ is a variable of the child component. A change in the parent component instance variable is automatically communicated through the association to the child variable. Conversely, a change in value in the child component variable is communicated to the parent variable. Component synchronization occurs at the beginning and end of each of the three request-handling phases of a component action request response loop (__takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__). Synchronization is performed through the accessor methods of both components.
__Note:__  The only request-response loop phase that component actions and direct actions have in common is the __appendToResponse:inContext:__ phase. When you are using direct actions, component synchronization occurs at the beginning and end of this phase, which means that the direct action method is performed before the components are synchronized.
This aspect of synchronization has implications for developers. Because WebObjects invokes explicitly implemented accessor methods many times during the same component action request-response loop, your accessor methods must have no side effects. Instead, they should simply set a variable's value or return a value. And if they return a value, there should be some way for WebObjects to set the value.
This rule applies also when the binding involves a parent or a child component's method instead of an instance variable. To illustrate this, assume that __startDate__ is a method of the Main component instead of an instance variable. Even in this case, WebObjects attempts to synchronize __startDate__ with the __selectedDate__ value. In other words, WebObjects attempts to invoke a __setStartDate:__ method and raises an exception if such a method does not exist.
See the chapter ["Creating Reusable Components"](Creating%20Reusable%20Components.md#apple-guzdonq) for more on state synchronization between child and parent component.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses22.md)
