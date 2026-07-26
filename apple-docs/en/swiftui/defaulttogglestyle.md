---
title: DefaultToggleStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaulttogglestyle
source_url: 'https://developer.apple.com/documentation/swiftui/defaulttogglestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaulttogglestyle.json'
content_hash: 'sha256:ab2a23f41fe1481e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultToggleStyle

<sub>Structure</sub>

The default toggle style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct DefaultToggleStyle
```

## Overview

Use the [automatic](togglestyle/automatic.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.automatic)
```

## Relationships

- **Conforms To**: [ToggleStyle](togglestyle.md)

## Topics

### Creating the toggle style

- [init()](<defaulttogglestyle/init().md>) — Creates a default toggle style.

### Supporting types

- [makeBody(configuration:)](<defaulttogglestyle/makebody(configuration_).md>) — Creates a view that represents the body of a toggle.

## See Also

### Supporting types

- [ButtonToggleStyle](buttontogglestyle.md) — A toggle style that displays as a button with its label as the title.
- [CheckboxToggleStyle](checkboxtogglestyle.md) — A toggle style that displays a checkbox followed by its label.
- [SwitchToggleStyle](switchtogglestyle.md) — A toggle style that displays a leading label and a trailing switch.
