---
title: Accessibility modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-accessibility
source_url: 'https://developer.apple.com/documentation/swiftui/view-accessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json'
content_hash: 'sha256:8815be0bb893af45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Accessibility modifiers

<sub>API Collection</sub>

Make your SwiftUI apps accessible to everyone, including people with disabilities.

## Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility support. The framework introspects common elements like navigation views, lists, text fields, sliders, buttons, and so on, and provides basic accessibility labels and values by default. You don’t have to do any extra work to enable these standard accessibility features.

SwiftUI also provides tools to help you enhance the accessibility of your app. For example, you can explicitly add accessibility labels to elements in your UI using the [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) or the [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) view modifier.

To learn more about adding accessibility features to your app, see [Accessibility fundamentals](accessibility-fundamentals.md).

## Topics

### Labels

- [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<view/accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<view/accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<view/accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<view/accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<view/accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.

### Values

- [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) — Adds a textual description of the value that the view contains.
- [accessibilityValue(_:isEnabled:)](<view/accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the view contains.

### Hints

- [accessibilityHint(_:)](<view/accessibilityhint(__).md>) — Communicates to the user what happens after performing the view’s action.
- [accessibilityHint(_:isEnabled:)](<view/accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after performing the view’s action.

### Actions

- [accessibilityAction(_:_:)](<view/accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](<view/accessibilityactions(__).md>) — Adds multiple accessibility actions to the view.
- [accessibilityActions(category:_:)](<view/accessibilityactions(category___).md>) — Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [accessibilityAction(named:_:)](<view/accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<view/accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](<view/accessibilityaction(intent_label_).md>) — Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](<view/accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<view/accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<view/accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<view/accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollStatus(_:isEnabled:)](<view/accessibilityscrollstatus(__isenabled_).md>) — Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.

### Gestures

- [accessibilityActivationPoint(_:)](<view/accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<view/accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<view/accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<view/accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<view/accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<view/accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<view/accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](<view/accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

### Elements

- [accessibilityElement(children:)](<view/accessibilityelement(children_).md>) — Creates a new accessibility element, or modifies the [AccessibilityChildBehavior](accessibilitychildbehavior.md) of the existing accessibility element.
- [accessibilityChildren(children:)](<view/accessibilitychildren(children_).md>) — Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [accessibilityHidden(_:)](<view/accessibilityhidden(__).md>) — Specifies whether to hide this view from system accessibility features.
- [accessibilityHidden(_:isEnabled:)](<view/accessibilityhidden(__isenabled_).md>) — Specifies whether to hide this view from system accessibility features.

### Custom controls

- [accessibilityRepresentation(representation:)](<view/accessibilityrepresentation(representation_).md>) — Replaces one or more accessibility elements for this view with new accessibility elements.
- [accessibilityRespondsToUserInteraction(_:)](<view/accessibilityrespondstouserinteraction(__).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<view/accessibilityrespondstouserinteraction(__isenabled_).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.

### Custom content

- [accessibilityCustomContent(_:_:importance:)](<view/accessibilitycustomcontent(____importance_).md>) — Add additional accessibility information to the view.

### Working with rotors

- [accessibilityRotor(_:entries:)](<view/accessibilityrotor(__entries_).md>) — Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<view/accessibilityrotor(__entries_entryid_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:entries:entryLabel:)](<view/accessibilityrotor(__entries_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:textRanges:)](<view/accessibilityrotor(__textranges_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.

### Configuring rotors

- [accessibilityRotorEntry(id:in:)](<view/accessibilityrotorentry(id_in_).md>) — Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [accessibilityLinkedGroup(id:in:)](<view/accessibilitylinkedgroup(id_in_).md>) — Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [accessibilitySortPriority(_:)](<view/accessibilitysortpriority(__).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

### Focus

- [accessibilityFocused(_:)](<view/accessibilityfocused(__).md>) — Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [accessibilityFocused(_:equals:)](<view/accessibilityfocused(__equals_).md>) — Modifies this view by binding its accessibility element’s focus state to the given state value.
- [accessibilityDefaultFocus(_:_:)](<view/accessibilitydefaultfocus(____).md>) — Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.

### Traits

- [accessibilityAddTraits(_:)](<view/accessibilityaddtraits(__).md>) — Adds the given traits to the view.
- [accessibilityRemoveTraits(_:)](<view/accessibilityremovetraits(__).md>) — Removes the given traits from this view.

### Identity

- [accessibilityIdentifier(_:)](<view/accessibilityidentifier(__).md>) — Uses the string you specify to identify the view.
- [accessibilityIdentifier(_:isEnabled:)](<view/accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view.

### Color inversion

- [accessibilityIgnoresInvertColors(_:)](<view/accessibilityignoresinvertcolors(__).md>) — Sets whether this view should ignore the system Smart Invert setting.

### Content descriptions

- [accessibilityTextContentType(_:)](<view/accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
- [accessibilityHeading(_:)](<view/accessibilityheading(__).md>) — Sets the accessibility level of this heading.

### VoiceOver

- [speechAdjustedPitch(_:)](<view/speechadjustedpitch(__).md>) — Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](<view/speechalwaysincludespunctuation(__).md>) — Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](<view/speechannouncementsqueued(__).md>) — Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](<view/speechspellsoutcharacters(__).md>) — Sets whether VoiceOver should speak the contents of the text view character by character.

### Charts

- [accessibilityChartDescriptor(_:)](<view/accessibilitychartdescriptor(__).md>) — Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.

### Large content

- [accessibilityShowsLargeContentViewer()](<view/accessibilityshowslargecontentviewer().md>) — Adds a default large content view to be shown by the large content viewer.
- [accessibilityShowsLargeContentViewer(_:)](<view/accessibilityshowslargecontentviewer(__).md>) — Adds a custom large content view to be shown by the large content viewer.

### Quick actions

- [accessibilityQuickAction(style:content:)](<view/accessibilityquickaction(style_content_).md>) — Adds a quick action to be shown by the system when active.
- [accessibilityQuickAction(style:isActive:content:)](<view/accessibilityquickaction(style_isactive_content_).md>) — Adds a quick action to be shown by the system when active.

### Using assistive access

- [assistiveAccessNavigationIcon(_:)](<view/assistiveaccessnavigationicon(__).md>) — Configures the view’s icon for purposes of navigation.
- [assistiveAccessNavigationIcon(systemImage:)](<view/assistiveaccessnavigationicon(systemimage_).md>) — Configures the view’s icon for purposes of navigation.

## See Also

### Configuring view elements

- [Appearance modifiers](view-appearance.md) — Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md) — Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md) — Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md) — Configure charts that you declare with Swift Charts.
