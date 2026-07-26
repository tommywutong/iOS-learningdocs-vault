---
title: LinkButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/linkbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/linkbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/linkbuttonstyle.json'
content_hash: 'sha256:08e031b7ab0ca8c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LinkButtonStyle

<sub>Structure</sub>

A button style for buttons that emulate links.

<sub>macOS</sub>

```swift
nonisolated struct LinkButtonStyle
```

## Overview

You can also use [link](primitivebuttonstyle/link.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<linkbuttonstyle/init().md>) — Creates a link button style.

### Supporting types

- [makeBody(configuration:)](<linkbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
