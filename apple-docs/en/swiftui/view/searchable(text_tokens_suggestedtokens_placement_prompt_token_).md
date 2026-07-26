---
title: 'searchable(text:tokens:suggestedTokens:placement:prompt:token:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:placement:prompt:token:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:placement:prompt:token:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchable%28text%3Atokens%3Asuggestedtokens%3Aplacement%3Aprompt%3Atoken%3A%29.json'
content_hash: 'sha256:527949e0e56a0128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

<sub>Instance Method</sub>

Marks this view as searchable with text, tokens, and suggestions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable

```

## Parameters

- `text` — The text to display and edit in the search field.

- `tokens` — A collection of tokens to display and edit in the search field.

- `suggestedTokens` — A collection of tokens to display as suggestions.

- `placement` — The preferred placement of the search field within the containing view hierarchy.

- `prompt` — Text resource for the localized prompt of the search field which provides users with guidance on what to search for.

- `token` — A content builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## See Also

### Making search suggestions

- [Suggesting search terms](../suggesting-search-terms.md) — Provide suggestions to people searching for content in your app.
- [searchSuggestions(_:)](<searchsuggestions(__).md>) — Configures the search suggestions for this view.
- [searchSuggestions(_:for:)](<searchsuggestions(__for_).md>) — Configures how to display search suggestions within this view.
- [searchCompletion(_:)](<searchcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a search suggestion.
- [SearchSuggestionsPlacement](../searchsuggestionsplacement.md) — The ways that SwiftUI displays search suggestions.
