---
title: HelpLink
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/helplink
source_url: 'https://developer.apple.com/documentation/swiftui/helplink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/helplink.json'
content_hash: 'sha256:caafab4d8cde9c83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HelpLink

<sub>Structure</sub>

A button with a standard appearance that opens app-specific help documentation.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct HelpLink
```

## Overview

A help link opens documentation relevant to the context where they are used. Typically this is by opening to an anchor in an Apple Help book, but can also perform an arbitrary action such as opening a URL or opening a window.

```swift
HelpLink(anchor: "accountSetupHelp")

HelpLink {
    openURL(onlineHelpURL)
}
```

Help links have a standard appearance, as well as conventional placement within a view. When used within an alert or confirmation dialog’s actions, the help link will automatically be placed in the top trailing corner. Or when used in a sheet toolbar, the help link is automatically placed in the lower leading corner.

```swift
struct SheetContentView: View {
    var body: some View {
        Form {
             ...
        }
        .toolbar {
            ToolbarItem(.confirmationAction) {
                Button("Save") { ... }
            }
            ToolbarItem(.cancellationAction) {
                Button("Cancel") { ... }
            }
            ToolbarItem {
                HelpLink(anchor: "sheetHelp")
            }
         }
    }
}
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a help link

- [init(action:)](<helplink/init(action_).md>) — Constructs a new help link with the specified action.
- [init(destination:)](<helplink/init(destination_).md>) — Constructs a new help link that opens the specified destination URL.
- [init(anchor:)](<helplink/init(anchor_).md>) — Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor:book:)](<helplink/init(anchor_book_).md>) — Constructs a new help link with the specified anchor and book.

## See Also

### Linking to other content

- [Link](link.md) — A control for navigating to a URL.
- [ShareLink](sharelink.md) — A view that controls a sharing presentation.
- [SharePreview](sharepreview.md) — A representation of a type to display in a share preview.
- [TextFieldLink](textfieldlink.md) — A control that requests text input from the user when pressed.
