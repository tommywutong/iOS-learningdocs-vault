---
title: 'onPlayPauseCommand(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onplaypausecommand(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onplaypausecommand(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onplaypausecommand%28perform%3A%29.json'
content_hash: 'sha256:072b379df6cb17a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onPlayPauseCommand(perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the system’s Play/Pause command.

<sub>tvOS</sub>

```swift
nonisolated func onPlayPauseCommand(perform action: (() -> Void)?) -> some View

```

## See Also

### Responding to commands

- [onMoveCommand(perform:)](<onmovecommand(perform_).md>) — Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [onDeleteCommand(perform:)](<ondeletecommand(perform_).md>) — Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [pageCommand(value:in:step:)](<pagecommand(value_in_step_).md>) — Steps a value through a range in response to page up or page down commands.
- [onExitCommand(perform:)](<onexitcommand(perform_).md>) — Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [onCommand(_:perform:)](<oncommand(__perform_).md>) — Adds an action to perform in response to the given selector.
- [MoveCommandDirection](../movecommanddirection.md) — Specifies the direction of an arrow key movement.
