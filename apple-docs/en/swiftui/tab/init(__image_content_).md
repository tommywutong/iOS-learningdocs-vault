---
title: 'init(_:image:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(_:image:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(_:image:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28_%3Aimage%3Acontent%3A%29.json'
content_hash: 'sha256:0b2bfd38d63bdeb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates a new tab that you can use in a tab view, with a localized string key label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ titleKey: LocalizedStringKey, image: String, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `titleKey` — The localized string key label for the tab’s tab item.

- `image` — The image for the tab’s tab item.

- `content` — The view content of the tab.

## See Also

### Creating a tab with image

- [init(_:image:value:content:)](<init(__image_value_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
- [init(_:image:role:content:)](<init(__image_role_content_).md>) — Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:role:content:)](<init(__image_value_role_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
