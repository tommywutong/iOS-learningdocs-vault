---
title: 'init(_:image:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menubarextra/init(_:image:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menubarextra/init%28_%3Aimage%3Acontent%3A%29.json'
content_hash: 'sha256:9b2cff504355df12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuBarExtra](../menubarextra.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — The localized string resource to use for the accessibility label of the item.

- `image` — The image resource to use as the label.

- `content` — A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with an image

- [init(_:image:isInserted:content:)](<init(__image_isinserted_content_).md>) — Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](<init(__systemimage_isinserted_content_).md>) — Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
