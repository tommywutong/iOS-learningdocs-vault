---
title: 'init(rootView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/init(rootview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/init(rootview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/init%28rootview%3A%29.json'
content_hash: 'sha256:3d045c442a1ee851'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# init(rootView:)

<sub>Initializer</sub>

Creates a hosting view object that wraps the specified SwiftUI view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency required init(rootView: Content)
```

## Parameters

- `rootView` — The root view of the SwiftUI view hierarchy that you want to manage using this hosting view.

## See Also

### Creating a hosting view

- [init(coder:)](<init(coder_).md>) — Creates a hosting view object from the contents of the specified archive.
- [prepareForReuse()](<prepareforreuse().md>)
