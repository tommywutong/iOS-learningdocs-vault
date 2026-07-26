---
title: 'accessibilityActions(category:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityactions(category:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityactions(category:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityactions%28category%3A_%3A%29.json'
content_hash: 'sha256:59473e57805401f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityActions(category:_:)

<sub>Instance Method</sub>

Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityActions<Content>(category: AccessibilityActionCategory, @ContentBuilder _ content: () -> Content) -> some View where Content : View

```

## Parameters

- `category` — The category the accessibility actions are grouped by.

- `content` — The accessibility actions added to the view.

## Discussion

Var body: some View { EditorView() .accessibilityActions(category: .edit) { ForEach(editActions) { action in Button(action.title) { action() } } if hasTextSuggestions { Button(“Show Text Suggestions”) { presentTextSuggestions() } } } }

## See Also

### Adding actions to views

- [accessibilityAction(_:_:)](<accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](<accessibilityactions(__).md>) — Adds multiple accessibility actions to the view.
- [accessibilityAction(named:_:)](<accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](<accessibilityaction(intent_label_).md>) — Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](<accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [AccessibilityActionKind](../accessibilityactionkind.md) — The structure that defines the kinds of available accessibility actions.
- [AccessibilityAdjustmentDirection](../accessibilityadjustmentdirection.md) — A directional indicator you use when making an accessibility adjustment.
- [AccessibilityActionCategory](../accessibilityactioncategory.md) — Designates an accessibility action category that is provided and named by the system.
