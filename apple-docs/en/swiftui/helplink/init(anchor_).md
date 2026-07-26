---
title: 'init(anchor:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/helplink/init(anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/helplink/init(anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/helplink/init%28anchor%3A%29.json'
content_hash: 'sha256:8914765fe6b1e057'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HelpLink](../helplink.md)

# init(anchor:)

<sub>Initializer</sub>

Constructs a new help link with the specified anchor in the main app bundle’s book.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init(anchor: NSHelpManager.AnchorName)
```

## Parameters

- `anchor` — The anchor within the help book to open to.

## Discussion

The main app bundle book name is defined by the `CFBundleHelpBookName` key in its Info.plist file.

## See Also

### Creating a help link

- [init(action:)](<init(action_).md>) — Constructs a new help link with the specified action.
- [init(destination:)](<init(destination_).md>) — Constructs a new help link that opens the specified destination URL.
- [init(anchor:book:)](<init(anchor_book_).md>) — Constructs a new help link with the specified anchor and book.
