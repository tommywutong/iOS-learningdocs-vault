---
title: 'searchCompletion(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchcompletion(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchcompletion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchcompletion%28_%3A%29.json'
content_hash: 'sha256:1148bf6cac9ecf0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchCompletion(_:)

<sub>Instance Method</sub>

Associates a fully formed string with the value of this view when used as a search suggestion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchCompletion(_ completion: String) -> some View

```

## Parameters

- `completion` — A string to use as the view’s completion.

## Discussion

Use this method to associate a fully formed string with a view that is within a search suggestion list context. The system uses this value when the view is selected to replace the partial text being currently edited of the associated search field.

On tvOS, the string that you provide to the this modifier is used when displaying the associated suggestion and when replacing the partial text of the search field.

```swift
SearchPlaceholderView()
    .searchable(text: $text) {
        Text("🍎").searchCompletion("apple")
        Text("🍐").searchCompletion("pear")
        Text("🍌").searchCompletion("banana")
    }
```

## See Also

### Making search suggestions

- [Suggesting search terms](../suggesting-search-terms.md) — Provide suggestions to people searching for content in your app.
- [searchSuggestions(_:)](<searchsuggestions(__).md>) — Configures the search suggestions for this view.
- [searchSuggestions(_:for:)](<searchsuggestions(__for_).md>) — Configures how to display search suggestions within this view.
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions.
- [SearchSuggestionsPlacement](../searchsuggestionsplacement.md) — The ways that SwiftUI displays search suggestions.
