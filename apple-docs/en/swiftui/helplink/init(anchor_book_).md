---
title: 'init(anchor:book:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/helplink/init(anchor:book:)'
source_url: 'https://developer.apple.com/documentation/swiftui/helplink/init(anchor:book:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/helplink/init%28anchor%3Abook%3A%29.json'
content_hash: 'sha256:472a1824c766715c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HelpLink](../helplink.md)

# init(anchor:book:)

<sub>Initializer</sub>

Constructs a new help link with the specified anchor and book.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)
```

## Parameters

- `anchor` — The anchor within the help book to open to.

- `book` — The specific book name to open.

## See Also

### Creating a help link

- [init(action:)](<init(action_).md>) — Constructs a new help link with the specified action.
- [init(destination:)](<init(destination_).md>) — Constructs a new help link that opens the specified destination URL.
- [init(anchor:)](<init(anchor_).md>) — Constructs a new help link with the specified anchor in the main app bundle’s book.
