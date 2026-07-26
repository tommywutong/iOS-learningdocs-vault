---
title: 'searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchable%28text%3Atokens%3Asuggestedtokens%3Aispresented%3Aplacement%3Aprompt%3Atoken%3A%29.json'
content_hash: 'sha256:ed946b36fa529106'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

<sub>Instance Method</sub>

Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable

```

## Parameters

- `text` — The text to display and edit in the search field.

- `tokens` — A collection of tokens to display and edit in the search field.

- `suggestedTokens` — A collection of tokens to display as suggestions.

- `isPresented` — A [Binding](../binding.md) that controls the presented state of search.

- `placement` — The preferred placement of the search field within the containing view hierarchy.

- `prompt` — Text resource for the localized prompt of the search field which provides users with guidance on what to search for.

- `token` — A content builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md). For information about presenting a search field programmatically, see [Managing search interface activation](../managing-search-interface-activation.md).

## See Also

### Detecting, activating, and dismissing search

- [Managing search interface activation](../managing-search-interface-activation.md) — Programmatically detect and dismiss a search field.
- [isSearching](../environmentvalues/issearching.md) — A Boolean value that indicates when the user is searching.
- [dismissSearch](../environmentvalues/dismisssearch.md) — An action that ends the current search interaction.
- [DismissSearchAction](../dismisssearchaction.md) — An action that can end a search interaction.
- [searchable(text:isPresented:placement:prompt:)](<searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<searchable(text_tokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
