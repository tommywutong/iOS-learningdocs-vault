---
title: ContextMenu
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（7.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/contextmenu
source_url: 'https://developer.apple.com/documentation/swiftui/contextmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contextmenu.json'
content_hash: 'sha256:0c7e26c298a66da0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContextMenu

<sub>Structure</sub>

A container for views that you present as menu items in a context menu.

> [!warning] Deprecated
> Use [contextMenu(menuItems:)](<view/contextmenu(menuitems_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct ContextMenu<MenuItems> where MenuItems : View
```

## Overview

A context menu view allows you to present a situationally specific menu that enables taking actions relevant to the current task.

You can create a context menu by first defining a `ContextMenu` container with the controls that represent the actions people can take, and then using the [contextMenu(_:)](<view/contextmenu(__).md>) view modifier to apply the menu to a view.

The example below creates and applies a two item context menu container to a [Text](text.md) view. The Boolean value `shouldShowMenu`, which defaults to true, controls the availability of context menu:

```swift
private let menuItems = ContextMenu {
    Button {
        // Add this item to a list of favorites.
    } label: {
        Label("Add to Favorites", systemImage: "heart")
    }
    Button {
        // Open Maps and center it on this item.
    } label: {
        Label("Show in Maps", systemImage: "mappin")
    }
}

private struct ContextMenuMenuItems: View {
    @State private var shouldShowMenu = true

    var body: some View {
        Text("Turtle Rock")
            .contextMenu(shouldShowMenu ? menuItems : nil)
    }
}
```

![A screenshot of a context menu showing two menu items: Add to Favorites, and Show in Maps.](../../../attachments/175048e4c43b6463112139fd1c3f69c8/View-contextMenu-1-iOS@2x.png)

## Topics

### Creating a context menu

- [init(menuItems:)](<contextmenu/init(menuitems_).md>) — Creates a context menu. _(deprecated)_

## See Also

### Deprecated types

- [MenuButton](menubutton.md) — A button that displays a menu containing a list of choices when pressed. _(deprecated)_
- [PullDownButton](pulldownbutton.md) _(deprecated)_
