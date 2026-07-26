---
title: UIAccessibility
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility-protocol
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility-protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility-protocol.json'
content_hash: 'sha256:8c807bf35f225750'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Accessibility for UIKit](accessibility-for-uikit.md)

# UIAccessibility

<sub>API Collection</sub>

A set of methods that provides accessibility information about views and controls in an app’s user interface.

## Overview

The `UIAccessibility` informal protocol provides accessibility information about an app’s user interface elements. Assistive apps, such as VoiceOver, convey this information to users with disabilities to help them use the app.

Standard UIKit controls and views implement the `UIAccessibility` methods and are accessible to assistive apps by default. This means that if your app uses only standard controls and views, such as [UIButton](uibutton.md), [UISegmentedControl](uisegmentedcontrol.md), and [UITableView](uitableview.md), you need only supply app-specific details when the default values are incomplete. You can do this by setting these values in Interface Builder or by setting the properties in this informal protocol.

The [UIAccessibilityElement](uiaccessibilityelement.md) class, which represents custom user interface objects, also implements the `UIAccessibility` informal protocol. If you create a completely custom [UIView](https://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) subclass, you might need to create an instance of [UIAccessibilityElement](uiaccessibilityelement.md) to represent it. In this case, you’d support all the `UIAccessibility` properties to correctly set and return the accessibility element’s properties.

## Topics

### Supporting basic accessibility

- [isAccessibilityElement](../objectivec/nsobject-swift.class/isaccessibilityelement.md)
- [accessibilityLabel](../objectivec/nsobject-swift.class/accessibilitylabel.md)
- [accessibilityValue](../objectivec/nsobject-swift.class/accessibilityvalue.md)
- [accessibilityHint](../objectivec/nsobject-swift.class/accessibilityhint.md)
- [accessibilityTraits](../objectivec/nsobject-swift.class/accessibilitytraits.md)
- [UIAccessibilityTraits](uiaccessibilitytraits.md) — Constants that describe how an accessibility element behaves.

### Defining accessibility text and language

- [Speech attributes for attributed strings](speech-attributes-for-attributed-strings.md) — Apply attributes to text in an attributed string to modify the pronunciation of that text.
- [Text attributes for attributed strings](text-attributes-for-attributed-strings.md) — Apply attributes to text in an attributed string to convey extra information about the text.
- [accessibilityHeaderElements](../objectivec/nsobject-swift.class/accessibilityheaderelements.md)
- [accessibilityAttributedHint](../objectivec/nsobject-swift.class/accessibilityattributedhint.md)
- [accessibilityAttributedLabel](../objectivec/nsobject-swift.class/accessibilityattributedlabel.md)
- [accessibilityLanguage](../objectivec/nsobject-swift.class/accessibilitylanguage.md)
- [accessibilityTextualContext](../objectivec/nsobject-swift.class/accessibilitytextualcontext.md)
- [accessibilityUserInputLabels](../objectivec/nsobject-swift.class/accessibilityuserinputlabels.md)
- [accessibilityAttributedUserInputLabels](../objectivec/nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [accessibilityAttributedValue](../objectivec/nsobject-swift.class/accessibilityattributedvalue.md)

### Configuring behavior

- [accessibilityCustomRotors](../objectivec/nsobject-swift.class/accessibilitycustomrotors.md)
- [accessibilityElementsHidden](../objectivec/nsobject-swift.class/accessibilityelementshidden.md)
- [accessibilityRespondsToUserInteraction](../objectivec/nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [accessibilityViewIsModal](../objectivec/nsobject-swift.class/accessibilityviewismodal.md)
- [shouldGroupAccessibilityChildren](../objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren.md)
- [accessibilityDirectTouchOptions](../objectivec/nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [DirectTouchOptions](uiaccessibility/directtouchoptions.md) — Constants that configure how VoiceOver produces audio for direct touch areas.

### Handling notifications

- [Notification names](notification-names.md) — The names of notifications that the accessibility system generates.
- [Notification dictionary keys](notification-dictionary-keys.md) — Handle notifications with keys in the user info dictionary.
- [Notification](uiaccessibility/notification.md) — An accessibility notification that an app can send.
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — Posts a notification to assistive apps.

### Navigating elements

- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [accessibilityActivationPoint](../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityFocusedUIElement](../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](../objectivec/nsobject-swift.class/accessibilityframe.md)
- [accessibilityHitTest(_:)](<../objectivec/nsobject-swift.class/accessibilityhittest(__).md>)
- [accessibilityNavigationStyle](../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md) — Constants that describe how to navigate an object’s elements with an assistive app.
- [accessibilityPath](../objectivec/nsobject-swift.class/accessibilitypath.md)
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
- [ZoomType](uiaccessibility/zoomtype.md) — The types of system Zoom that can be in effect.
- [UIGuidedAccessAccessibilityFeatureAssistiveTouch](uiguidedaccessaccessibilityfeature/assistivetouch.md) — The AssistiveTouch accessibility feature.

### Supporting types

- [AXArrayReturnBlock](axarrayreturnblock.md)
- [AXAttributedStringArrayReturnBlock](axattributedstringarrayreturnblock.md)
- [AXAttributedStringReturnBlock](axattributedstringreturnblock.md)
- [AXBoolReturnBlock](axboolreturnblock.md)
- [AXContainerTypeReturnBlock](axcontainertypereturnblock.md)
- [AXCustomActionsReturnBlock](axcustomactionsreturnblock.md)
- [AXCustomRotorsReturnBlock](axcustomrotorsreturnblock.md)
- [AXNavigationStyleReturnBlock](axnavigationstylereturnblock.md)
- [AXObjectReturnBlock](axobjectreturnblock.md)
- [AXPathReturnBlock](axpathreturnblock.md)
- [AXPointReturnBlock](axpointreturnblock.md)
- [AXRectReturnBlock](axrectreturnblock.md)
- [AXStringArrayReturnBlock](axstringarrayreturnblock.md)
- [AXStringReturnBlock](axstringreturnblock.md)
- [AXTextualContextReturnBlock](axtextualcontextreturnblock.md)
- [AXTraitsReturnBlock](axtraitsreturnblock.md)
- [AXUITextInputReturnBlock](axuitextinputreturnblock.md)
- [AXVoidReturnBlock](axvoidreturnblock.md)
- [UIAccessibility](uiaccessibility.md) — A namespace for accessibility symbols for UIKit apps.

## See Also

### Related Documentation

- [Accessibility](../accessibility.md) — Make your apps accessible to everyone who uses Apple devices.
- [Accessibility for UIKit](accessibility-for-uikit.md) — Make your UIKit apps accessible to everyone who uses iOS and tvOS.

### Essentials

- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md) — Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.
