---
title: 'init(value:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(value:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(value:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28value%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:bb010ba09d89fd5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(value:content:label:)

<sub>Initializer</sub>

Creates a new tab with a label that you can use in a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(value: Value, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `value` — The `selection` value which selects this tab.

- `content` — The view content of the tab.

- `label` — The label for the tab’s tab item.

## See Also

### Creating a tab with label

- [init(content:label:)](<init(content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(role:content:label:)](<init(role_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](<init(value_role_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
