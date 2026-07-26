---
title: 'init(value:role:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(value:role:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(value:role:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28value%3Arole%3Acontent%3A%29.json'
content_hash: 'sha256:b9cd29b59655786e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(value:role:content:)

<sub>Initializer</sub>

Creates a new tab with a label inferred from the role.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `value` — The `selection` value which selects this tab.

- `role` — The `role` defining the semantic purpose of the tab.

- `content` — The view content of the tab.

## See Also

### Creating a tab

- [init(content:)](<init(content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:content:)](<init(value_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(role:content:)](<init(role_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
