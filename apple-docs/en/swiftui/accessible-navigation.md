---
title: Accessible navigation
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-navigation
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-navigation.json'
content_hash: 'sha256:ada39cb31d4e8ad6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Accessible navigation

<sub>API Collection</sub>

Enable users to navigate to specific user interface elements using rotors.

## Overview

An accessibility rotor is a shortcut that enables users to quickly navigate to specific elements of the user interface, and, optionally, to specific ranges of text within those elements.

![](../../../attachments/5ceef0267b3475033df3fcff2a12dd25/accessible-navigation-hero@2x.png)

The system automatically provides rotors for many navigable elements, but you can supply additional rotors for specific purposes, or replace system rotors when they don’t automatically pick up off-screen elements, like those far down in a [LazyVStack](lazyvstack.md) or a [List](list.md).

For design guidance, see [Accessibility](../design/human-interface-guidelines/accessibility.md#Navigation) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Working with rotors

- [accessibilityRotor(_:entries:)](<view/accessibilityrotor(__entries_).md>) — Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<view/accessibilityrotor(__entries_entryid_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:entries:entryLabel:)](<view/accessibilityrotor(__entries_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:textRanges:)](<view/accessibilityrotor(__textranges_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.

### Creating rotors

- [AccessibilityRotorContent](accessibilityrotorcontent.md) — Content within an accessibility rotor.
- [AccessibilityRotorContentBuilder](accessibilityrotorcontentbuilder.md) — Result builder you use to generate rotor entry content.
- [AccessibilityRotorEntry](accessibilityrotorentry.md) — A struct representing an entry in an Accessibility Rotor.

### Replacing system rotors

- [AccessibilitySystemRotor](accessibilitysystemrotor.md) — Designates a Rotor that replaces one of the automatic, system-provided Rotors with a developer-provided Rotor.

### Configuring rotors

- [accessibilityRotorEntry(id:in:)](<view/accessibilityrotorentry(id_in_).md>) — Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [accessibilityLinkedGroup(id:in:)](<view/accessibilitylinkedgroup(id_in_).md>) — Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [accessibilitySortPriority(_:)](<view/accessibilitysortpriority(__).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

## See Also

### Accessibility

- [Accessibility fundamentals](accessibility-fundamentals.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md) — Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md) — Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md) — Describe interface elements to help people understand what they represent.
