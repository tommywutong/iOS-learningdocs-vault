---
title: MenuStyleConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menustyleconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/menustyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyleconfiguration.json'
content_hash: 'sha256:d88df7ef72b35f71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuStyleConfiguration

<sub>Structure</sub>

A configuration of a menu.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MenuStyleConfiguration
```

## Overview

Use the [init(_:)](<menu/init(__).md>) initializer of [Menu](menu.md) to create an instance using the current menu style, which you can modify to create a custom style.

For example, the following code creates a new, custom style that adds a red border to the current menu style:

```swift
struct RedBorderMenuStyle: MenuStyle {
    func makeBody(configuration: Configuration) -> some View {
        Menu(configuration)
            .border(Color.red)
    }
}
```

## Topics

### Setting the label and content

- [Label](menustyleconfiguration/label.md) — A type-erased label of a menu.
- [Content](menustyleconfiguration/content.md) — A type-erased content of a menu.

## See Also

### Styling menus

- [menuStyle(_:)](<view/menustyle(__).md>) — Sets the style for menus within this view.
- [MenuStyle](menustyle.md) — A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.
