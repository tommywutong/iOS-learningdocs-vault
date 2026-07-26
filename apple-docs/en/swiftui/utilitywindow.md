---
title: UtilityWindow
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/utilitywindow
source_url: 'https://developer.apple.com/documentation/swiftui/utilitywindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/utilitywindow.json'
content_hash: 'sha256:e8bab64c52185429'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UtilityWindow

<sub>Structure</sub>

A specialized window scene that provides secondary utility to the content of the main scenes of an application.

<sub>macOS</sub>

```swift
nonisolated struct UtilityWindow<Content> where Content : View
```

## Overview

Utility windows are typically used to display controls, settings, or information associated the main content of an application, sometimes referred to as tool palettes or inspector windows. Because of this role, they have specialized behavior compared to all other windows:

- They receive `FocusedValues` from the focused main scene in an application, similar to commands in the main menu, which can be used to display information on the active content as the user focuses on different scenes.
- They have a default window level of `.floating` so they remain visible when moving focus between the main scenes.
- They hide when the window is no longer active.
- They only become focused when explicitly needed, such as clicking in the titlebar or on a focusable view.
- When focused, they can be dismissed with the Escape key.
- They are not minimizable by default.

```swift
@main
struct PhotoBrowser: App {
    var body: some Scene {
        WindowGroup {
            PhotoGallery()
        }

        UtilityWindow("Photo Info", id: "photo-info") {
            PhotoInfoViewer()
        }
    }
}

struct PhotoInfoViewer: View {
    // Automatically updates to the photo selection from whichever
    // photo gallery window is focused.
    @FocusedValue(PhotoSelection.self) private var selectedPhotos

    var body: some View {
        Text("\(selectedPhotos?.count ?? 0) photos selected")
    }
}
```

`UtilityWindow` will automatically add a menu item to show/hide itself in the “View” menu. This can be removed by applying [commandsRemoved()](<scene/commandsremoved().md>) to the utility window, and manually placing a [WindowVisibilityToggle](windowvisibilitytoggle.md) elsewhere in an app’s commands. Utility windows can also be programmatically presented with [openWindow](environmentvalues/openwindow.md) and dismissed using [dismiss](environmentvalues/dismiss.md).

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Initializers

- [init(_:id:content:)](<utilitywindow/init(__id_content_).md>) — Creates a utility window with a localized title and identifier.

## See Also

### Creating windows

- [WindowGroup](windowgroup.md) — A scene that presents a group of identically structured windows.
- [Window](window.md) — A scene that presents its content in a single, unique window.
- [WindowStyle](windowstyle.md) — A specification for the appearance and interaction of a window.
- [windowStyle(_:)](<scene/windowstyle(__).md>) — Sets the style for windows created by this scene.
