---
title: ModifiedContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/modifiedcontent
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent.json'
content_hash: 'sha256:5d445501c9a16059'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ModifiedContent

<sub>Structure</sub>

A value with a modifier applied to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ModifiedContent<Content, Modifier>
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Chart3DContent](../charts/chart3dcontent.md), [Copyable](../swift/copyable.md), [CustomHoverEffect](customhovereffect.md), [DynamicMapContent](../mapkit/dynamicmapcontent.md), [DynamicTableRowContent](dynamictablerowcontent.md), [DynamicViewContent](dynamicviewcontent.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [HoverEffectContent](hovereffectcontent.md), [MapContent](../mapkit/mapcontent.md), [Scene](scene.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TableRowContent](tablerowcontent.md), [View](view.md), [ViewModifier](viewmodifier.md), [VisualEffect](visualeffect.md)

## Topics

### Creating a modified content view

- [init(content:modifier:)](<modifiedcontent/init(content_modifier_).md>) — A structure that defines the content and modifier needed to produce a new view or view modifier.
- [content](modifiedcontent/content.md) — The content that the modifier transforms into a new view or new view modifier.
- [modifier](modifiedcontent/modifier.md) — The view modifier.

### Instance Methods

- [accessibility(activationPoint:)](<modifiedcontent/accessibility(activationpoint_).md>) — Specifies the point where activations occur in the view. _(deprecated)_
- [accessibility(addTraits:)](<modifiedcontent/accessibility(addtraits_).md>) — Adds the given traits to the view. _(deprecated)_
- [accessibility(hidden:)](<modifiedcontent/accessibility(hidden_).md>) — Specifies whether to hide this view from system accessibility features. _(deprecated)_
- [accessibility(hint:)](<modifiedcontent/accessibility(hint_).md>) — Communicates to the user what happens after performing the view’s action. _(deprecated)_
- [accessibility(identifier:)](<modifiedcontent/accessibility(identifier_).md>) — Uses the specified string to identify the view. _(deprecated)_
- [accessibility(inputLabels:)](<modifiedcontent/accessibility(inputlabels_).md>) — Sets alternate input labels with which users identify a view. _(deprecated)_
- [accessibility(label:)](<modifiedcontent/accessibility(label_).md>) — Adds a label to the view that describes its contents. _(deprecated)_
- [accessibility(removeTraits:)](<modifiedcontent/accessibility(removetraits_).md>) — Removes the given traits from this view. _(deprecated)_
- [accessibility(selectionIdentifier:)](<modifiedcontent/accessibility(selectionidentifier_).md>) — Sets a selection identifier for this view’s accessibility element. _(deprecated)_
- [accessibility(sortPriority:)](<modifiedcontent/accessibility(sortpriority_).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level. _(deprecated)_
- [accessibility(value:)](<modifiedcontent/accessibility(value_).md>) — Adds a textual description of the value that the view contains. _(deprecated)_
- [accessibilityAction(_:_:)](<modifiedcontent/accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(_:intent:)](<modifiedcontent/accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:_:)](<modifiedcontent/accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(named:intent:)](<modifiedcontent/accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityActivationPoint(_:)](<modifiedcontent/accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<modifiedcontent/accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityAddTraits(_:)](<modifiedcontent/accessibilityaddtraits(__).md>) — Adds the given traits to the view.
- [accessibilityAdjustableAction(_:)](<modifiedcontent/accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityCustomContent(_:_:importance:)](<modifiedcontent/accessibilitycustomcontent(____importance_).md>) — Add additional accessibility information to the view.
- [accessibilityDirectTouch(_:options:)](<modifiedcontent/accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityDragPoint(_:description:)](<modifiedcontent/accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<modifiedcontent/accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<modifiedcontent/accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<modifiedcontent/accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityHeading(_:)](<modifiedcontent/accessibilityheading(__).md>) — Set the level of this heading.
- [accessibilityHidden(_:)](<modifiedcontent/accessibilityhidden(__).md>) — Specifies whether to hide this view from system accessibility features.
- [accessibilityHidden(_:isEnabled:)](<modifiedcontent/accessibilityhidden(__isenabled_).md>) — Specifies whether to hide this view from system accessibility features.
- [accessibilityHint(_:)](<modifiedcontent/accessibilityhint(__).md>) — Communicates to the user what happens after performing the view’s action.
- [accessibilityHint(_:isEnabled:)](<modifiedcontent/accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after performing the view’s action.
- [accessibilityIdentifier(_:)](<modifiedcontent/accessibilityidentifier(__).md>) — Uses the string you specify to identify the view.
- [accessibilityIdentifier(_:isEnabled:)](<modifiedcontent/accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view.
- [accessibilityInputLabels(_:)](<modifiedcontent/accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<modifiedcontent/accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabel(_:)](<modifiedcontent/accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<modifiedcontent/accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityRemoveTraits(_:)](<modifiedcontent/accessibilityremovetraits(__).md>) — Removes the given traits from this view.
- [accessibilityRespondsToUserInteraction(_:)](<modifiedcontent/accessibilityrespondstouserinteraction(__).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<modifiedcontent/accessibilityrespondstouserinteraction(__isenabled_).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [accessibilityScrollAction(_:)](<modifiedcontent/accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollStatus(_:isEnabled:)](<modifiedcontent/accessibilityscrollstatus(__isenabled_).md>) — Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [accessibilitySortPriority(_:)](<modifiedcontent/accessibilitysortpriority(__).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [accessibilityTextContentType(_:)](<modifiedcontent/accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
- [accessibilityValue(_:)](<modifiedcontent/accessibilityvalue(__).md>) — Adds a textual description of the value that the view contains.
- [accessibilityValue(_:isEnabled:)](<modifiedcontent/accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the view contains.
- [accessibilityZoomAction(_:)](<modifiedcontent/accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

## See Also

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [ViewModifier](viewmodifier.md) — A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](emptymodifier.md) — An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [EnvironmentalModifier](environmentalmodifier.md) — A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — A namespace for various manipulable related types.
