---
title: Accessibility Programming Guidelines for Carbon
apple_id: TP30001127
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MakingAppsAccessible/AXCarbonSemiStandard/AXCarbonSemiStandard.html
archived_at: '2026-07-15T05:23:22.433069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Carbon](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Carbon.md)


[Next](Making%20a%20Custom%20Carbon%20Application%20Accessible.md)[Previous](Making%20a%20Standard%20Carbon%20Application%20Accessible.md)

# Making a Semistandard Carbon Application Accessible

Many applications use HIObject and HIView objects, but may implement custom classes to represent some of the contents of those objects. An example is an application that creates a custom HIView to represent a custom control not provided by the system, such as a volume indicator control.

This chapter defines a semistandard Carbon application as one that fits the following criteria:

- It uses only HIObject and HIView objects to represent its user interface objects, although it may use custom classes to implement substructure.
- It is Carbon event driven.
- The accessibility hierarchy may deviate from the containment hierarchy defined by the HIObjects and HIViews.

If this describes your application, there are a few things you must do to make sure assistive applications can access all parts of your application’s user interface. This chapter describes the steps you take to access-enable the custom portions of your application. It does not describe the steps you take to access-enable the standard portions of your application. If you haven’t already, be sure to read [Making a Standard Carbon Application Accessible](Making%20a%20Standard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywviucykjcummjqge) to learn how to provide the context-specific attribute values all applications must supply.

Although access enabling a semistandard Carbon application is somewhat more work than access enabling a standard Carbon application, the task is quite manageable. In general terms, you need to provide the same information about your custom objects that Carbon provides about standard objects. Specifically, this means you:

- Create an accessibility object for each accessible custom subview of the HIView objects in the user interface, if necessary.

  For each accessibility object you create, you must provide the necessary attributes and make sure it is properly inserted into your application’s accessibility hierarchy.
- Adjust the default accessibility hierarchy, if necessary, to accommodate child objects you might add or remove.
- Install any custom Carbon accessibility event handlers your application requires to implement custom behavior.

The following sections describe how to accomplish these steps. To learn how to provide application-specific values for descriptions, titles, and labels, see [Making a Standard Carbon Application Accessible](Making%20a%20Standard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywviucykjcummjqge).

In addition, be sure your application does not use the `GetCurrentEventKeyModifiers` function. If it does, see [Key Modifiers and VoiceOver](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cizcumskf) for information about why you should not use this function and a suggestion for how to replace it.

A single HIView object can represent a simple user interface element that contains no substructure or a complex element that contains a great deal of substructure. A data browser, for example, is a single HIView that contains a complex substructure. As described in [The Carbon Implementation of the Accessibility Object](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cjjeuoqsj), Carbon can represent the accessible parts of a complex substructure with a single HIView combined with a unique identifier.

In your application, you might define both simple and complex custom HIView objects. For these objects to be accessible, you must create accessibility objects to represent them. The following sections describe how to do this.

If your custom subview is an HIView and it contains no substructure, create an accessibility object for it with an identifier value of `0`. Recall from [The Carbon Implementation of the Accessibility Object](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cjjeuoqsj) that an identifier value of `0` indicates that the accessibility object represents the user interface element as a whole. Because this accessibility object represents a user interface element that has no substructure, it automatically represents the element as a whole.

To create an accessibility object for such a user interface element, use the `AXUIElementCreateWithHIObjectAndIdentifier` function, passing in the HIViewRef reference and 0, as shown below:

```
accessibilityObject = AXUIElementCreateWithHIObjectAndIdentifier( HIObjectRef myHIView, 0 )
```

Because your custom subview is an HIView, Carbon provides attribute values it can extract from the object, such as size and position. As with other accessibility objects in your application, however, you must provide the context-specific information that Carbon cannot determine. For information on providing descriptive and linking information, see [Making a Standard Carbon Application Accessible](Making%20a%20Standard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywviucykjcummjqge). If there are additional attribute values you need to provide, do this with custom event handlers. For more information on how to do this, see [Install Custom Event Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfjfdeiq2d).

Although most custom HIViews an application might create are uncomplicated, it’s not uncommon for an application to need a custom HIView with complex substructure. From an accessibility perspective, however, such an HIView is accessible but its contents are not. This is because Carbon does not automatically create accessibility objects for the children of a custom HIView.

If you do this in your application, the first thing you need to do is create an accessibility object to represent each accessible child of the HIView. As mentioned in [Creation of Accessibility Objects](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2ci5femqke), you may choose to create these accessibility objects only when needed (in response to an assistive application’s requests) or in advance (when you open the application or display a window). Either way, when it’s time to provide an accessible subview, use the `AXUIElementCreateWithHIObjectAndIdentifier` function to create an accessibility object for it.

As described in [The Carbon Implementation of the Accessibility Object](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cjjeuoqsj), an accessibility object consists of an HIObject and an identifier. If you are creating an accessibility object for a child view of an HIView, for example, pass to the `AXUIElementCreateWithHIObjectAndIdentifier` function:

- The `HIViewRef` of the parent object
- An integer you define that uniquely identifies the subview

As with other accessibility objects in your application, you must provide the context-specific descriptive and linking information that Carbon cannot determine. For information on providing this information, see [Making a Standard Carbon Application Accessible](Making%20a%20Standard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywviucykjcummjqge). To provide additional attribute values, use custom event handlers, as described in [Install Custom Event Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfjfdeiq2d).

If you add a new subview to an existing HIView you need to adjust the accessibility hierarchy that Carbon creates. Similarly, you must adjust the accessibility hierarchy if you want to prevent a subview of an HIView from being accessible. This section describes how to adjust the accessibility hierarchy to accommodate these changes. This section assumes that you have already created accessibility objects to represent any new subviews you are adding to the hierarchy. If you have not, see [Create Accessibility Objects for Custom Subviews](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfjbeucrkf) for more information on how to do this.

To add the accessibility object representing a subview to your application’s accessibility hierarchy, you follow these steps:

1. Make sure the accessibility object you create returns its new parent when asked for the value of the parent attribute.

   In most cases, the parent of the new accessibility object is its containing HIView. However, there may be times when you want an accessibility object to be the child of some more distant ancestor. Be sure to map out these relationships to ensure their correct representation in the accessibility hierarchy.
2. Install on the parent object an event handler for the `kEventAccessibleGetNamedAttribute` event. When an assistive application asks for the value of the children attribute, your handler gets the child array the parent object’s event handler provides and adds the new child (or children) to it. Your handler then returns the modified array.
3. Override the parent object’s hit-testing and keyboard-focus event handlers so you can return more specific information.

It is unlikely you will ever need to remove a child accessibility object from the accessibility hierarchy. If you do, however, the process is simple:

1. Install on the parent object an event handler for the `kEventAccessibleGetNamedAttribute` event. When an assistive application asks for the value of the children attribute, your handler gets the child array the parent object’s event handler provides and removes the child from it. Your handler then returns the modified array.
2. Override the parent object’s hit-testing and keyboard-focus event handlers so you can remove the child from the return values.
3. Inspect the accessibility hierarchy for other attributes that might refer to the child you want to remove. A convenience attribute, such as the kAXHorizontalScrollBarAttribute attribute, might refer to a child you want to remove. If you find any such attributes, adjust your handler for the `kEventAccessibleGetNamedAttribute` event to handle these, as well.

Although the Carbon accessibility implementation automatically handles events for standard HIViews, some of these events require information about the children of an HIView. If you implement these children, you must install custom handlers that provide information about them.

The types of event you must handle depend on the complexity of the subviews you implement.

- __Simple subview__. This is a subview that does not contain any children. For these subviews, you must make sure the parent HIView includes the subview in its children attribute array. Then, you can rely on the parent’s event handlers to return accurate information about your custom subview, including hit-testing and keyboard-focus information.
- __Complex subview__. This is a subview that contains an arbitrarily complex hierarchy of children. For these subviews, you must make sure the parent HIView includes your top-level subview in its children attribute array. Additionally, you must install handlers on your subview and its children to handle other events, such as hit-testing and keyboard-focus events.

If you use a custom class to implement a simple subview of an HIView, your main task is to make sure the parent view is aware of its child view. This ensures that your subview accessibility object is part of the accessibility hierarchy. Then, you may choose to provide handlers for other events.

To ensure that the parent HIView is aware of your simple subview, you must insert the accessibility object you’ve created for the subview into the parent’s children attribute array. To do this, you install on the parent HIView a handler for the `kEventAccessibleGetNamedAttribute` event that listens for a request for the value of the children attribute. When such a request arrives, your custom handler gets the parent HIView’s children attribute array and inserts your accessibility object.

After your custom accessibility object is a member of its parent’s children attribute array, you can rely on the parent’s default hit-testing and keyboard-focus handlers to return your subview when appropriate.

If you implement a complex subview, you must handle the `kEventAccessibleGetNamedAttribute` event both for your parent HIView (as described in [Handle Events for Simple Subviews](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfijcuqrki)) and for your top-level subview. In addition, you must handle the hit-testing and keyboard-focus events that request information about your subview’s children.

To report information about your subview’s internal structure, install on your subview’s accessibility object a handler for the `kEventAccessibleGetNamedAttribute` event. Your custom handler responds to the request for the value of the children attribute by creating and returning an array of the subview’s accessible child accessibility objects. If your complex subview represents several levels of containment, you have to provide a similar handler for each level.

To handle the hit-testing and keyboard-focus events for your subview’s accessible children, install handlers for the `kEventAccessibleGetChildAtPoint` and `kEventAccessibleGetFocusedChild` events. It is important to return only the immediate child of the accessibility object receiving these events, not a grandchild or more distant descendant. This is because the Carbon accessibility implementation automatically handles the recursive traversal of the accessibility hierarchy.

If the custom subviews you create support actions, you must also handle the following events:

- `kEventAccessibleGetAllActionNames`
- `kEventAccessibleGetNamedActionDescription`
- `kEventAccessiblePerformNamedAction`

Your handler for the `kEventAccessibleGetAllActionNames` event must return the names of all actions your custom subview supports. Action names are defined in `AXActionConstants.h` (in the HIServices framework) and are of the form `AX`_Actionname_, such as `AXRaise` and `AXPush`. To supply these names, you create a CFString for each action name and insert them into the mutable CFArray in the event’s _kEventParamAccessibleActionNames_ parameter.

Unlike an action name, such as `AXRaise`, an action description is a human-intelligible, localizable string that names the action, such as “raise”. If your custom subview supports an action, you must also supply the action description. If you’re developing in Mac OS X version10.4 or later, you can use the `AXUIElementCopyActionDescription` convenience function (defined in `AXUIElement.h`) to get the current system-defined action description instead of hard-coding it. This way, your action description will always be consistent with the system’s action descriptions, even if they change.

Use the action description to modify the mutable CFString in the event’s _kEventParamAccessibleActionDescription_ parameter.

An assistive application uses the `kEventAccessiblePerformNamedAction` event to tell an accessibility object to perform an action. If you provide a custom subview that performs actions, you must handle this event.

Beginning in Mac OS X version 10.3, the `kEventAccessiblePerformNamedAction` event includes a parameter that allows you to defer the action if performing it involves a call to a routine that might not return immediately. This can happen if your application performs a modal action, such as bringing up a menu. An assistive application waiting for confirmation of the performance of an action can time out if it takes too long. The assistive application can interpret this as a failure to perform the action (and give this feedback to the user), even if your application is running normally.

To avoid this situation, you can check the _kEventParamAccessibilityEventQueued_ parameter. If it indicates the event has been queued, you can perform the action (including the calls to routines that might not return immediately) without causing an assistive application to time out. If it indicates the event has not been queued, you can request the event be queued and sent to you later. To request the event be queued, return `eventDeferAccessibilityEventErr` from your event handler.

An assistive application relies on notifications from accessibility objects to tell it when, for example, the object appears or disappears. Carbon implements the notification mechanism for standard HIObject and HIView objects. If you create custom classes to implement subviews in your application, however, you must send some of these notifications yourself.

To broadcast a change to a custom user interface object, use the `AXNotificationHIObjectNotify` function (defined in `CarbonEvents.h`). The function requires the `HIObjectRef` and 64-bit identifier that identify the user interface object and the notification name string. If, for example, a custom window has moved, you pass the notification string “AXWindowMoved”. The header file `AXNotificationConstants.h` (in the HIServices framework) defines the notification strings you can use.

[Next](Making%20a%20Custom%20Carbon%20Application%20Accessible.md)[Previous](Making%20a%20Standard%20Carbon%20Application%20Accessible.md)

