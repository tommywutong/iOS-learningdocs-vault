---
title: Accessible descriptions
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessible-descriptions
source_url: 'https://developer.apple.com/documentation/swiftui/accessible-descriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessible-descriptions.json'
content_hash: 'sha256:92285d2b49aa63ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Accessible descriptions

<sub>API Collection</sub>

Describe interface elements to help people understand what they represent.

## Overview

SwiftUI can often infer some information about your user interface elements, but you can use accessibility modifiers to provide even more information for users that need it.

![](../../../attachments/f52d60c9e7c4a20b6bbd457a3d013a84/accessible-descriptions-hero@2x.png)

For design guidance, see [Accessibility](../design/human-interface-guidelines/accessibility.md#Content-descriptions) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Applying labels

- [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<view/accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<view/accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<view/accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<view/accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<view/accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.

### Describing values

- [accessibilityValue(_:)](<view/accessibilityvalue(__).md>) — Adds a textual description of the value that the view contains.
- [accessibilityValue(_:isEnabled:)](<view/accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the view contains.

### Describing content

- [accessibilityTextContentType(_:)](<view/accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
- [accessibilityHeading(_:)](<view/accessibilityheading(__).md>) — Sets the accessibility level of this heading.
- [AccessibilityHeadingLevel](accessibilityheadinglevel.md) — The hierarchy of a heading in relation to other headings.
- [AccessibilityTextContentType](accessibilitytextcontenttype.md) — Textual context that assistive technologies can use to improve the presentation of spoken text.

### Describing charts

- [accessibilityChartDescriptor(_:)](<view/accessibilitychartdescriptor(__).md>) — Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [AXChartDescriptorRepresentable](axchartdescriptorrepresentable.md) — A type to generate an `AXChartDescriptor` object that you use to provide information about a chart and its data for an accessible experience in VoiceOver or other assistive technologies.

### Adding custom descriptions

- [accessibilityCustomContent(_:_:importance:)](<view/accessibilitycustomcontent(____importance_).md>) — Add additional accessibility information to the view.
- [AccessibilityCustomContentKey](accessibilitycustomcontentkey.md) — Key used to specify the identifier and label associated with an entry of additional accessibility information.

### Assigning traits to content

- [accessibilityAddTraits(_:)](<view/accessibilityaddtraits(__).md>) — Adds the given traits to the view.
- [accessibilityRemoveTraits(_:)](<view/accessibilityremovetraits(__).md>) — Removes the given traits from this view.
- [AccessibilityTraits](accessibilitytraits.md) — A set of accessibility traits that describe how an element behaves.

### Offering hints

- [accessibilityHint(_:)](<view/accessibilityhint(__).md>) — Communicates to the user what happens after performing the view’s action.
- [accessibilityHint(_:isEnabled:)](<view/accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after performing the view’s action.

### Configuring VoiceOver

- [speechAdjustedPitch(_:)](<view/speechadjustedpitch(__).md>) — Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](<view/speechalwaysincludespunctuation(__).md>) — Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](<view/speechannouncementsqueued(__).md>) — Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](<view/speechspellsoutcharacters(__).md>) — Sets whether VoiceOver should speak the contents of the text view character by character.

## See Also

### Accessibility

- [Accessibility fundamentals](accessibility-fundamentals.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md) — Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md) — Improve access to actions that your app can undertake.
- [Accessible navigation](accessible-navigation.md) — Enable users to navigate to specific user interface elements using rotors.
