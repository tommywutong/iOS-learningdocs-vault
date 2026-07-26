---
title: 'init(coder:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingcontroller/init(coder:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/init%28coder%3A%29.json'
content_hash: 'sha256:fadc20033e014525'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# init(coder:)

<sub>Initializer</sub>

Creates a hosting controller object from the contents of the specified archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency required dynamic init?(coder aDecoder: NSCoder)
```

## Discussion

The default implementation of this method throws an exception. To create your view controller from an archive, override this method and initialize the superclass using the [init(coder:rootView:)](<init(coder_rootview_).md>) method instead.

-Parameter coder: The decoder to use during initialization.

## See Also

### Creating a hosting controller object

- [init(rootView:)](<init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:rootView:)](<init(coder_rootview_).md>) — Creates a hosting controller object from an archive and the specified SwiftUI view.
