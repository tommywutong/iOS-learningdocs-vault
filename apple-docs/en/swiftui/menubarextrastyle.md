---
title: MenuBarExtraStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menubarextrastyle
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextrastyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextrastyle.json'
content_hash: 'sha256:813e977c5fd8ec36'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuBarExtraStyle

<sub>Protocol</sub>

A specification for the appearance and behavior of a menu bar extra scene.

<sub>macOS</sub>

```swift
protocol MenuBarExtraStyle
```

## Relationships

- **Conforming Types**: [AutomaticMenuBarExtraStyle](automaticmenubarextrastyle.md), [PullDownMenuBarExtraStyle](pulldownmenubarextrastyle.md), [WindowMenuBarExtraStyle](windowmenubarextrastyle.md)

## Topics

### Getting menu bar extra styles

- [automatic](menubarextrastyle/automatic.md) — The default menu bar extra style.
- [menu](menubarextrastyle/menu.md) — A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [window](menubarextrastyle/window.md) — A menu bar extra style that renders its contents in a popover-like window.

### Supporting types

- [AutomaticMenuBarExtraStyle](automaticmenubarextrastyle.md) — The default menu bar extra style. You can also use [automatic](menubarextrastyle/automatic.md) to construct this style.
- [PullDownMenuBarExtraStyle](pulldownmenubarextrastyle.md) — A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [WindowMenuBarExtraStyle](windowmenubarextrastyle.md) — A menu bar extra style that renders its contents in a popover-like window.

## See Also

### Creating a menu bar extra

- [MenuBarExtra](menubarextra.md) — A scene that renders itself as a persistent control in the system menu bar.
- [menuBarExtraStyle(_:)](<scene/menubarextrastyle(__).md>) — Sets the style for menu bar extra created by this scene.
