---
title: BorderlessButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/borderlessbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/borderlessbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderlessbuttonstyle.json'
content_hash: 'sha256:1119c5e0503b9ce6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BorderlessButtonStyle

<sub>Structure</sub>

A button style that doesn’t apply a border.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct BorderlessButtonStyle
```

## Overview

You can also use [borderless](primitivebuttonstyle/borderless.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<borderlessbuttonstyle/init().md>) — Creates a borderless button style.

### Supporting types

- [makeBody(configuration:)](<borderlessbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
