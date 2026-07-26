---
title: 'init(selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabview/init(selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabview/init(selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabview/init%28selection%3Acontent%3A%29.json'
content_hash: 'sha256:374e7c63a0a17143'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabView](../tabview.md)

# init(selection:content:)

<sub>Initializer</sub>

Creates a tab view that uses a builder to create and specify selection values for its tabs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<C>(selection: Binding<SelectionValue>, @TabContentBuilder<SelectionValue> content: () -> C) where Content == TabContentBuilder<SelectionValue>.Content<C>, C : TabContent
```

## Parameters

- `selection` — The selection in the TabView. The value of this binding must match the `value` of the tabs in `content`.

- `content` — The [Tab](../tab.md) content.

## See Also

### Creating a tab view

- [init(content:)](<init(content_).md>)
