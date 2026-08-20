---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/EnhancingtheAccessibilityofStandardAppKitControls.html
archived_at: '2026-07-15T03:49:08.315358Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Accessibility Programming Guide for OS X](index.md)



## Enhancing the Accessibility of Standard AppKit Controls

When it comes to accessibility, AppKit does a lot of the heavy lifting for you. AppKit views and controls adopt the [NSAccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility) protocol. This provides appropriate default values and implementations for all the information properties and action methods. The AppKit elements also send the appropriate notifications, based on their expected usage.

The system also attempts to fill in many of the information properties with meaningful default values. For example, an [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) object’s [accessibilityLabel](https://developer.apple.com/documentation/appkit/nsaccessibility/1534976-accessibilitylabel) property automatically defaults to the button’s title. This means, in many cases, standard AppKit controls do not require any additional work on your part. They are accessibility-enabled straight out of the box.

However, while the AppKit’s default properties are complete, they are not always as useful as we would like. In some cases, you may need to modify these default values to better represent your app, to provide additional context, or to modify the user’s flow through the app. Typically we do this by modifying the information properties.

You can modify these properties in three ways:

- __Using Interface Builder.__ When using Interface Builder, the Accessibility Identity settings in the Identity inspector let you modify some of the information properties. Specifically, the Description field lets you set the element’s [accessibilityLabel](https://developer.apple.com/documentation/appkit/nsaccessibility/1534976-accessibilitylabel) property while the Help field let’s you set its [accessibilityHelp](https://developer.apple.com/documentation/appkit/nsaccessibility/1534974-accessibilityhelp) property.
- __Assigning programmatically.__ You can assign a new value to any of the properties in code.
- __Overriding accessor methods.__ If you subclass the AppKit element, you can override the accessor methods for its information properties. This can be more efficient when working with dynamic controls. Here, you simply return the current state upon request—rather than trying to update the property in response to changes.

> [!NOTE]
> 

### Enhancing the Default Behavior

When modifying a control’s default accessibility behaviors, start by focusing on the following:

- __Follow the HIG.__ Make sure your user interface follows the guidelines listed in the _OS X Human Interface Guidelines_. Accessibility clients expect your app to behave in certain ways. It is considerably easier to accessibility-enable your app when you follow the guidelines in the HIG.
- __Assign a useful label.__ Every element that the user can interact with must have a meaningful value set for its [accessibilityLabel](https://developer.apple.com/documentation/appkit/nsaccessibility/1534976-accessibilitylabel) property. Ideally, this label is a single word that briefly describes the control. Add, Play, Delete, Search, Favorites, and Volume all make ideal labels.

  Do not include the type of control in the label. For example, use Add not Add Button. The control’s [accessibilityRoleDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535144-accessibilityroledescription) property already captures the control type.

  Also, to ensure that VocieOver reads the label with the correct inflection, the label should start with a capital letter. Do not put a period at the end. Finally, always localize your control’s label.
- __Modify the role description, if necessary.__ Accessibility clients use the [accessibilityRoleDescription](https://developer.apple.com/documentation/appkit/nsaccessibility/1535144-accessibilityroledescription) property when describing the control. Most of the time, the default value for the role description works perfectly well; however, you might find a few cases where you can make the control’s intent clearer by replacing the default role description. This is particularly true when you are using a standard control in a nonstandard manner.
- __Use help text to describe the effect.__ Accessibility clients use the [accessibilityHelp](https://developer.apple.com/documentation/appkit/nsaccessibility/1534974-accessibilityhelp) property to describe the results of performing an action. Essentially, the help text acts like a tool tip.

  Use help text only when the results are not obvious from the control’s label. Just like the label, strive to make the help text as short as possible. Start with a capital letter. Begin with a verb and omit the subject. For example, use “Plays the song” not “This button plays the song.” Also, do not include a description of the action, gesture, view or control. Finally, always localize your help text.
- __Define links and groups to provide context.__ Visual users often know that sets of controls go together due to their proximity on screen. However, you must explicitly define these relationships before accessibility clients can use them as well. For example, a view could adopt the [NSAccessibilityGroup](https://developer.apple.com/documentation/appkit/nsaccessibilitygroup) protocol, indicating that its contents should be treated as a group of controls. Similarly, you can use the [accessibilityLinkedUIElements](https://developer.apple.com/documentation/appkit/nsaccessibility/1534972-accessibilitylinkeduielements) property to define the relationship between a list item and the contents displayed in different pane or window. You can also use the [accessibilityTitleUIElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535155-accessibilitytitleuielement) to specify the static text element that acts as this control’s label.
- __Focus users on the important parts of the interface.__ Use the [accessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535002-accessibilityelement) property to focus the users on the important parts of the interface. If this property is set to `NO``false`, accessibility clients ignore this element, skipping directly to its children (if any). By default, `NSView` and its subclasses set this value to `NO``false`. Users are not typically interested in the views. They want to access the things inside the views. However, if your `NSView` subclass adopts one of the role-specific accessibility protocols, the system automatically changes the [accessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibility/1535002-accessibilityelement) property’s value to `YES``true`.

It’s often useful to observe how VoiceOver treats these properties. For example, when you select a control, VoiceOver reads the label and the role description. If you pause with a UI element selected, VoiceOver provides additional guidance and then reads the help text (if any).

[The OS X Accessibility Model](OSXAXmodel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqhawviucykjcummjqge)

[Implementing Accessibility for Custom Controls](ImplementingAccessibilityforCustomControls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrvgywvgvzr)
