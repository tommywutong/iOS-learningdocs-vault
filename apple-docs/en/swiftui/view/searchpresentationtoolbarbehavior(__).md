---
title: 'searchPresentationToolbarBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.1+, iPadOS 17.1+, Mac Catalyst 17.1+, macOS 14.1+, tvOS 17.1+, visionOS 1.0+, watchOS 10.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchpresentationtoolbarbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchpresentationtoolbarbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchpresentationtoolbarbehavior%28_%3A%29.json'
content_hash: 'sha256:b9f56081bf0e4ed4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchPresentationToolbarBehavior(_:)

<sub>Instance Method</sub>

Configures the search toolbar presentation behavior for any searchable modifiers within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchPresentationToolbarBehavior(_ behavior: SearchPresentationToolbarBehavior) -> some View

```

## Discussion

By default on iOS, a toolbar may hide parts of its content when presenting search to focus on searching. You can override this behavior by providing a value of [avoidHidingContent](../searchpresentationtoolbarbehavior/avoidhidingcontent.md) to this modifer.

```swift
@State private var searchText = ""

List {
    // ... content
}
.searchable(text: $searchText)
.searchPresentationToolbarBehavior(.avoidHidingContent)
```

## See Also

### Displaying toolbar content during search

- [SearchPresentationToolbarBehavior](../searchpresentationtoolbarbehavior.md) — A type that defines how the toolbar behaves when presenting search.
