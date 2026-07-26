---
title: UIAccessibilityFocus
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/uiaccessibilityfocus
source_url: 'https://developer.apple.com/documentation/objectivec/uiaccessibilityfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/uiaccessibilityfocus.json'
content_hash: 'sha256:f7a1460c6dade60b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# UIAccessibilityFocus

<sub>API Collection</sub>

An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.

## Overview

VoiceOver and other assistive technologies place a virtual focus on elements, which allows users to inspect an element without activating it. If you know the current location of the virtual focus, you can optimize the user experience for assistive technology users. For example, if your application expects people to tap once to select an object and then double-tap to activate it, VoiceOver users must make an extra tap to focus VoiceOver on the object before tapping to select it. To improve the VoiceOver user’s experience, you can move selection to an element at the same time VoiceOver focuses on the element. In this way, the user can activate the element without having to tap again to select the element.

## Topics

### Getting focus information

- [- accessibilityElementDidBecomeFocused](<nsobject-swift.class/accessibilityelementdidbecomefocused().md>) — Sent after an assistive technology has set its virtual focus on the accessibility element.
- [- accessibilityElementDidLoseFocus](<nsobject-swift.class/accessibilityelementdidlosefocus().md>) — Sent after an assistive technology has removed its virtual focus from an accessibility element.
- [- accessibilityElementIsFocused](<nsobject-swift.class/accessibilityelementisfocused().md>) — Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers().md>) — Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.

## See Also

### Related Documentation

- [Accessibility Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [UIAccessibilityAction](uiaccessibilityaction.md) — A set of methods that accessibility elements can use to support specific actions.
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — A pair of properties to allow you to fine-tune how drags and drops are exposed to assistive technologies.
