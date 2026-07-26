---
title: 'searchSelection(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchselection(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchselection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchselection%28_%3A%29.json'
content_hash: 'sha256:8cd613ce2b5c757d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchSelection(_:)

<sub>Instance Method</sub>

Binds the selection of the search field associated with the nearest searchable modifier to the given [TextSelection](../textselection.md) value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func searchSelection(_ selection: Binding<TextSelection?>) -> some View

```

## Parameters

- `selection` — The selection value to bind.

## Discussion

Use this modifier to read and set selection in your search interface. Selection is represented using `TextSelection` where the indices are relative to the search text you provide on the [searchable(text:placement:prompt:)](<searchable(text_placement_prompt_).md>) modifier. Note that this value will not represent selection outside of the text, such as in any leading tokens.

SwiftUI will automatically update this value when the user changes selection, such as by typing. Likewise, you can change selection by writing to this value.

The following example creates a search interface that selects all of the text on focus.

```swift
struct ContentView: View {
    @State var text = "Hello, world!"
    @State var selection: TextSelection?
    @FocusState var focused

    var body: some View {
        NavigationSplitView {
            Sidebar()
                .searchable(text: $text)
                .searchFocused($focused)
                .searchSelection($selection)
        } detail: {
            Detail()
        }
        .onChange(of: focused) {
            if focused {
                selection = TextSelection(
                    range: text.startIndex..<text.endIndex)
            }
        }
    }
}
```

## See Also

### Displaying a search interface

- [searchable(text:placement:prompt:)](<searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:isPresented:placement:prompt:)](<searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchPresentationToolbarBehavior(_:)](<searchpresentationtoolbarbehavior(__).md>) — Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [searchToolbarBehavior(_:)](<searchtoolbarbehavior(__).md>) — Configures the behavior for search in the toolbar.
