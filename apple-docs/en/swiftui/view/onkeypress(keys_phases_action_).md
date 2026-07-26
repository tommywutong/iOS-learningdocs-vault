---
title: 'onKeyPress(keys:phases:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onkeypress(keys:phases:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onkeypress(keys:phases:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onkeypress%28keys%3Aphases%3Aaction%3A%29.json'
content_hash: 'sha256:87052d20df5dc393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onKeyPress(keys:phases:action:)

<sub>Instance Method</sub>

Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases = [.down, .repeat], action: @escaping (KeyPress) -> KeyPress.Result) -> some View

```

## Parameters

- `keys` — A set of keys to match against incoming hardware keyboard events.

- `phases` — The key-press phases to match (`.down`, `.repeat`, and `.up`). The default value is `[.down, .repeat]`.

- `action` — The action to perform. The action receives a value describing the matched key event. Return `.handled` to consume the event and prevent further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds keyboard input when focused.

## See Also

### Responding to keyboard input

- [onKeyPress(_:action:)](<onkeypress(__action_).md>) — Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [onKeyPress(phases:action:)](<onkeypress(phases_action_).md>) — Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [onKeyPress(_:phases:action:)](<onkeypress(__phases_action_).md>) — Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [onKeyPress(characters:phases:action:)](<onkeypress(characters_phases_action_).md>) — Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [KeyPress](../keypress.md)
