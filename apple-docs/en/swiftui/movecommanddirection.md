---
title: MoveCommandDirection
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.15+, tvOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/movecommanddirection
source_url: 'https://developer.apple.com/documentation/swiftui/movecommanddirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/movecommanddirection.json'
content_hash: 'sha256:f0e4fa942d98687e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MoveCommandDirection

<sub>Enumeration</sub>

Specifies the direction of an arrow key movement.

<sub>macOS, tvOS</sub>

```swift
enum MoveCommandDirection
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting move command directions

- [MoveCommandDirection.up](movecommanddirection/up.md)
- [MoveCommandDirection.down](movecommanddirection/down.md)
- [MoveCommandDirection.left](movecommanddirection/left.md)
- [MoveCommandDirection.right](movecommanddirection/right.md)

## See Also

### Responding to commands

- [onMoveCommand(perform:)](<view/onmovecommand(perform_).md>) — Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [onDeleteCommand(perform:)](<view/ondeletecommand(perform_).md>) — Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [pageCommand(value:in:step:)](<view/pagecommand(value_in_step_).md>) — Steps a value through a range in response to page up or page down commands.
- [onExitCommand(perform:)](<view/onexitcommand(perform_).md>) — Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [onPlayPauseCommand(perform:)](<view/onplaypausecommand(perform_).md>) — Adds an action to perform in response to the system’s Play/Pause command.
- [onCommand(_:perform:)](<view/oncommand(__perform_).md>) — Adds an action to perform in response to the given selector.
