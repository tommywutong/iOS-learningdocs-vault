---
title: 'init(value:role:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(value:role:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(value:role:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28value%3Arole%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:241e849c2c626425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(value:role:content:label:)

<sub>Initializer</sub>

Creates a new tab with a label that you can use in a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(value: Value, role: TabRole?, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `value` — The `selection` value which selects this tab.

- `role` — The role defining the semantic purpose of the tab.

- `content` — The view content of the tab.

- `label` — The label for the tab’s tab item.

## See Also

### Creating a tab with label

- [init(content:label:)](<init(content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(value:content:label:)](<init(value_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(role:content:label:)](<init(role_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
