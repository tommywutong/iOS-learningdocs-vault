---
title: 'init(action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/helplink/init(action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/helplink/init(action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/helplink/init%28action%3A%29.json'
content_hash: 'sha256:ba1211e42136956a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HelpLink](../helplink.md)

# init(action:)

<sub>Initializer</sub>

Constructs a new help link with the specified action.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init(action: @escaping () -> Void)
```

## Parameters

- `action` — The action to perform when the user clicks the button.

## Discussion

Use this initializer when you want the standard help button appearance with a custom button action that does not open an article in an Apple Help book.

## See Also

### Creating a help link

- [init(destination:)](<init(destination_).md>) — Constructs a new help link that opens the specified destination URL.
- [init(anchor:)](<init(anchor_).md>) — Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor:book:)](<init(anchor_book_).md>) — Constructs a new help link with the specified anchor and book.
