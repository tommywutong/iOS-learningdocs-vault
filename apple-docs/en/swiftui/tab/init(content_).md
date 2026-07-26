---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28content%3A%29.json'
content_hash: 'sha256:aaad5f94cf7e8320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(content:)

<sub>Initializer</sub>

Creates a new tab that you can use in a tab view, with an empty label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@ContentBuilder content: () -> Content) where Label == EmptyView
```

## Parameters

- `content` — The view content of the tab.

## See Also

### Creating a tab

- [init(value:content:)](<init(value_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(role:content:)](<init(role_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](<init(value_role_content_).md>) — Creates a new tab with a label inferred from the role.
