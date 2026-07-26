---
title: AccessoryBarButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessorybarbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/accessorybarbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessorybarbuttonstyle.json'
content_hash: 'sha256:078b96253337c00f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessoryBarButtonStyle

<sub>Structure</sub>

A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.

<sub>macOS</sub>

```swift
nonisolated struct AccessoryBarButtonStyle
```

## Overview

This is the default button style for views in accessory toolbars, which you create with [init(id:)](<toolbaritemplacement/init(id_).md>), and for searchable scopes. This style also affects other view types that you apply a button style to, like [Toggle](toggle.md), [Picker](picker.md), and [Menu](menu.md) instances.

Use [accessoryBar](primitivebuttonstyle/accessorybar.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<accessorybarbuttonstyle/init().md>) — Creates an accessory toolbar style

### Supporting types

- [makeBody(configuration:)](<accessorybarbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
