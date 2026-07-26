---
title: 'init(coder:rootView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingcontroller/init(coder:rootview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(coder:rootview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/init%28coder%3Arootview%3A%29.json'
content_hash: 'sha256:0bda1d63d271af82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# init(coder:rootView:)

<sub>Initializer</sub>

Creates a hosting controller object from an archive and the specified SwiftUI view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency init?(coder aDecoder: NSCoder, rootView: Content)
```

## Parameters

- `rootView` — The root view of the SwiftUI view hierarchy that you want to manage using this view controller.

## Return Value

A `UIViewController` object that you can present from your interface.

## See Also

### Creating a hosting controller object

- [init(rootView:)](<init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:)](<init(coder_).md>) — Creates a hosting controller object from the contents of the specified archive.
