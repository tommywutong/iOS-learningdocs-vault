---
title: 'accessibilityAction(intent:label:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityaction(intent:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityaction(intent:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityaction%28intent%3Alabel%3A%29.json'
content_hash: 'sha256:5814f97c479ebc2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityAction(intent:label:)

<sub>Instance Method</sub>

Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityAction<I, Label>(intent: I, @ViewBuilder label: () -> Label) -> some View where I : AppIntent, Label : View

```

## See Also

### Adding actions to views

- [accessibilityAction(_:_:)](<accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](<accessibilityactions(__).md>) — Adds multiple accessibility actions to the view.
- [accessibilityAction(named:_:)](<accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(_:intent:)](<accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(category:_:)](<accessibilityactions(category___).md>) — Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [AccessibilityActionKind](../accessibilityactionkind.md) — The structure that defines the kinds of available accessibility actions.
- [AccessibilityAdjustmentDirection](../accessibilityadjustmentdirection.md) — A directional indicator you use when making an accessibility adjustment.
- [AccessibilityActionCategory](../accessibilityactioncategory.md) — Designates an accessibility action category that is provided and named by the system.
