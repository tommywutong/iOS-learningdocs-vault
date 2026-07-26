---
title: scrollDismissesKeyboardMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode.json'
content_hash: 'sha256:a6b01a0008e82121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# scrollDismissesKeyboardMode

<sub>Instance Property</sub>

The way that scrollable content interacts with the software keyboard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode { get set }
```

## Discussion

The default value is [automatic](../scrolldismisseskeyboardmode/automatic.md). Use the [scrollDismissesKeyboard(_:)](<../view/scrolldismisseskeyboard(__).md>) modifier to configure this property.

## See Also

### Interacting with a software keyboard

- [scrollDismissesKeyboard(_:)](<../view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [ScrollDismissesKeyboardMode](../scrolldismisseskeyboardmode.md) — The ways that scrollable content can interact with the software keyboard.
