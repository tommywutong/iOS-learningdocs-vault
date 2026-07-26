---
title: 'searchable(text:tokens:placement:prompt:token:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchable%28text%3Atokens%3Aplacement%3Aprompt%3Atoken%3A%29.json'
content_hash: 'sha256:da30e5534f10213a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchable(text:tokens:placement:prompt:token:)

<sub>Instance Method</sub>

Marks this view as searchable with text and tokens.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable

```

## Parameters

- `text` — The text to display and edit in the search field.

- `tokens` — A collection of tokens to display and edit in the search field.

- `placement` — The preferred placement of the search field within the containing view hierarchy.

- `prompt` — Text resource for the localized prompt of the search field which provides users with guidance on what to search for.

- `token` — A content builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## See Also

### Searching your app’s data model

- [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md) — Present an interface that people can use to search for content in your app.
- [Performing a search operation](../performing-a-search-operation.md) — Update search results based on search text and optional tokens that you store.
- [searchable(text:placement:prompt:)](<searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:editableTokens:placement:prompt:token:)](<searchable(text_editabletokens_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [SearchFieldPlacement](../searchfieldplacement.md) — The placement of a search field in a view hierarchy.
