---
title: AccessoryBarActionButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessorybaractionbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/accessorybaractionbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessorybaractionbuttonstyle.json'
content_hash: 'sha256:58c8e81146b2af76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessoryBarActionButtonStyle

<sub>Structure</sub>

A button style that you use for extra actions in an accessory toolbar.

<sub>macOS</sub>

```swift
nonisolated struct AccessoryBarActionButtonStyle
```

## Overview

Use this style for buttons that perform extra actions relative to the accessory toolbar’s main functions, like adding or editing filters. This style also affects other view types that you apply a button style to, like [Toggle](toggle.md), [Picker](picker.md), and [Menu](menu.md) instances.

Use [accessoryBarAction](primitivebuttonstyle/accessorybaraction.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<accessorybaractionbuttonstyle/init().md>) — Creates an accessory toolbar action button style

### Supporting types

- [makeBody(configuration:)](<accessorybaractionbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
