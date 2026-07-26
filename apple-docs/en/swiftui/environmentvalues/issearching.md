---
title: isSearching
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/issearching
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/issearching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/issearching.json'
content_hash: 'sha256:9a6a64670d7e2a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isSearching

<sub>Instance Property</sub>

A Boolean value that indicates when the user is searching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSearching: Bool { get }
```

## Discussion

You can read this value like any of the other [EnvironmentValues](../environmentvalues.md), by creating a property with the [Environment](../environment.md) property wrapper:

```swift
@Environment(\.isSearching) private var isSearching
```

Get the value to find out when the user interacts with a search field that’s produced by one of the searchable modifiers, like [searchable(text:placement:prompt:)](<../view/searchable(text_placement_prompt_).md>):

```swift
struct SearchingExample: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView()
                .searchable(text: $searchText)
        }
    }
}

struct SearchedView: View {
    @Environment(\.isSearching) private var isSearching

    var body: some View {
        Text(isSearching ? "Searching!" : "Not searching.")
    }
}
```

When the user first taps or clicks in a search field, the `isSearching` property becomes `true`. When the user cancels the search operation, the property becomes `false`. To programmatically set the value to `false` and dismiss the search operation, use [dismissSearch](dismisssearch.md).

> [!important] Important
> Access the value from inside the searched view, as the example above demonstrates, rather than from the searched view’s parent. SwiftUI sets the value in the environment of the view that you apply the searchable modifier to, and doesn’t propagate the value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

- [Managing search interface activation](../managing-search-interface-activation.md) — Programmatically detect and dismiss a search field.
- [dismissSearch](dismisssearch.md) — An action that ends the current search interaction.
- [DismissSearchAction](../dismisssearchaction.md) — An action that can end a search interaction.
- [searchable(text:isPresented:placement:prompt:)](<../view/searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<../view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<../view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<../view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
