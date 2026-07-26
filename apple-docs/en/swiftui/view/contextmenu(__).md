---
title: 'contextMenu(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（7.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/contextmenu(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contextmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contextmenu%28_%3A%29.json'
content_hash: 'sha256:38adf89f362b4db7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contextMenu(_:)

<sub>Instance Method</sub>

Adds a context menu to the view.

> [!warning] Deprecated
> Use [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func contextMenu<MenuItems>(_ contextMenu: ContextMenu<MenuItems>?) -> some View where MenuItems : View

```

## Parameters

- `contextMenu` — A context menu container for views that you present as menu items in a context menu.

## Return Value

A view that can show a context menu.

## Discussion

Use this method to attach a specified context menu to a view. You can make the context menu unavailable by conditionally passing `nil` as the value for the `contextMenu`.

The example below creates a [ContextMenu](../contextmenu.md) that contains two items and passes them into the modifier. The Boolean value `shouldShowMenu`, which defaults to `true`, controls the context menu availability:

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

![A screenshot of a context menu showing two menu items: Add to Favorites, and Show in Maps.](../../../../attachments/175048e4c43b6463112139fd1c3f69c8/View-contextMenu-1-iOS@2x.png)

## See Also

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarTitle(_:displayMode:)](<navigationbartitle(__displaymode_).md>) — Sets the title and display mode in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:)](<navigationbaritems(leading_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [navigationBarHidden(_:)](<navigationbarhidden(__).md>) — Hides the navigation bar for this view. _(deprecated)_
- [statusBar(hidden:)](<statusbar(hidden_).md>) — Sets the visibility of the status bar. _(deprecated)_
