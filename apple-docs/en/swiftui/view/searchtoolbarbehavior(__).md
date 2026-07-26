---
title: 'searchToolbarBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchtoolbarbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchtoolbarbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchtoolbarbehavior%28_%3A%29.json'
content_hash: 'sha256:2c710e9441ad574d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchToolbarBehavior(_:)

<sub>Instance Method</sub>

Configures the behavior for search in the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func searchToolbarBehavior(_ behavior: SearchToolbarBehavior) -> some View

```

## Discussion

This modifier can be used to change the default behavior of a search field that appears in the toolbar. Place this modifier after the [searchable(text:isPresented:placement:prompt:)](<searchable(text_ispresented_placement_prompt_).md>) modifier that renders search in the toolbar.

On iPhone, the search field in the bottom toolbar can be configured to appear as a button-like control when inactive:

```swift
@State private var searchText = ""

NavigationStack {
    RecipeList()
        .searchable($searchText)
        .searchToolbarBehavior(.minimized)
}
```

## See Also

### Displaying a search interface

- [searchable(text:placement:prompt:)](<searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:isPresented:placement:prompt:)](<searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchPresentationToolbarBehavior(_:)](<searchpresentationtoolbarbehavior(__).md>) — Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [searchSelection(_:)](<searchselection(__).md>) — Binds the selection of the search field associated with the nearest searchable modifier to the given [TextSelection](../textselection.md) value.
