---
title: BorderlessButtonMenuStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/borderlessbuttonmenustyle
source_url: 'https://developer.apple.com/documentation/swiftui/borderlessbuttonmenustyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderlessbuttonmenustyle.json'
content_hash: 'sha256:43cb8725a3064b91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BorderlessButtonMenuStyle

<sub>Structure</sub>

A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

> [!warning] Deprecated
> Use [menuStyle(_:)](<view/menustyle(__).md>) with [button](menustyle/button.md) and [buttonStyle(_:)](<view/buttonstyle(__)-66fbx.md>) with [borderless](primitivebuttonstyle/borderless.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated struct BorderlessButtonMenuStyle
```

## Overview

Use [borderlessButton](menustyle/borderlessbutton.md) to construct this style.

## Relationships

- **Conforms To**: [MenuStyle](menustyle.md)

## Topics

### Creating a bordeless button menu style

- [init()](<borderlessbuttonmenustyle/init().md>) — Creates a borderless button menu style. _(deprecated)_
- [init(showsMenuIndicator:)](<borderlessbuttonmenustyle/init(showsmenuindicator_).md>) — Creates a borderless button menu style, specifying whether to show a visual menu indicator. _(deprecated)_

## See Also

### Supporting types

- [DefaultMenuStyle](defaultmenustyle.md) — The default menu style, based on the menu’s context.
- [ButtonMenuStyle](buttonmenustyle.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [BorderedButtonMenuStyle](borderedbuttonmenustyle.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_
