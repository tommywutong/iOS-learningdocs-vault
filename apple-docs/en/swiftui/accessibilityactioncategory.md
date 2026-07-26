---
title: AccessibilityActionCategory
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityactioncategory
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityactioncategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityactioncategory.json'
content_hash: 'sha256:11efc7955c59934f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityActionCategory

<sub>Structure</sub>

Designates an accessibility action category that is provided and named by the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityActionCategory
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<accessibilityactioncategory/init(__).md>) — Creates a custom action category labeled by `nameResource`.

### Type Properties

- [default](accessibilityactioncategory/default.md) — An accessibility action category for the default actions of a view. This category replaces the system provided actions rotor for accessibility technologies like VoiceOver.
- [edit](accessibilityactioncategory/edit.md) — An accessibility action category for associating actions related to editing text. This category replaces the system provided Edit actions for accessibility technologies like VoiceOver.

## See Also

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
