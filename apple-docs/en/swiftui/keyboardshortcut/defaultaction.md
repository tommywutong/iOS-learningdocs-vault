---
title: defaultAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/defaultaction
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/defaultaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/defaultaction.json'
content_hash: 'sha256:631759aebb6a8a77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyboardShortcut](../keyboardshortcut.md)

# defaultAction

<sub>Type Property</sub>

The standard keyboard shortcut for the default button, consisting of the Return (↩) key and no modifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let defaultAction: KeyboardShortcut
```

## Discussion

On macOS, the default button is designated with special coloration. If more than one control is assigned this shortcut, only the first one is emphasized.

## See Also

### Getting standard shortcuts

- [cancelAction](cancelaction.md) — The standard keyboard shortcut for cancelling the in-progress action or dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.
