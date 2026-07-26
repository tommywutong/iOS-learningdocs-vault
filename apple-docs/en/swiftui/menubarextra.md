---
title: MenuBarExtra
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menubarextra
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra.json'
content_hash: 'sha256:6c7179b07fcd393e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuBarExtra

<sub>Structure</sub>

A scene that renders itself as a persistent control in the system menu bar.

<sub>macOS</sub>

```swift
nonisolated struct MenuBarExtra<Label, Content> where Label : View, Content : View
```

## Overview

Use a `MenuBarExtra` when you want to provide access to commonly used functionality, even when your app is not active.

```swift
@main
struct AppWithMenuBarExtra: App {
    @AppStorage("showMenuBarExtra") private var showMenuBarExtra = true

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        MenuBarExtra(
            "App Menu Bar Extra", systemImage: "star",
            isInserted: $showMenuBarExtra)
        {
            StatusMenu()
        }
    }
}
```

Or alternatively, to create a utility app that only shows in the menu bar.

```swift
@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("Utility App", systemImage: "hammer") {
            AppMenu()
        }
    }
}
```

An app that only shows in the menu bar will be automatically terminated if the user removes the extra from the menu bar.

For apps that only show in the menu bar, a common behavior is for the app to not display its icon in either the Dock or the application switcher. To enable this behavior, set the [LSUIElement](../bundleresources/information-property-list/lsuielement.md) flag in your app’s [Information Property List](../bundleresources/information-property-list.md) file to `true`.

For more complex or data rich menu bar extras, you can use the [window](menubarextrastyle/window.md) style, which displays a popover-like window from the menu bar icon that contains standard controls. You define the layout and contents of those controls with the content that you provide:

```swift
MenuBarExtra("Utility App", systemImage: "hammer") {
    ScrollView {
        LazyVGrid(...)
    }
}
.menuBarExtraStyle(.window)
```

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Creating a menu bar extra

- [init(_:content:)](<menubarextra/init(__content_).md>) — Creates a menu bar extra with a localized resource for a localized string to use as the label. The extra defines the primary scene of an `App`.
- [init(content:label:)](<menubarextra/init(content_label_).md>) — Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](<menubarextra/init(__isinserted_content_).md>) — Creates a menu bar extra with a localized resource for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
- [init(isInserted:content:label:)](<menubarextra/init(isinserted_content_label_).md>) — Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

### Creating a menu bar extra with an image

- [init(_:image:content:)](<menubarextra/init(__image_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:image:isInserted:content:)](<menubarextra/init(__image_isinserted_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](<menubarextra/init(__systemimage_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](<menubarextra/init(__systemimage_isinserted_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.

## See Also

### Creating a menu bar extra

- [menuBarExtraStyle(_:)](<scene/menubarextrastyle(__).md>) — Sets the style for menu bar extra created by this scene.
- [MenuBarExtraStyle](menubarextrastyle.md) — A specification for the appearance and behavior of a menu bar extra scene.
