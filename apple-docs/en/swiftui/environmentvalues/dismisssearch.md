---
title: dismissSearch
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/dismisssearch
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/dismisssearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/dismisssearch.json'
content_hash: 'sha256:b9e5e3a5f27717c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# dismissSearch

<sub>Instance Property</sub>

An action that ends the current search interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dismissSearch: DismissSearchAction { get }
```

## Discussion

Use this environment value to get the [DismissSearchAction](../dismisssearchaction.md) instance for the current [Environment](../environment.md). Then call the instance to dismiss the current search interaction. You call the instance directly because it defines a [callAsFunction()](<../dismisssearchaction/callasfunction().md>) method that Swift calls when you call the instance.

When you dismiss search, SwiftUI:

- Sets [isSearching](issearching.md) to `false`.
- Clears any text from the search field.
- Removes focus from the search field.

> [!note] Note
> Calling this instance has no effect if the user isn’t interacting with a search field.

Use this action to dismiss a search operation based on another user interaction. For example, consider a searchable view with a [Button](../button.md) that presents more information about the first matching item from a collection:

```swift
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView(searchText: searchText)
                .searchable(text: $searchText)
        }
    }
}

private struct SearchedView: View {
    let searchText: String

    let items = ["a", "b", "c"]
    var filteredItems: [String] { items.filter { $0 == searchText.lowercased() } }

    @State private var isPresented = false
    @Environment(\.dismissSearch) private var dismissSearch

    var body: some View {
        if let item = filteredItems.first {
            Button("Details about \(item)") {
                isPresented = true
            }
            .sheet(isPresented: $isPresented) {
                NavigationStack {
                    DetailView(item: item, dismissSearch: dismissSearch)
                }
            }
        }
    }
}
```

The button becomes visible only after the user enters search text that produces a match. When the user taps the button, SwiftUI shows a sheet that provides more information about the item, including an Add button for adding the item to a stored list of items:

```swift
private struct DetailView: View {
    var item: String
    var dismissSearch: DismissSearchAction

    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Text("Information about \(item).")
            .toolbar {
                Button("Add") {
                    // Store the item here...

                    dismiss()
                    dismissSearch()
                }
            }
    }
}
```

People can dismiss the sheet by dragging it down, effectively canceling the operation, leaving the in-progress search interaction intact. Alternatively, people can tap the Add button to store the item. Because the person using your app is likely to be done with both the detail view and the search interaction at this point, the button’s closure also uses the [dismiss](dismiss.md) property to dismiss the sheet, and the [dismissSearch](dismisssearch.md) property to reset the search field.

> [!important] Important
> Access the action from inside the searched view, as the example above demonstrates, rather than from the searched view’s parent, or another hierarchy, like that of a sheet. SwiftUI sets the value in the environment of the view that you apply the searchable modifier to, and doesn’t propagate the value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

- [Managing search interface activation](../managing-search-interface-activation.md) — Programmatically detect and dismiss a search field.
- [isSearching](issearching.md) — A Boolean value that indicates when the user is searching.
- [DismissSearchAction](../dismisssearchaction.md) — An action that can end a search interaction.
- [searchable(text:isPresented:placement:prompt:)](<../view/searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<../view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<../view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<../view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
