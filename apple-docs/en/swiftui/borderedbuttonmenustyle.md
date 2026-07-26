---
title: BorderedButtonMenuStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 11.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/borderedbuttonmenustyle
source_url: 'https://developer.apple.com/documentation/swiftui/borderedbuttonmenustyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderedbuttonmenustyle.json'
content_hash: 'sha256:7b21a8672b8abeee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BorderedButtonMenuStyle

<sub>Structure</sub>

A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

> [!warning] Deprecated
> Use [menuStyle(_:)](<view/menustyle(__).md>) with [button](menustyle/button.md) and [buttonStyle(_:)](<view/buttonstyle(__)-66fbx.md>) with [bordered](primitivebuttonstyle/bordered.md).

<sub>macOS</sub>

```swift
nonisolated struct BorderedButtonMenuStyle
```

## Overview

Use [borderedButton](menustyle/borderedbutton.md) to construct this style.

## Relationships

- **Conforms To**: [MenuStyle](menustyle.md)

## Topics

### Creating a bordered button menu style

- [init()](<borderedbuttonmenustyle/init().md>) — Creates a bordered button menu style. _(deprecated)_

## See Also

### Supporting types

- [DefaultMenuStyle](defaultmenustyle.md) — The default menu style, based on the menu’s context.
- [ButtonMenuStyle](buttonmenustyle.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_
