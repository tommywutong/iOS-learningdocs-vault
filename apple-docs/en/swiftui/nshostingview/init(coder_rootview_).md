---
title: 'init(coder:rootView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/init(coder:rootview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/init(coder:rootview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/init%28coder%3Arootview%3A%29.json'
content_hash: 'sha256:0c1097c25839603e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# init(coder:rootView:)

<sub>Initializer</sub>

Creates a hosting view object from an archive and the specified SwiftUI view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency init?(coder: NSCoder, rootView: Content)
```

## Parameters

- `coder` — The decoder to use during initialization.

- `rootView` — The root view of the SwiftUI view hierarchy that you want to manage using this hosting view.
