---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/Associations.html
archived_at: '2026-07-15T07:46:51.200677Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](Templates.md)

# __Associations and the Current Component__

A dynamic HTML element such as a text field or a pop-up button differs from a static HTML element (for example, a heading) in that its attributes can change over a cycle of the request-response loop. These attributes can include values that determine behavior or appearance (a "disabled" attribute, for instance), values that users enter into a field, values that are returned from a method, and actions to invoke when users click or otherwise activate the element. Each dynamic element stores its attributes as instance variables of type WOAssociation.

WOAssociation objects know how to obtain and set the value they represent. Usually WOAssociations work by key-value coding. The key to a value can be represented as a sequence of keys separated by periods. The resolution of a key by yielding its value makes possible the resolution of the next key. For instance:

```
  self.aRepetition.list.item
```

means that `self` (identifying the current component) has a WORepetiton named `aRepetition`. The `list` key denotes the list of elements displayed by the WORepetiton, and the `item` is the key to the current item in that list. Keys (including actions) are WOAssociations defined for each dynamic element. The values for these keys are constants assigned in the ".wod" file, or they derive from bindings to variables or methods, also made in a component's ".wod" file.

WOAssociations refer to the _current component_ for the initial value of this sequence. It gets this object from the transaction's WOContext object. Often the current component is the request or response page of the transaction, but it can be a reusable component embedded in a page, or even a component incorporated by one of those subcomponents (see "[Subcomponents and Component References](Subcomponents.md#apple-kjcumnzwgeytg)" for more on this). The WOContext stores the current component on a stack, "pushing" and "popping" components onto and off of the stack as necessary.

Depending on the phase of the request-response loop, a dynamic element uses its WOAssociations to "pull" values from the request (that is, set its values to what the user specifies) or to "push" its values onto the response page. When a dynamic element that can respond to user actions (such as WOSubmitButton) requests the value of its "action" WOAssociation, the appropriate action method in the current component is invoked and the response page is returned.

The exchange of data through an association that binds an attribute of a parent component to an attribute of a child component is two-way. This two-way binding allows the synchronization of state between the two components. For example, consider this example declaration in __Main.wod__ of the TimeOff example:

```
START:Calendar {
    selectedDate = startDate;
    callBack = "mainPage";
};
```

In this example, Main is the parent component and Calendar is the child component. The "startDate" variable belongs to the parent component while "selectedDate" is a variable of the child component. A change in the parent component instance variable is automatically communicated through the association to the child variable. Conversely, a change in value in the child component variable is communicated to the parent variable. Component synchronization occurs at the beginning and end of each of the three request-handling phases of a component (__takeValuesFromRequest:inContext:__, __invokeAction:inContext:__, and __appendToResponse:inContext:__) Synchronization is performed through the accessor methods of both components.

This aspect of synchronization has a couple of implications for developers, especially when they implement accessor methods. Since WebObjects invokes explicitly implemented accessor methods up to six times during the same request-response loop, these methods should not have any side effects. Accessor methods should simply set a variable's value or return a value. And if you return a value, there should be some way for WebObjects to set the value. This rule applies also when the binding involves a parent or a child component's method instead of an instance variable. To illustrate this, assume that "startDate" is a method of the Main component instead of an instance variable. Even in this case, WebObjects attempts to synchronize "startDate" with the "selectedDate" value. In other words, WebObjects attempts to invoke a "setStartDate:" method, and raises if such a method does not exist.

See the chapter "[Reusable Components](../Reuse/Reuse.book.md)" for more on state synchronization between child and parent component.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](Subcomponents.md)
