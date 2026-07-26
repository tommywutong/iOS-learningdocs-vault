---
title: WindowVisibilityToggle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowvisibilitytoggle
source_url: 'https://developer.apple.com/documentation/swiftui/windowvisibilitytoggle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowvisibilitytoggle.json'
content_hash: 'sha256:7bd598db1f2e0bd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowVisibilityToggle

<sub>Structure</sub>

A specialized button for toggling the visibility of a window.

<sub>macOS</sub>

```swift
nonisolated struct WindowVisibilityToggle<Label> where Label : View
```

## Overview

This is most commonly used in the main menu, where it can toggle the visibility of `Window` and `UtilityWindow` windows. The default label uses the title of the window in the format of “Show ” and “Hide ” depending on the current visibility of the window.

A keyboard shortcut can be assigned to this button.

The below example demonstrates how a main menu can be constructed with visibility buttons, replacing the default commands added by `Window` and `Utility Window`:

```swift
 struct PhotoEditor: App {
     var body: some Scene {
         WindowGroup {
             PhotoEditor()
         }
         .commands {
            CommandGroup(before: .textFormatting) {
                Section {
                    WindowVisibilityToggle(windowID: "formatting")
                        .keyboardShortcut("t", modifiers: [.command, .shift])

                    // other custom/image formatting controls
                }
            }
            CommandGroup(before: .sidebar) {
                Section {
                    WindowVisibilityToggle(windowID: "photo-library")

                    // other controls for showing/hiding UI
                }
            }
         }

         UtilityWindow("Formatting Style", id: "formatting") {
             TextAndImageFormatForm()
         }
         .commandsRemoved()

         Window("Photo Library", id: "photo-library") {
             PhotoInfoViewer()
         }
         .commandsRemoved()
     }
 }
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a window visibility toggle

- [init(windowID:)](<windowvisibilitytoggle/init(windowid_).md>) — Create a window visibility toggle to alter the visibility of a specific window.

### Supporting types

- [DefaultWindowVisibilityToggleLabel](defaultwindowvisibilitytogglelabel.md) — The default label of a window visibility toggle.

## See Also

### Configuring window visibility

- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
