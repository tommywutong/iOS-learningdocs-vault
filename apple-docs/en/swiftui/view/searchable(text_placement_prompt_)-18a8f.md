---
title: 'searchable(text:placement:prompt:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchable(text:placement:prompt:)-18a8f'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)-18a8f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchable%28text%3Aplacement%3Aprompt%3A%29-18a8f.json'
content_hash: 'sha256:2a28795ba92ebd9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchable(text:placement:prompt:)

<sub>Instance Method</sub>

Marks this view as searchable, which configures the display of a search field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View

```

## Parameters

- `text` — The text to display and edit in the search field.

- `placement` — The preferred placement of the search field within the containing view hierarchy.

- `prompt` — A [Text](../text.md) view representing the prompt of the search field which provides users with guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).
