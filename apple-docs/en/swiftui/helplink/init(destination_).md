---
title: 'init(destination:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/helplink/init(destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/helplink/init(destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/helplink/init%28destination%3A%29.json'
content_hash: 'sha256:d8f3876e962acbf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HelpLink](../helplink.md)

# init(destination:)

<sub>Initializer</sub>

Constructs a new help link that opens the specified destination URL.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init(destination: URL)
```

## Parameters

- `destination` — The URL to open when the button is clicked.

## Discussion

Use this initializer when you want the standard help button appearance that opens a link to a website.

You can override the default behavior when the button is clicked by setting the [openURL](../environmentvalues/openurl.md) environment value with a custom [OpenURLAction](../openurlaction.md).

## See Also

### Creating a help link

- [init(action:)](<init(action_).md>) — Constructs a new help link with the specified action.
- [init(anchor:)](<init(anchor_).md>) — Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor:book:)](<init(anchor_book_).md>) — Constructs a new help link with the specified anchor and book.
