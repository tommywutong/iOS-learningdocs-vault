---
title: BorderedButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/borderedbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/borderedbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderedbuttonstyle.json'
content_hash: 'sha256:19e07ea3c1e8b2cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BorderedButtonStyle

<sub>Structure</sub>

A button style that applies standard border artwork based on the button’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct BorderedButtonStyle
```

## Overview

You can also use [bordered](primitivebuttonstyle/bordered.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Creating the button style

- [init()](<borderedbuttonstyle/init().md>) — Creates a bordered button style.

### Supporting types

- [makeBody(configuration:)](<borderedbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

### Deprecated symbols

- [init(tint:)](<borderedbuttonstyle/init(tint_).md>) — Creates a bordered button style with a tint color. _(deprecated)_

## See Also

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
