---
title: search
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/submittriggers/search
source_url: 'https://developer.apple.com/documentation/swiftui/submittriggers/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/submittriggers/search.json'
content_hash: 'sha256:b8485cd87a4723eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SubmitTriggers](../submittriggers.md)

# search

<sub>Type Property</sub>

Defines triggers originating from search fields constructed from searchable modifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let search: SubmitTriggers
```

## Discussion

In the example below, only the search field or search completions placed by the searchable modifier will trigger the view model to submit its current search query.

```swift
@StateObject private var viewModel = ViewModel()

NavigationView {
    SidebarView()
    DetailView()
}
.searchable(
    text: $viewModel.searchText,
    placement: .sidebar
) {
    SuggestionsView()
}
.onSubmit(of: .search) {
    viewModel.submitCurrentSearchQuery()
}
```

## See Also

### Getting submit triggers

- [text](text.md) — Defines triggers originating from text input controls like `TextField` and `SecureField`.
