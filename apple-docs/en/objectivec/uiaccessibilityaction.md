---
title: UIAccessibilityAction
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/uiaccessibilityaction
source_url: 'https://developer.apple.com/documentation/objectivec/uiaccessibilityaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/uiaccessibilityaction.json'
content_hash: 'sha256:d6134225ae5a6892'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# UIAccessibilityAction

<sub>API Collection</sub>

A set of methods that accessibility elements can use to support specific actions.

## Overview

The `UIAccessibilityAction` informal protocol provides a way for accessibility elements to support specific actions, such as selecting values in a range or scrolling through information on the screen. For example, to respond to a scrolling gesture, you implement the [- accessibilityScroll:](<nsobject-swift.class/accessibilityscroll(__).md>) method and post [pageScrolled](../uikit/uiaccessibility/notification/pagescrolled.md) with the new page status (such as “Page 3 of 9”). Or, to make an element such as a slider or picker view accessible, you first need to characterize it by including the [adjustable](../uikit/uiaccessibilitytraits/adjustable.md) trait. Then, you must implement the [- accessibilityIncrement](<nsobject-swift.class/accessibilityincrement().md>) and [- accessibilityDecrement](<nsobject-swift.class/accessibilitydecrement().md>) methods. When you do this, assistive technology users can adjust the element using gestures specific to the assistive technology.

## Topics

### Performing an action

- [- accessibilityActivate](<nsobject-swift.class/accessibilityactivate().md>) — Tells the element to activate itself and report the success or failure of the operation.
- [- accessibilityIncrement](<nsobject-swift.class/accessibilityincrement().md>) — Tells the accessibility element to increment the value of its content.
- [- accessibilityDecrement](<nsobject-swift.class/accessibilitydecrement().md>) — Tells the accessibility element to decrement the value of its content.
- [- accessibilityScroll:](<nsobject-swift.class/accessibilityscroll(__).md>) — Scrolls screen content in an application-specific way and returns the success or failure of the action.
- [- accessibilityPerformEscape](<nsobject-swift.class/accessibilityperformescape().md>) — Dismisses a modal view and returns the success or failure of the action.
- [- accessibilityPerformMagicTap](<nsobject-swift.class/accessibilityperformmagictap().md>) — Performs a salient action.

### Accessing custom actions

- [accessibilityCustomActions](nsobject-swift.class/accessibilitycustomactions.md) — An array of custom actions to display along with the built-in actions.

### Constants

- [UIAccessibilityScrollDirection](../uikit/uiaccessibilityscrolldirection.md) — The direction of a scrolling action.

## See Also

### Related Documentation

- [Accessibility Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [UIAccessibilityFocus](uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — A pair of properties to allow you to fine-tune how drags and drops are exposed to assistive technologies.
