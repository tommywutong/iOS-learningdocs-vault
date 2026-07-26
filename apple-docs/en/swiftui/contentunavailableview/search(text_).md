---
title: 'search(text:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/contentunavailableview/search(text:)'
source_url: 'https://developer.apple.com/documentation/swiftui/contentunavailableview/search(text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentunavailableview/search%28text%3A%29.json'
content_hash: 'sha256:654f8a245649012a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentUnavailableView](../contentunavailableview.md)

# search(text:)

<sub>Type Method</sub>

Creates a `ContentUnavailableView` instance that conveys a search state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func search(text: String) -> ContentUnavailableView<Label, Description, Actions>
```

## Parameters

- `text` — The search text query.

## Discussion

For example, consider the usage of this static member in _ContactsListView_:

```swift
struct ContactsListView: View {
    @ObservedObject private var viewModel = ContactsViewModel()

    var body: some View {
        NavigationStack {
            CustomSearchBar(query: $viewModel.searchText)
            List {
                ForEach(viewModel.searchResults) { contact in
                    NavigationLink {
                        ContactsView(contact)
                    } label: {
                        Text(contact.name)
                    }
                }
            }
            .navigationTitle("Contacts")
            .overlay {
                if viewModel.searchResults.isEmpty {
                    ContentUnavailableView
                        .search(text: viewModel.searchText)
                }
            }
        }
    }
}
```

## See Also

### Getting built-in unavailable views

- [search](search.md) — Creates a `ContentUnavailableView` instance that conveys a search state.
