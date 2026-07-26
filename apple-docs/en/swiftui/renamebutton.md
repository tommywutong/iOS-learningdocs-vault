---
title: RenameButton
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/renamebutton
source_url: 'https://developer.apple.com/documentation/swiftui/renamebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/renamebutton.json'
content_hash: 'sha256:1f2f3664a470eea9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RenameButton

<sub>Structure</sub>

A button that triggers a standard rename action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct RenameButton<Label> where Label : View
```

## Overview

A rename button receives its action from the environment. Use the [renameAction(_:)](<view/renameaction(__).md>) modifier to set the action. The system disables the button if you don’t define an action.

```swift
struct RowView: View {
    @State private var text = ""
    @FocusState private var isFocused: Bool

    var body: some View {
        TextField(text: $text) {
            Text("Prompt")
        }
        .focused($isFocused)
        .contextMenu {
            RenameButton()
            // ... your own custom actions
        }
        .renameAction { isFocused = true }
    }
}
```

When someone taps the rename button in the context menu, the rename action focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation title modifier automatically configures the environment with the appropriate rename action.

```swift
ContentView()
    .navigationTitle($contentTitle)
    .toolbarTitleMenu {
        // ... your own custom actions
        RenameButton()
    }
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating an rename button

- [init()](<renamebutton/init().md>) — Creates a rename button.

## See Also

### Creating special-purpose buttons

- [EditButton](editbutton.md) — A button that toggles the edit mode environment value.
- [PasteButton](pastebutton.md) — A system button that reads items from the pasteboard and delivers it to a closure.
