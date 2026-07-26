---
title: SwitchToggleStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 18.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/switchtogglestyle
source_url: 'https://developer.apple.com/documentation/swiftui/switchtogglestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/switchtogglestyle.json'
content_hash: 'sha256:19c17b76970d96c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SwitchToggleStyle

<sub>Structure</sub>

A toggle style that displays a leading label and a trailing switch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct SwitchToggleStyle
```

## Overview

Use the [switch](togglestyle/switch.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```

## Relationships

- **Conforms To**: [ToggleStyle](togglestyle.md)

## Topics

### Creating the toggle style

- [init()](<switchtogglestyle/init().md>) — Creates a switch toggle style.

### Supporting types

- [makeBody(configuration:)](<switchtogglestyle/makebody(configuration_).md>) — Creates a view that represents the body of a toggle switch.

### Deprecated initializers

- [init(tint:)](<switchtogglestyle/init(tint_).md>) — Creates a switch style with a tint color. _(deprecated)_

## See Also

### Supporting types

- [DefaultToggleStyle](defaulttogglestyle.md) — The default toggle style.
- [ButtonToggleStyle](buttontogglestyle.md) — A toggle style that displays as a button with its label as the title.
- [CheckboxToggleStyle](checkboxtogglestyle.md) — A toggle style that displays a checkbox followed by its label.
