---
title: NSHostingMenu
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 14.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingmenu
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingmenu.json'
content_hash: 'sha256:c896c45aedb7604e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSHostingMenu

<sub>Class</sub>

An AppKit menu with menu items that are defined by a SwiftUI View.

<sub>macOS</sub>

```swift
class NSHostingMenu<Content> where Content : View
```

## Overview

Because `NSHostingMenu` is an `NSMenu` subclass, you can integrate it into your existing AppKit view hierarchies that display menus. For example, you can set a hosting menu as an AppKit view’s context menu.

A hosting menu’s `items` property will be updated based on the content of the provided `rootView`, so direct mutations to the item array are not allowed, even if done using methods like `addItem` on the menu itself.

SwiftUI views hosted in the menu will be styled and behave identically to views in a [Menu](menu.md) or `View/contextMenu`. Make sure to use a `Group` or a view with multiple subviews as your top level container instead of an `HStack` or other container that would attempt to place all of your actions in a single menu item.

> [!note] Note
> When used as the menu of an `NSPopUpButton`, make sure `NSPopUpButtonCell.usesItemFromMenu` is set to `false`. When using a hosting menu with macOS 14, do not change the value of the `delegate` property. (Setting the delegate is permitted on macOS 15 and newer.)

For example, the following code would set up the first part of the Finder’s context menu, both in the Action button in the toolbar and as a context menu:

```swift
struct FileOrFolderContextMenu: View {
    let url: URL
    var body: some View {
        Section {
            if url.hasDirectoryPath {
                Button("Open in New Tab") { ... }
            } else {
                Button("Open") { ... }
                Menu("Open With") { ... }
            }
        }
        Section {
            Button("Move to Trash") { ... }
        }
        Section {
            Button("Get Info") { ... }
            Button("Rename") { ... }
            if url.pathExtension != "zip" {
                Button("Compress “\(url.lastPathComponent)”") { ... }
            }
            // ...
        }
    }
}

// In the toolbar setup:
let popUpButton = NSPopUpButton(frame: .zero, pullsDown: true)
(popUpButton.cell as! NSPopUpButtonCell).usesItemFromMenu = false
popUpButton.menu = NSHostingMenu(rootView: Group {
    Button("New Folder") { ... }
    FileOrFolderContextMenu(url: selectedURL)
})

// In the column view:
List(directoryContents, selection: $selection) { entry in
    DirectoryEntryRow(entry: entry)
        .contextMenu {
            FileOrFolderContextMenu(url: entry.url)
        }
}
```

## Relationships

- **Inherits From**: [NSMenu](../appkit/nsmenu.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## Topics

### Initializers

- [init(rootView:)](<nshostingmenu/init(rootview_).md>) — Creates a hosting menu object that wraps the specified SwiftUI view.

### Instance Properties

- [rootView](nshostingmenu/rootview.md) — The root view of the SwiftUI view hierarchy managed by this menu.

### Instance Methods

- [copy(with:)](<nshostingmenu/copy(with_).md>)

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](nshostingcontroller.md) — An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](nshostingview.md) — An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingSizingOptions](nshostingsizingoptions.md) — Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md) — Options for how hosting views and controllers manage aspects of the associated window.
