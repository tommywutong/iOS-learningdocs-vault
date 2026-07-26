---
title: 'init(coder:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/init(coder:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/init%28coder%3A%29.json'
content_hash: 'sha256:c12068399d02e0f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# init(coder:)

<sub>Initializer</sub>

Creates a hosting view object from the contents of the specified archive.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency required dynamic init?(coder aDecoder: NSCoder)
```

## Discussion

The default implementation of this method throws an exception. To create your view from an archive, override this method and initialize the superclass using the [init(coder:rootView:)](<init(coder_rootview_).md>) method instead.

## See Also

### Creating a hosting view

- [init(rootView:)](<init(rootview_).md>) — Creates a hosting view object that wraps the specified SwiftUI view.
- [prepareForReuse()](<prepareforreuse().md>)
