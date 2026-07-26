---
title: OpenWindowAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openwindowaction
source_url: 'https://developer.apple.com/documentation/swiftui/openwindowaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openwindowaction.json'
content_hash: 'sha256:bfdaf2b348a82c7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OpenWindowAction

<sub>Structure</sub>

An action that presents a window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct OpenWindowAction
```

## Overview

Use the [openWindow](environmentvalues/openwindow.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to open a window. You call the instance directly because it defines a [callAsFunction(id:)](<openwindowaction/callasfunction(id_).md>) method that Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

```swift
@main
struct Mail: App {
    var body: some Scene {
        WindowGroup(id: "mail-viewer") {
            MailViewer()
        }
    }
}

struct NewViewerButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open new mail viewer") {
            openWindow(id: "mail-viewer")
        }
    }
}
```

You indicate which scene to open by providing one of the following:

- A string identifier that you pass through the `id` parameter, as in the above example.
- A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.
- Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type, like a [UUID](../foundation/uuid.md).

Use the first option to target either a [WindowGroup](windowgroup.md) or a [Window](window.md) scene in your app that has a matching identifier. For a `WindowGroup`, the system creates a new window for the group. If the window group presents data, the system provides the default value or `nil` to the window’s root view. If the targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a `WindowGroup` and provide a value to present. If the interface already has a window from the group that’s presenting the specified value, the system brings the window to the front. Otherwise, the system creates a new window and passes a binding to the specified value.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction(id:)](<openwindowaction/callasfunction(id_).md>) — Opens a window that’s associated with the specified identifier.
- [callAsFunction(id:value:)](<openwindowaction/callasfunction(id_value_).md>) — Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier.
- [callAsFunction(value:)](<openwindowaction/callasfunction(value_).md>) — Opens a window defined by a window group that presents the type of the specified value.

### Structures

- [SharingBehavior](openwindowaction/sharingbehavior.md)

### Instance Methods

- [callAsFunction(id:sharingBehavior:)](<openwindowaction/callasfunction(id_sharingbehavior_).md>) — Opens a window that’s associated with the specified identifier, using the specified sharing sharingBehavior..
- [callAsFunction(id:value:sharingBehavior:)](<openwindowaction/callasfunction(id_value_sharingbehavior_).md>) — Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier, using the specified sharingBehavior.
- [callAsFunction(value:sharingBehavior:)](<openwindowaction/callasfunction(value_sharingbehavior_).md>) — Opens a window defined by a window group that presents the type of the specified value, using the specified sharingBehavior.

## See Also

### Opening windows

- [Presenting windows and spaces](../visionos/presenting-windows-and-spaces.md) — Open and close the scenes that make up your app’s interface.
- [supportsMultipleWindows](environmentvalues/supportsmultiplewindows.md) — A Boolean value that indicates whether the current platform supports opening multiple windows.
- [openWindow](environmentvalues/openwindow.md) — A window presentation action stored in a view’s environment.
- [PushWindowAction](pushwindowaction.md) — An action that opens the requested window in place of the window the action is called from.
