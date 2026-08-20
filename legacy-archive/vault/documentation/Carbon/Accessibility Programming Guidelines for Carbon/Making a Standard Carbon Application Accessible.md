---
title: Accessibility Programming Guidelines for Carbon
apple_id: TP30001127
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MakingAppsAccessible/AXCarbonStandard/AXCarbonStandard.html
archived_at: '2026-07-15T05:23:22.440659Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Carbon](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Carbon.md)


[Next](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md)[Previous](Accessibility%20and%20the%20Carbon%20Framework.md)

# Making a Standard Carbon Application Accessible

Most new Carbon applications rely on HIToolbox technologies to implement their user interfaces. This chapter defines a standard Carbon application as one that fits the following criteria:

- It uses only standard HIObjects and HIViews to represent all user interface objects.
- It uses only standard HIViews to represent all subviews of a complex HIView, such as the contents of a tabs view.
- The accessibility hierarchy of the application does not deviate from the containment hierarchy defined by the HIObject and HIView objects in the user interface. In other words, you do not redefine the parent-child relationships among user interface objects.

If this describes your application, read this chapter to learn how to access-enable your application. If your application fits most of the criteria, but implements some custom behavior, read this chapter first. Then, read [Making a Semistandard Carbon Application Accessible](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrrgawviucykjcummjqge) to learn how to handle the custom behavior.

Because your application uses only standard HIObjects and subclasses in its user interface, there is very little you have to do to make it accessible. Carbon provides much of the accessibility infrastructure, so your task is mainly one of enhancement and refinement. This is because the Carbon accessibility implementation can handle generic things such as window placement, containment hierarchies, and actions, but it can’t predict or discover many of the application-specific details that make your application unique. Far from being merely cosmetic, therefore, the information you provide not only makes your application more accessible, it enhances the user’s experience.

The rest of this chapter describes specific steps you take to make your application accessible. In addition, be sure your application does not use the `GetCurrentEventKeyModifiers` function. If it does, see [Key Modifiers and VoiceOver](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cizcumskf) for information about why you should not use this function and a suggestion for how to replace it.

An assistive application needs to be able to describe all accessible user interface elements to the user. Often, an assistive application can present the title of the element to the user, but sometimes an element’s title is either unavailable or not sufficiently descriptive. Therefore, you must examine your application and ensure that all accessibility objects supply descriptive information about themselves in either the title or description attributes.

First, determine if a given accessibility object already includes the title attribute. A standard HIView object that displays a text title as part of its visual interface, such as an OK button, already includes the title attribute with the value of the displayed text. Such an object does not need a description attribute because its title is sufficient to convey its purpose to the user. (If a user interface element is titled by a separate static-text string, see [Link Objects and Related Static Text Titles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywugsceinceeqsg) for details on how to provide this information to assistive applications.)

A button that displays an icon instead of a text title, however, does not have a title attribute. An example of such an object is a “back” button that displays a left-pointing arrow instead of the word “Back”. An assistive application cannot describe such a button’s purpose to a user unless the accessibility object representing the button includes the description attribute. If you have such an object in your application, you must supply an appropriate description in the description attribute.

An accessibility object’s description attribute is static and not settable by an assistive application. For this reason, you can use the `HIObjectSetAuxiliaryAccessibilityAttribute` function to set it. If you’re interested in how this function works, see [Providing Attribute Values Without Event Handlers](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cizcuissg). If you’re developing in a version of Mac OS X prior to 10.4, see [Install the Necessary Event Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywugscei5cuusce) to learn how to set the description value with an event handler.

If you must supply the value of an accessibility object’s description attribute, be sure that the description:

- __Is accurate and succinct__. Remember that a user may hear this description spoken aloud by an assistive application every time the object has keyboard focus or is under the mouse pointer.
- __Does not include the role of the object__. An assistive application, such as a screen reader, is likely to speak a concatenation of the description string you provide and the role description value. If you include the role in your description, such as “left justify button”, a screen reader may speak “left justify button button”.
- __Uses only lower case and does not include any punctuation__. This ensures that your description is intelligible to the largest range of assistive applications. Setting a description value to “left justify” instead of “left-justify”, for example, avoids potential confusion.

It is not uncommon for an application to display a piece of static text that serves as the title for a user interface object. You might choose to do this if you want to display a title for some number of user interface objects that do not display titles as part of their visual display. If this is something you do in your application, you must make the relationship between the static text and the interface object or objects clear to assistive applications. Otherwise, an assistive application cannot tell a user that the static text title and the user interface object or objects are related.

Mac OS X version 10.4 introduced two new attributes to handle this situation:

- `kAXTitleUIElementAttribute`
- `kAXServesAsTitleForUIElementsAttribute`

Because these attributes are static and nonsettable (they help define the layout of your application), you can use the `HIObjectSetAuxiliaryAccessibilityAttribute` function to provide their values. As their names imply, the values of these attributes are not strings, but accessibility objects. This means that you must create a new accessibility object to represent the static text before you use the `HIObjectSetAuxiliaryAccessibilityAttribute` function to link it to the user interface object (or set of objects) it describes.

The value of the `kAXTitleUIElementAttribute` attribute is an accessibility object that represents a static text title. The value of the `kAXServesAsTitleForUIElementsAttribute` attribute is an array of accessibility objects. This allows you to link several user interface objects to a single title.

To see how this works, consider a set of editable text fields intended to contain parts of a mailing address. Instead of titling each text field separately, you supply a single static text title, such as “Address:”, to title the set of text fields. To link these text fields with the static text title, you follow these steps:

1. Use the `AXUIElementCreateWithHIObjectAndIdentifier` function to create an accessibility object to represent the static text title (“Address:”, in this example).
2. Add the `kAXServesAsTitleForUIElementsAttribute` attribute to the accessibility object representing the static text title that you created in Step 1. The value of this attribute is an array containing the accessibility object (or objects) representing the user interface object (or objects) you want to be associated with this static text title.

   In this example, the value of the `kAXServesAsTitleForUIElementsAttribute` attribute is an array containing the accessibility objects that represent the editable text fields.
3. Add the `kAXTitleUIElementAttribute` attribute to the accessibility object representing the user interface object to which you want to relate the title. The value of this attribute is the accessibility object you created in Step 1 to represent the static text title.

   In this example, you add the `kAXTitleUIElementAttribute` attribute to each accessibility object that represents one of the editable text fields.

A label is separate static text that gives additional information about parts of a control. For example, an application might display a slider with labeled tick marks that describe the slider’s measurements.

To a sighted user, the proximity of the label and the slider implies their relationship. To an assistive application, however, the label and the slider are unrelated. To allow an assistive application to provide this information to the user, therefore, you must specify the relationship between them.

Unlike the title of a button, a label is not part of the user interface object it describes. Instead, a label is similar to a static text title, such as the title “Address:” in the example in [Link Objects and Related Static Text Titles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqgywugsceinceeqsg).

In the example above, the slider is accompanied by a set of tick marks, each of which refers to one value in the range of values the slider can have. Each tick mark is considered to be a separate label. This allows you to provide such information in discrete pieces, instead of in a single string. Such a slider does not have a label consisting of the single string “0 5 10 15 20”, therefore, but a set of labels, each of which contains a single element, such as “0”, “5’, “10”, “15”, and “20”.

To provide such information to an assistive application, you create an accessibility object for each label. Each of these accessibility objects includes a `kAXLabelValueAttribute` attribute that contains the value of that label. The accessibility object representing the control (the slider in this example) contains a `kAXLabelUIElementsAttribute` attribute. The value of this attribute is an array of accessibility objects, which allows you to link an arbitrary number of labels with the control.

If your application displays different views of the same or related content, you must make this relationship clear to assistive applications. For example, if you display a list of files in one window and you allow the user to view the contents of a selected file in another part of the window or in a different window, an assistive application cannot know that the two views are related. Similarly, an assistive application cannot predict where you display the results of a search field in your application. You must tell an assistive application how such views are related to ensure that a user can move directly between them without having to step through every intervening view and control.

To make this relationship explicit, add the `kAXLinkedUIElementsAttribute` attribute to each related view’s accessibility object. The value of this attribute is an array of accessibility objects so you can specify different configurations of related views, such as one-to-one and one-to-many.

You can provide these links either statically or dynamically, depending on the design of your application. If a link is dictated by the layout of your application, you can use the `HIObjectSetAuxiliaryAccessibilityAttribute` function to provide the attribute values. If, on the other hand, a link is determined dynamically when a user uses your application, you set the value of the `kAXLinkedUIElementsAttribute` attribute with an event handler for the `kEventAccessibleGetNamedAttribute` event.

The `HIObjectSetAuxiliaryAccessibilityAttribute` function introduced in Mac OS X version 10.4 gives you a convenient way to provide the values of static attributes. If you are developing in a version of Mac OS X prior to 10.4, however, or you are dealing with settable attribute values, you use the Carbon event mechanism to set them. For an overview of the Carbon accessibility events, see [Accessibility Carbon Events](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cizeeossd).

To set the value of a settable attribute, create a handler for the `kEventAccessibleSetNamedAttribute` event. This event includes parameters that contain the name of the attribute and the new value. Your handler should ensure that:

- The accessibility object supports the given attribute.
- The data (which can be of an arbitrary Core Foundation type) makes sense for the attribute.

If the handler accepts the given parameter values, it should set the value of the attribute to the passed-in data. If the accessibility object does not support the given attribute, the handler should return the `eventNotHandledErr` error.

It’s worth repeating that most Carbon applications that do not implement any custom user interface objects or custom subviews of HIView do not have to install custom event handlers. For such applications, the standard event handlers Carbon installs should be sufficient.

To provide an accessibility object’s attribute value using an event handler, create a handler for the `kEventAccessibleGetNamedAttribute` event. This event includes a parameter that contains the name of the attribute (in a CFString object). Your handler should ensure that the accessibility object supports the attribute. If it does, the handler should return the value of the attribute in the _kEventParamAccessibleAttributeValue_ parameter. If it does not support the attribute, your handler should return the `eventNotHandledErr` error.

The `kEventAccessibleGetNamedAttribute` event can also include a parameter that describes a part of a parameterized attribute. As described in [Parameterized Attributes](Accessibility%20and%20the%20Carbon%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrxfvbuqmrqg4wuer2cjbeucr2f), parameterized attributes became available in Mac OS X version 10.3. If the given accessibility object supports parameterized attributes, your handler should return the value for the part of the element specified by the _kEventParamAccessibleAttributeParameter_ parameter. Again, if the accessibility object does not support the attribute, your handler should return the `eventNotHandledErr` error.

If you’re developing an application in a version of Mac OS X prior to 10.4, you must install a custom event handler to provide the value of the description attribute for those accessibility objects that need it. Your handler must also provide the values of the title and label attributes if you support them. This event handler responds to the `kEventAccessibleGetNamedAttribute` event by returning the value of the passed-in attribute in the _kEventParamAccessibleAttributeValue_ parameter.

[Next](Making%20a%20Semistandard%20Carbon%20Application%20Accessible.md)[Previous](Accessibility%20and%20the%20Carbon%20Framework.md)

