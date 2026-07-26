---
title: MenuButton
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/menubutton
source_url: 'https://developer.apple.com/documentation/swiftui/menubutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubutton.json'
content_hash: 'sha256:870e1fa8a596814c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuButton

<sub>Structure</sub>

A button that displays a menu containing a list of choices when pressed.

> [!warning] Deprecated
> Use [Menu](menu.md) instead.

<sub>macOS</sub>

```swift
nonisolated struct MenuButton<Label, Content> where Label : View, Content : View
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a menu button

- [init(_:content:)](<menubutton/init(__content_).md>) — Creates a menu button with the specified localized title and content. _(deprecated)_
- [init(label:content:)](<menubutton/init(label_content_).md>) — Creates a menu button with the specified label and content. _(deprecated)_

### Styling a menu button

- [menuButtonStyle(_:)](<view/menubuttonstyle(__).md>) — Sets the style for menu buttons within this view. _(deprecated)_
- [MenuButtonStyle](menubuttonstyle.md) — A custom specification for the appearance and interaction of a menu button. _(deprecated)_

## See Also

### Deprecated types

- [PullDownButton](pulldownbutton.md) _(deprecated)_
- [ContextMenu](contextmenu.md) — A container for views that you present as menu items in a context menu. _(deprecated)_
