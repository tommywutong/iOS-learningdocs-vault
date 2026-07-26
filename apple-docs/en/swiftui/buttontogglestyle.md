---
title: ButtonToggleStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttontogglestyle
source_url: 'https://developer.apple.com/documentation/swiftui/buttontogglestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttontogglestyle.json'
content_hash: 'sha256:d82a74fedd27446b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonToggleStyle

<sub>Structure</sub>

A toggle style that displays as a button with its label as the title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated struct ButtonToggleStyle
```

## Overview

You can also use [button](togglestyle/button.md) to construct this style.

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```

## Relationships

- **Conforms To**: [ToggleStyle](togglestyle.md)

## Topics

### Creating the toggle style

- [init()](<buttontogglestyle/init().md>) — Creates a button toggle style.

### Supporting types

- [makeBody(configuration:)](<buttontogglestyle/makebody(configuration_).md>) — Creates a view that represents the body of a toggle button.

## See Also

### Supporting types

- [DefaultToggleStyle](defaulttogglestyle.md) — The default toggle style.
- [CheckboxToggleStyle](checkboxtogglestyle.md) — A toggle style that displays a checkbox followed by its label.
- [SwitchToggleStyle](switchtogglestyle.md) — A toggle style that displays a leading label and a trailing switch.
