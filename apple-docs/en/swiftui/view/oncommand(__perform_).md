---
title: 'onCommand(_:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncommand(_:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncommand(_:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncommand%28_%3Aperform%3A%29.json'
content_hash: 'sha256:5e2251e9bad71439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCommand(_:perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the given selector.

<sub>macOS</sub>

```swift
nonisolated func onCommand(_ selector: Selector, perform action: (() -> Void)?) -> some View

```

## Parameters

- `selector` — The selector to register for `action`.

- `action` — The action to perform. If `action` is `nil`, `command` keeps its association with this view but doesn’t trigger.

## Return Value

A view that triggers `action` when the `command` occurs.

## Discussion

This view or one of the views it contains must be in focus in order for the action to trigger. Other actions for the same command on views _closer_ to the view in focus take priority, potentially overriding this action.

## See Also

### Responding to commands

- [onMoveCommand(perform:)](<onmovecommand(perform_).md>) — Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [onDeleteCommand(perform:)](<ondeletecommand(perform_).md>) — Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [pageCommand(value:in:step:)](<pagecommand(value_in_step_).md>) — Steps a value through a range in response to page up or page down commands.
- [onExitCommand(perform:)](<onexitcommand(perform_).md>) — Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [onPlayPauseCommand(perform:)](<onplaypausecommand(perform_).md>) — Adds an action to perform in response to the system’s Play/Pause command.
- [MoveCommandDirection](../movecommanddirection.md) — Specifies the direction of an arrow key movement.
