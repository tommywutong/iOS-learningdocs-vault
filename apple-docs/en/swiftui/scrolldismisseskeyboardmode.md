---
title: ScrollDismissesKeyboardMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolldismisseskeyboardmode
source_url: 'https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolldismisseskeyboardmode.json'
content_hash: 'sha256:922938f6f9e8470f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollDismissesKeyboardMode

<sub>Structure</sub>

The ways that scrollable content can interact with the software keyboard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
struct ScrollDismissesKeyboardMode
```

## Overview

Use this type in a call to the [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) modifier to specify the dismissal behavior of scrollable views.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting modes

- [automatic](scrolldismisseskeyboardmode/automatic.md) — Determine the mode automatically based on the surrounding context.
- [immediately](scrolldismisseskeyboardmode/immediately.md) — Dismiss the keyboard as soon as scrolling starts.
- [interactively](scrolldismisseskeyboardmode/interactively.md) — Enable people to interactively dismiss the keyboard as part of the scroll operation.
- [never](scrolldismisseskeyboardmode/never.md) — Never dismiss the keyboard automatically as a result of scrolling.

## See Also

### Interacting with a software keyboard

- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [scrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md) — The way that scrollable content interacts with the software keyboard.
