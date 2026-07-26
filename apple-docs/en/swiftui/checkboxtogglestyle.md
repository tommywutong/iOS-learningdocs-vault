---
title: CheckboxToggleStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/checkboxtogglestyle
source_url: 'https://developer.apple.com/documentation/swiftui/checkboxtogglestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/checkboxtogglestyle.json'
content_hash: 'sha256:6a795edd64dd2663'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CheckboxToggleStyle

<sub>Structure</sub>

A toggle style that displays a checkbox followed by its label.

<sub>macOS</sub>

```swift
nonisolated struct CheckboxToggleStyle
```

## Overview

Use the [checkbox](togglestyle/checkbox.md) static variable to create this style:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```

## Relationships

- **Conforms To**: [ToggleStyle](togglestyle.md)

## Topics

### Creating the toggle style

- [init()](<checkboxtogglestyle/init().md>) — Creates a checkbox toggle style.

### Supporting types

- [makeBody(configuration:)](<checkboxtogglestyle/makebody(configuration_).md>) — Creates a view that represents the body of a toggle checkbox.

## See Also

### Supporting types

- [DefaultToggleStyle](defaulttogglestyle.md) — The default toggle style.
- [ButtonToggleStyle](buttontogglestyle.md) — A toggle style that displays as a button with its label as the title.
- [SwitchToggleStyle](switchtogglestyle.md) — A toggle style that displays a leading label and a trailing switch.
