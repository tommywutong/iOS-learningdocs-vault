---
title: Accessibility Programming Guide for iOS
apple_id: TP40008785
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Accessibility_on_iPhone/Accessibility_on_iPhone.html
archived_at: '2026-07-18T02:14:04.073803Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guide for iOS](Introduction.md)


[Next](Making%20Your%20iOS%20App%20Accessible.md)[Previous](Introduction.md)

# Understanding Accessibility on iOS

From the beginning, iOS-based devices included several features that made the device easy for everyone to use, including visual voicemail, large fonts in Mail, and zooming in webpages, photos, and maps. With the addition of the following accessibility features, it’s even easier for people with visual, auditory, and physical disabilities to use their devices:

- Zoom. Magnifies the entire device screen.
- White on Black. Inverts the colors on the display.
- Mono Audio. Combines the sound of the left and right channels into a mono signal played on both sides.
- Speak Auto-text. Speaks the text corrections and suggestions iPhone makes while users type.
- Voice Control. Allows users to make phone calls and control iPod playback using voice commands.

In addition, visually impaired users can rely on VoiceOver to help them use their devices.

VoiceOver is Apple’s innovative screen-reading technology, which gives users control over their devices without having to see the screen. VoiceOver does this by acting as an intermediary between an application's user interface and the user's touch, providing audible descriptions of elements and actions in the application. When VoiceOver is active, users don’t have to worry about accidentally deleting a contact or calling a phone number, because VoiceOver tells them where they are in the user interface, what actions they can take, and what the results of those actions will be.

An application is accessible when all user interface elements with which users can interact are accessible. A user interface element is accessible when it properly reports itself as an accessibility element.

To be useful, however, an accessible user interface element must provide accurate and helpful information about its screen position, name, behavior, value, and type. This is the information VoiceOver speaks to users. The iOS SDK contains a programming interface and tools that help you ensure that the user interface elements in your application are both accessible and useful (for more information, see [iOS Accessibility API and Tools](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgawvgvzs)).

You should make your iPhone application accessible to VoiceOver users because:

- It increases your user base. You've worked hard to create a great application; don’t miss the opportunity to make it available to even more users.
- It allows people to use your application without seeing the screen. Users with visual impairments can use your application with the help of VoiceOver.
- It helps you address accessibility guidelines. Various governing bodies create guidelines for accessibility and making your iPhone application accessible to VoiceOver users can help you meet them.
- It's the right thing to do.

It’s important to be aware that supporting accessibility does not impact your ability to innovate and create beautiful iPhone applications. The UI Accessibility programming interface allows you to add a thin layer of functionality that does not alter your application’s appearance, or interfere with its main logic.

iOS 3.0 and later includes the UI Accessibility programming interface, which is a lightweight API that helps an application provide all the information VoiceOver needs to describe the user interface and help visually impaired people use the application.

The UI Accessibility programming interface is part of UIKit and is implemented on standard UIKit controls and views by default. This means that, when you use standard controls and views, much of the work of making your application accessible is done for you. Depending on the level of customization in your application, making it accessible can be as simple as providing accurate and helpful descriptions of your accessible user-interface elements.

The iOS SDK also provides tools to help you make your application accessible:

- An Interface Builder inspector pane that provides an easy way to furnish descriptive accessibility information while you're designing your nib files. To learn more about how to do this, see [Defining Custom Attribute Information in Interface Builder](Making%20Your%20iOS%20App%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgiwvgvzr).
- Accessibility Inspector, which displays the accessibility information embedded in your application’s user interface and allows you to verify this information when you run your application in iOS Simulator. To learn how to examine the accessibility information in your application, see [Debug Accessibility in iOS Simulator with the Accessibility Inspector](https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestAccessibilityiniOSSimulatorwithAccessibilityInspector/TestAccessibilityiniOSSimulatorwithAccessibilityInspector.html#//apple_ref/doc/uid/TP40012619-CH4).

In addition, you can use VoiceOver itself to test the accessibility of your application. To learn how to test your application with VoiceOver, see [Test Accessibility on Your Device with VoiceOver](https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestAccessibilityonYourDevicewithVoiceOver/TestAccessibilityonYourDevicewithVoiceOver.html#//apple_ref/doc/uid/TP40012619-CH3).

The UI Accessibility programming interface consists of two informal protocols, one class, a function, and a handful of constants:

- The `UIAccessibility` informal protocol. Objects that implement the `UIAccessibility` protocol report their accessibility status (that is, whether they are accessible) and supply descriptive information about themselves. Standard UIKit controls and views implement the `UIAccessibility` protocol by default.
- The `UIAccessibilityContainer` informal protocol. This protocol allows a subclass of `UIView` to make some or all of the objects it contains accessible as separate elements. This is particularly useful when the objects contained in such a view are not themselves subclasses of `UIView` and, for this reason, are not automatically accessible.
- The `UIAccessibilityElement` class. This class defines an object that can be returned through the `UIAccessibilityContainer` protocol. You can create an instance of `UIAccessibilityElement` to represent an item that isn’t automatically accessible, such as an object that does not inherit from `UIView`, or an object that does not exist.
- The `UIAccessibilityConstants.h` header file. This header file defines the constants that describe the traits that an accessibility element can exhibit and the notifications that an application can post.

The attributes that describe an accessible user interface element make up the core of the UI Accessibility API. VoiceOver supplies attribute information to users when they access or interact with a control or view.

Attributes are also the components of the programming interface that you’re most likely to use. This is because attributes encapsulate the information that differentiates one control or view from another. For standard UIKit controls and views, you might just need to ensure that the default attribute information is appropriate for your application; for custom controls and views, you might have to supply most of the attribute information.

The UI Accessibility programming interface defines the following attributes:

- __Label__. A short, localized word or phrase that succinctly describes the control or view, but does not identify the element’s type. Examples are “Add” or “Play.”
- __Traits__. A combination of one or more individual traits, each of which describes a single aspect of an element’s state, behavior, or usage. For example, an element that behaves like a keyboard key and that is currently selected can be characterized by the combination of the Keyboard Key and Selected traits.
- __Hint__. A brief, localized phrase that describes the results of an action on an element. Examples are “Adds a title” or “Opens the shopping list.”
- __Frame__. The frame of the element in screen coordinates, which is given by the `CGRect` structure that specifies an element’s screen location and size.
- __Value__. The current value of an element, when the value is not represented by the label. For example, the label for a slider might be “Speed,” but its current value might be “50%.”

Accessibility elements provide content for attributes, whether that content is supplied by default or by you. An accessibility element always provides content for the frame and label attributes. The frame attribute is required because an accessibility element must always be able to report its position in the user interface. (Note that an object that inherits from `UIView` includes the frame attribute by default.) The label attribute is required because it contains the name or description of the accessibility element that VoiceOver speaks.

An accessibility element is not required to provide content for the hint and traits attributes, if these attributes do not apply to the element. For example, an element that does not perform an action does not need to provide a hint.

An accessibility element provides information for the value attribute only when the element’s contents are changeable and cannot always be described by the label. For example, a text field that contains an email address might have the label “Email address,” but its contents depends on user input and is usually of the form “username@address.” Figure 1-1 shows some of the information VoiceOver might provide.

__Figure 1-1__  VoiceOver speaks the information provided by accessible elements

!!

VoiceOver users rely on the labels and hints they hear to help them use your application. For this reason, it’s especially important to make sure that every accessible user interface element in your application provides accurate and informative descriptions. For standard UIKit controls and views, the default attribute information is often appropriate, but you should inspect these elements to make sure. For custom controls and views, you may have to supply some or all of this information yourself. For some guidelines on how to do this, see [Crafting Useful Labels and Hints](Making%20Your%20iOS%20App%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgiwvgvzw).

[Next](Making%20Your%20iOS%20App%20Accessible.md)[Previous](Introduction.md)

