---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/ImplementingAccessibilityforCustomControls.html
archived_at: '2026-07-15T03:49:09.153267Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Accessibility Programming Guide for OS X](index.md)



## Implementing Accessibility for Custom Controls

At its most basic, implementing accessibility for custom controls is as simple as adopting a protocol and then implementing any missing methods. The real challenge comes when you want to modify the control’s behavior beyond what is provided by the protocol or when you are working with specialized controls—for example, controls that are not backed by a view.

### Adopting a Role-Specific Protocol

The first step in implementing accessibility is to identify the role-specific protocol that best matches your control’s intended behavior. For example, if your control is something that triggers actions when the user clicks on it, it should probably adopt the [NSAccessibilityButton](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton) protocol.

The accessibility API provides 18 role-specific protocols. These protocols represent the most common control types found in apps. For more information about a particular protocol, see that protocol’s reference documentation.

- [NSAccessibilityButton](https://developer.apple.com/documentation/appkit/nsaccessibilitybutton)
- [NSAccessibilityCheckBox](https://developer.apple.com/documentation/appkit/nsaccessibilitycheckbox)
- [NSAccessibilityRadioButton](https://developer.apple.com/documentation/appkit/nsaccessibilityradiobutton)
- [NSAccessibilitySwitch](https://developer.apple.com/documentation/appkit/nsaccessibilityswitch)
- [NSAccessibilityStaticText](https://developer.apple.com/documentation/appkit/nsaccessibilitystatictext)
- [NSAccessibilityNavigableStaticText](https://developer.apple.com/documentation/appkit/nsaccessibilitynavigablestatictext)
- [NSAccessibilityImage](https://developer.apple.com/documentation/appkit/nsaccessibilityimage)
- [NSAccessibilityProgressIndicator](https://developer.apple.com/documentation/appkit/nsaccessibilityprogressindicator)
- [NSAccessibilitySlider](https://developer.apple.com/documentation/appkit/nsaccessibilityslider)
- [NSAccessibilityStepper](https://developer.apple.com/documentation/appkit/nsaccessibilitystepper)
- [NSAccessibilityTable](https://developer.apple.com/documentation/appkit/nsaccessibilitytable)
- [NSAccessibilityOutline](https://developer.apple.com/documentation/appkit/nsaccessibilityoutline)
- [NSAccessibilityList](https://developer.apple.com/documentation/appkit/nsaccessibilitylist)
- [NSAccessibilityRow](https://developer.apple.com/documentation/appkit/nsaccessibilityrow)
- [NSAccessibilityLayoutArea](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutarea)
- [NSAccessibilityLayoutItem](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutitem)
- [NSAccessibilityGroup](https://developer.apple.com/documentation/appkit/nsaccessibilitygroup)
- [NSAccessibilityContainsTransientUI](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui)

After you have selected an appropriate protocol, adopt that protocol. Xcode then warn you about any missing methods. Simply implement these methods, and your control is ready to use.

> [!NOTE]
> 

The methods in these protocols represent the minimum required to act according to the specified role. If your control’s intended use closely matches the role, this may be all you need. However, you can further customize your control’s behavior both by implementing additional accessibility methods and properties, and by sending notifications to the accessibility client.

### Customizing the Role

The [NSAccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility) protocol declares all the information properties and action methods used by the accessibility API. Your control can freely adopt any of these methods or properties. You don’t need to adopt the [NSAccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility) protocol—in fact, you generally shouldn’t adopt this protocol. Accessibility clients automatically detect and use any of these methods as soon as they are available.

In particular, the role-specific protocols often require an information property’s getter method, but not its setter method. If you just implement the getter method, accessibility clients are granted read-only access to the data. If you implement both the getter and the setter, accessibility clients are granted read-write access. This allows users to modify the property’s value using an accessibility client.

> [!NOTE]
> 

For controls that store values, you often want to implement both the `accessibilityValue` and the `setAccessibilityValue:` accessor methods. Implementing `setAccessibilityValue:` lets users modify the control’s value through an accessibility client.

Additionally, if your control doesn’t quite fit any of the roles, pick the role that most-closely represents your control’s intended use, and then add other information properties and action methods needed to flesh out its desired abilities and behaviors.

### Notifying the Accessibility Client

After you adopt a role-specific protocol, Xcode’s compiler warnings lead you through the process of implementing the required information properties and action methods. However, it does not help with notifications. Controls often need to alert the accessibility clients to changes. For example, if your control’s value changes, you need to send a [NSAccessibilityValueChangedNotification](https://developer.apple.com/documentation/appkit/nsaccessibilityvaluechangednotification) notification.

These notifications do not use the standard [NSNotification](https://developer.apple.com/documentation/foundation/nsnotification) system. Instead, these notifications are sent to the accessibility client’s process using the [NSAccessibilityPostNotification](https://developer.apple.com/documentation/appkit/1529733-nsaccessibilitypostnotification) method. Review the complete list of notifications listed in _[NSAccessibility Protocol Reference](https://developer.apple.com/documentation/appkit/nsaccessibility)_, and make sure you are posting any relevant notifications as your control’s state changes.

For more information on accessibility notifications, see _[AXUIElement.h Reference](https://developer.apple.com/documentation/applicationservices/axuielement.h)_.

### Controls Without Views

The previous discussion assumes that your control inherits from [NSView](https://developer.apple.com/documentation/appkit/nsview) or one of the standard AppKit controls. In some cases, however, your controls may simply be visual elements that are drawn and managed by their containing view. If you want to make accessibility clients aware of—and able to interact with—these controls, you must create a custom [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelement) subclass to represent them.

To work properly, you must do the following:

- Instantiate your [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelement) subclass either by using the [accessibilityElementWithRole:frame:label:parent:](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1531178-element) convenience method or by setting your element’s [accessibilityRole](https://developer.apple.com/documentation/appkit/nsaccessibility/1535005-accessibilityrole), [accessibilityLabel](https://developer.apple.com/documentation/appkit/nsaccessibility/1534976-accessibilitylabel) and [accessibilityParent](https://developer.apple.com/documentation/appkit/nsaccessibility/1535040-accessibilityparent) properties.
- Either add the [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelement) subclass to its parent’s [accessibilityChildren](https://developer.apple.com/documentation/appkit/nsaccessibility/1535018-accessibilitychildren) array, or call the parent’s [accessibilityAddChildElement:](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1533717-accessibilityaddchildelement) convenience method.
- Set your [NSAccessibilityElement](https://developer.apple.com/documentation/appkit/nsaccessibilityelement) subclass’s [accessibilityFrameInParentSpace](https://developer.apple.com/documentation/appkit/nsaccessibilityelement/1569648-accessibilityframeinparentspace) property. Unlike [accessibilityFrame](https://developer.apple.com/documentation/appkit/nsaccessibility/1534939-accessibilityframe), this property ensures that your control moves with its superview.
- Adopt a role-specific protocol, customize the role, and post notifications just as you would handle any other accessible control.

[Enhancing the Accessibility of Standard AppKit Controls](EnhancingtheAccessibilityofStandardAppKitControls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrvg4wvgvzr)

[Testing for Accessibility on OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXTestingApps.html#//apple_ref/doc/uid/TP40001078-CH210-TPXREF101)
