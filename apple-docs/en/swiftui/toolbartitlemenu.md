---
title: ToolbarTitleMenu
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbartitlemenu
source_url: 'https://developer.apple.com/documentation/swiftui/toolbartitlemenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbartitlemenu.json'
content_hash: 'sha256:3d21059c6ae60792'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarTitleMenu

<sub>Structure</sub>

The title menu of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct ToolbarTitleMenu<Content> where Content : View
```

## Overview

A title menu represents common functionality that can be done on the content represented by your app’s toolbar or navigation title. This menu may be populated from your app’s commands like [saveItem](commandgroupplacement/saveitem.md) or [printItem](commandgroupplacement/printitem.md).

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu()
    }
```

You can provide your own set of actions to override this behavior.

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu {
            DuplicateButton()
            PrintButton()
        }
    }
```

In iOS and iPadOS, this will construct a menu that can be presented by tapping the navigation title in the app’s navigation bar.

## Relationships

- **Conforms To**: [CustomizableToolbarContent](customizabletoolbarcontent.md), [ToolbarContent](toolbarcontent.md)

## Topics

### Creating a toolbar title menu

- [init()](<toolbartitlemenu/init().md>) — Creates a toolbar title menu where actions are inferred from your apps commands.
- [init(content:)](<toolbartitlemenu/init(content_).md>) — Creates a toolbar title menu.

## See Also

### Setting the toolbar title menu

- [toolbarTitleMenu(content:)](<view/toolbartitlemenu(content_).md>) — Configure the title menu of a toolbar.
