---
title: 'searchSuggestions(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchsuggestions(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchsuggestions(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchsuggestions%28_%3Afor%3A%29.json'
content_hash: 'sha256:1e6301e3eb075456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchSuggestions(_:for:)

<sub>Instance Method</sub>

Configures how to display search suggestions within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchSuggestions(_ visibility: Visibility, for placements: SearchSuggestionsPlacement.Set) -> some View

```

## Parameters

- `visibility` — The visibility of the search suggestions for the specified locations.

- `placements` — The set of locations in which to set the visibility of search suggestions.

## Discussion

SwiftUI presents search suggestions differently depending on several factors, like the platform, the position of the search field, and the size class. Use this modifier when you want to only display suggestions in certain ways under certain conditions. For example, you might choose to display suggestions in a menu when possible, but directly filter your data source otherwise.

```swift
enum FruitSuggestion: String, Identifiable {
    case apple, banana, orange
    var id: Self { self }
}

@State private var text = ""
@State private var suggestions: [FruitSuggestion] = []

var body: some View {
    MainContent()
        .searchable(text: $text) {
            ForEach(suggestions) { suggestion
                Text(suggestion.rawValue)
                    .searchCompletion(suggestion.rawValue)
            }
            .searchSuggestions(.hidden, for: .content)
        }
}
```

## See Also

### Making search suggestions

- [Suggesting search terms](../suggesting-search-terms.md) — Provide suggestions to people searching for content in your app.
- [searchSuggestions(_:)](<searchsuggestions(__).md>) — Configures the search suggestions for this view.
- [searchCompletion(_:)](<searchcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a search suggestion.
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions.
- [SearchSuggestionsPlacement](../searchsuggestionsplacement.md) — The ways that SwiftUI displays search suggestions.
