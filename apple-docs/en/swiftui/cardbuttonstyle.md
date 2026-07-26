---
title: CardButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [tvOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/cardbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/cardbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/cardbuttonstyle.json'
content_hash: 'sha256:4008dcf7c7b321f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CardButtonStyle

<sub>Structure</sub>

A button style that doesn’t pad the content, and applies a motion effect when a button has focus.

<sub>tvOS</sub>

```swift
nonisolated struct CardButtonStyle
```

## Overview

You can also use [card](primitivebuttonstyle/card.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<cardbuttonstyle/init().md>) — Creates a style that doesn’t pad a button’s content and applies a motion effect to a focused button.

### Supporting types

- [makeBody(configuration:)](<cardbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Related Documentation

- [TVCardView](../tvuikit/tvcardview.md) — A view that responds to focus interaction with a motion effect it applies to all of its subviews.

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
