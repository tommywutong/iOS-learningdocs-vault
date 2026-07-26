---
title: 'searchable(text:placement:prompt:suggestions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（27.0 起废弃）, iPadOS 15.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, tvOS 15.0+（27.0 起废弃）, visionOS 1.0+, watchOS 8.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/searchable(text:placement:prompt:suggestions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:suggestions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchable%28text%3Aplacement%3Aprompt%3Asuggestions%3A%29.json'
content_hash: 'sha256:e583cb448022ca29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchable(text:placement:prompt:suggestions:)

<sub>Instance Method</sub>

Marks this view as searchable, which configures the display of a search field.

> [!warning] Deprecated
> Use the searchable modifier with the searchSuggestions modifier

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ContentBuilder suggestions: () -> S) -> some View where S : View

```

## Parameters

- `text` — The text to display and edit in the search field.

- `placement` — Where the search field should attempt to be placed based on the containing view hierarchy.

- `prompt` — A key for the localized prompt of the search field which provides users with guidance on what to search for.

- `suggestions` — A content builder that produces content that populates a list of suggestions.

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).
