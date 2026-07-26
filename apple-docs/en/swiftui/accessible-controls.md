---
title: Accessible controls
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-controls
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-controls.json'
content_hash: 'sha256:0cb89f7df23b6b91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Accessible controls

<sub>API Collection</sub>

Improve access to actions that your app can undertake.

## Overview

Help people using assistive technologies to gain access to controls in your app.

![](../../../attachments/206dea16b7574c6f5be707477407cfd3/accessible-controls-hero@2x.png)

For design guidance, see [Accessibility](../design/human-interface-guidelines/accessibility.md#Buttons-and-controls) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Adding actions to views

- [accessibilityAction(_:_:)](<view/accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](<view/accessibilityactions(__).md>) — Adds multiple accessibility actions to the view.
- [accessibilityAction(named:_:)](<view/accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<view/accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](<view/accessibilityaction(intent_label_).md>) — Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](<view/accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<view/accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<view/accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<view/accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(category:_:)](<view/accessibilityactions(category___).md>) — Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [AccessibilityActionKind](accessibilityactionkind.md) — The structure that defines the kinds of available accessibility actions.
- [AccessibilityAdjustmentDirection](accessibilityadjustmentdirection.md) — A directional indicator you use when making an accessibility adjustment.
- [AccessibilityActionCategory](accessibilityactioncategory.md) — Designates an accessibility action category that is provided and named by the system.

### Offering Quick Actions to people

- [accessibilityQuickAction(style:content:)](<view/accessibilityquickaction(style_content_).md>) — Adds a quick action to be shown by the system when active.
- [accessibilityQuickAction(style:isActive:content:)](<view/accessibilityquickaction(style_isactive_content_).md>) — Adds a quick action to be shown by the system when active.
- [AccessibilityQuickActionStyle](accessibilityquickactionstyle.md) — A type that describes the presentation style of an accessibility quick action.

### Making gestures accessible

- [accessibilityActivationPoint(_:)](<view/accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<view/accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<view/accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<view/accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<view/accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<view/accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<view/accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](<view/accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
- [AccessibilityZoomGestureAction](accessibilityzoomgestureaction.md) — Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.

### Controlling focus

- [accessibilityFocused(_:)](<view/accessibilityfocused(__).md>) — Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [accessibilityFocused(_:equals:)](<view/accessibilityfocused(__equals_).md>) — Modifies this view by binding its accessibility element’s focus state to the given state value.
- [AccessibilityFocusState](accessibilityfocusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the focus of any active accessibility technology, such as VoiceOver, changes.

### Managing interactivity

- [accessibilityRespondsToUserInteraction(_:)](<view/accessibilityrespondstouserinteraction(__).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<view/accessibilityrespondstouserinteraction(__isenabled_).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.

## See Also

### Accessibility

- [Accessibility fundamentals](accessibility-fundamentals.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md) — Enhance the legibility of content in your app’s interface.
- [Accessible descriptions](accessible-descriptions.md) — Describe interface elements to help people understand what they represent.
- [Accessible navigation](accessible-navigation.md) — Enable users to navigate to specific user interface elements using rotors.
