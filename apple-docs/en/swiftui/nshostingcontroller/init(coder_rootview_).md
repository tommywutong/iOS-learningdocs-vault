---
title: 'init(coder:rootView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingcontroller/init(coder:rootview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/init(coder:rootview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/init%28coder%3Arootview%3A%29.json'
content_hash: 'sha256:a5f05d660c793128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# init(coder:rootView:)

<sub>Initializer</sub>

Creates a hosting controller object from an archive and the specified SwiftUI view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init?(coder: NSCoder, rootView: Content)
```

## Parameters

- `coder` — The decoder to use during initialization.

- `rootView` — The root view of the SwiftUI view hierarchy that you want to manage using this view controller.

## See Also

### Creating a hosting controller object

- [init(rootView:)](<init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:)](<init(coder_).md>) — Creates a hosting controller object from the contents of the specified archive.
