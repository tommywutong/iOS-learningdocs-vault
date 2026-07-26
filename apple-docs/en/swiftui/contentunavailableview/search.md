---
title: search
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentunavailableview/search
source_url: 'https://developer.apple.com/documentation/swiftui/contentunavailableview/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentunavailableview/search.json'
content_hash: 'sha256:313dc7399fe40978'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentUnavailableView](../contentunavailableview.md)

# search

<sub>Type Property</sub>

Creates a `ContentUnavailableView` instance that conveys a search state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions> { get }
```

## Discussion

A `ContentUnavailableView` initialized with this static member is expected to be contained within a searchable view hierarchy. Such a configuration enables the search query to be parsed into the view’s description.

For example, consider the usage of this static member in _ContactsListView_:

```swift
struct ContactsListView: View {
    @ObservedObject private var viewModel = ContactsViewModel()

    var body: some View {
        NavigationStack {
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
            .searchable(text: $viewModel.searchText)
            .overlay {
                if searchResults.isEmpty {
                    ContentUnavailableView.search
                }
            }
        }
    }
}
```

## See Also

### Getting built-in unavailable views

- [search(text:)](<search(text_).md>) — Creates a `ContentUnavailableView` instance that conveys a search state.
