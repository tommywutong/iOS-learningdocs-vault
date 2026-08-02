---
title: Accessibility Programming Guidelines for Carbon
apple_id: TP30001127
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MakingAppsAccessible/AXCarbonCustom/AXCarbonCustom.html
archived_at: '2026-07-15T05:23:22.416208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Carbon](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Carbon.md)


[Next](Document%20Revision%20History.md)[Previous](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md)

# Making a Custom Carbon Application Accessible

Many Carbon applications use custom application frameworks instead of newer technologies, such as HIToolbox. This chapter defines a custom Carbon application as one that fits at least some of the following criteria:

- It relies on a custom application framework.
- Its user interface implementation may not be object-oriented.
- It may not use Carbon events.

If some of these statements describe your application, you should read this chapter for guidelines on how to access-enable your application.

There is no doubt that it is more work to access-enable a custom application than an application that handles Carbon events and uses only HIObjects and HIViews in its user interface. However, the Carbon accessibility implementation allows the selective addition of accessibility support. This means you can add accessibility where and when you need it, without worrying about having to redesign your application.

Although some steps will change for individual applications, in general, you take the following steps to access-enable a custom Carbon application:

- Decide which user interface objects need to be accessible and define their relationships.
- Create an accessibility object for each accessible user interface object.
- Install event handlers on the new accessibility objects to handle the accessibility events.
- Make sure the new accessibility objects send the appropriate notifications to assistive applications.

The following sections in this chapter describe each of these steps in more detail. In addition, be sure your application does not use the `GetCurrentEventKeyModifiers` function. If it does, see [Key Modifiers and VoiceOver](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cizcumskf) for information about why you should not use this function and a suggestion for how to replace it.

As described in _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_, your application presents itself to an assistive application as a hierarchy of accessibility objects. As assistive application traverses the hierarchy in response to a user’s navigational commands and when determining keyboard and mouse focus. If a user interface object is not represented by an accessibility object in the accessibility hierarchy, it is invisible to an assistive application.

The first step in access enabling a custom Carbon application is to determine which objects should appear in the accessibility hierarchy.

In a standard Carbon application, the containment hierarchy defined by the HIObjects and HIViews automatically provides the fundamental structure of the accessibility hierarchy. An HIView, for example, is aware of all its children and Carbon automatically provides references to these children in response to events that ask for them.

Because your application does not rely on standard HIObjects and HIViews in its user interface, you have to define the accessibility hierarchy yourself. This requires some thought about how a user navigates and uses your application. It might be helpful to use the Accessibility Inspector application (available in `/Developer/Applications/Utilities/Accessibility Tools` in Mac OS X version 10.4) to examine the accessibility hierarchies of other applications.

With your application’s accessibility hierarchy mapped out, you can proceed with the task of making each appropriate user interface object accessible

As described in [Creation of Accessibility Objects](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2ci5femqke), it is efficient to create accessibility objects as they are needed, in response to accessibility events, rather than creating all of them when your application launches (or a window opens). Whichever way you choose to create accessibility objects to represent your custom user interface objects, however, you must do some preparation first.

Because the Carbon implementation of accessibility objects is based on HIObject, you must create an HIObject wrapper for each accessible custom object in your user interface. You need to have an HIObject to represent a view, for example, so you have an object on which to install your custom accessibility event handlers. As you access-enable your application, you install the accessibility event handlers that supply values and information specific to your application.

To create an HIObject (or HIView) wrapper for a custom user interface object, you use the `HIObjectCreate` function.

Note that you need to register your wrapper subclass in advance with the `HIObjectRegisterSubclass` function.

Instead of creating an HIObject wrapper for each subcomponent of your complex object, create a wrapper for the top-level object and define a unique 64-bit identifier for each accessible subcomponent. To follow the Carbon convention, the identifier of the top-level object should be `0`.

Now that you have an `HIObjectRef`, you use it to create an accessibility object. To do so, use the `AXUIElementCreateWithHIObjectAndIdentifier` function, passing it the `HIObjectRef` and an identifier.

For complex objects that contain arbitrary levels of child objects, the identifier of the top-level, parent object should have the value `0`. If you need to create an accessibility object for a subcomponent, you define an identifier for that part that makes sense in your implementation.

When you create an accessibility object, you must also supply the appropriate set of attributes and values. As described in [Accessibility Object Attributes](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cjbfecr2j), the most important attribute is the role attribute. The Mac OS X accessibility protocol defines a large number of roles that cover most things a user interface object can be. Assistive applications rely on the roles Mac OS X defines, so you should not create new ones. Look through the roles defined in `AXRoleConstants.h` to find the role that most closely describes what you custom object does. If your custom object behaves like a button, for example, you should define its role attribute to be `AXButton`.

If you provide the value of the role attribute, you also have to provide the value of the role description attribute. Carbon provides the `HICopyAccessibilityRoleDescription` function that allows you to get the Apple-defined role description for a specific role so you don’t have to create one yourself. Using this function ensures that your application will always be up to date, even if Apple changes a role’s description.

After you’ve created accessibility objects to represent all your accessible user interface objects, install your custom accessibility event handlers. These handlers are just like the handlers discussed in [Install Custom Event Handlers](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfjfdeiq2d). The only difference is in the specific events you must handle.

In general, you will need to handle all the events you handle for a semistandard Carbon application, in addition to any required by your custom user interface elements.

As with the accessibility Carbon events, you handle notifications in you custom application just as you handle them in a semistandard application. The difference is in which notifications you must send. For completely custom objects, you cannot depend on Carbon to send notifications for you, so you must send them yourself. This includes the fundamental creation and destruction notifications, in addition to the notifications of object movement and value change.

See [Send Notifications](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawuessfivauirsf) for more information on how to send notifications.

[Next](Document%20Revision%20History.md)[Previous](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md)

