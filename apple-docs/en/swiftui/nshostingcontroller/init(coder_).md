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
doc_path: '/documentation/swiftui/nshostingcontroller/init(coder:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/init%28coder%3A%29.json'
content_hash: 'sha256:4d4e4fc3bc2d51fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# init(coder:)

<sub>Initializer</sub>

Creates a hosting controller object from the contents of the specified archive.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency required dynamic init?(coder: NSCoder)
```

## Parameters

- `coder` — The decoder to use during initialization.

## Discussion

The default implementation of this method throws an exception. To create your view controller from an archive, override this method and initialize the superclass using the [init(coder:rootView:)](<init(coder_rootview_).md>) method instead.

## See Also

### Creating a hosting controller object

- [init(rootView:)](<init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:rootView:)](<init(coder_rootview_).md>) — Creates a hosting controller object from an archive and the specified SwiftUI view.
