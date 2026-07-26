---
title: 'onKeyPress(_:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onkeypress(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onkeypress(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onkeypress%28_%3Aaction%3A%29.json'
content_hash: 'sha256:ce4aaf80f476c91a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onKeyPress(_:action:)

<sub>Instance Method</sub>

Performs an action if the user presses a key on a hardware keyboard while the view has focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func onKeyPress(_ key: KeyEquivalent, action: @escaping () -> KeyPress.Result) -> some View

```

## Parameters

- `key` — The key to match against incoming hardware keyboard events.

- `action` — The action to perform. Return `.handled` to consume the event and prevent further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for key-down and key-repeat events.

## See Also

### Responding to keyboard input

- [onKeyPress(phases:action:)](<onkeypress(phases_action_).md>) — Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [onKeyPress(_:phases:action:)](<onkeypress(__phases_action_).md>) — Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [onKeyPress(characters:phases:action:)](<onkeypress(characters_phases_action_).md>) — Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [onKeyPress(keys:phases:action:)](<onkeypress(keys_phases_action_).md>) — Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [KeyPress](../keypress.md)
