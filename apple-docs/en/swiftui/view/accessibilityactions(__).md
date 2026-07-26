---
title: 'accessibilityActions(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityactions(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityactions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityactions%28_%3A%29.json'
content_hash: 'sha256:0d57a1c7d2f5ec10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityActions(_:)

<sub>Instance Method</sub>

Adds multiple accessibility actions to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityActions<Content>(@ContentBuilder _ content: () -> Content) -> some View where Content : View

```

## Discussion

Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. For example, this is how a dynamic number of custom action could be added to a view.

```swift
var isDraft: Bool

var body: some View {
    ContentView()
        .accessibilityActions {
            ForEach(actions) { action in
                Button {
                    action()
                } label: {
                    Text(action.title)
                }
            }

            if isDraft {
                Button {
                    // Handle Delete
                } label: {
                    Text("Delete")
                }
            }
        }
```

## See Also

### Adding actions to views

- [accessibilityAction(_:_:)](<accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(named:_:)](<accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](<accessibilityaction(intent_label_).md>) — Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](<accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(category:_:)](<accessibilityactions(category___).md>) — Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [AccessibilityActionKind](../accessibilityactionkind.md) — The structure that defines the kinds of available accessibility actions.
- [AccessibilityAdjustmentDirection](../accessibilityadjustmentdirection.md) — A directional indicator you use when making an accessibility adjustment.
- [AccessibilityActionCategory](../accessibilityactioncategory.md) — Designates an accessibility action category that is provided and named by the system.
