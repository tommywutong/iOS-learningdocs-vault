---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusstate/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusstate/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusstate/projectedvalue.json'
content_hash: 'sha256:04968b257986673f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusState](../focusstate.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the focus state value that returns a binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: FocusState<Value>.Binding { get }
```

## Discussion

When focus is outside any view that is bound to this state, the wrapped value is `nil` for optional-typed state or `false` for Boolean state.

In the following example of a simple navigation sidebar, when the user presses the Filter Sidebar Contents button, focus moves to the sidebar’s filter text field. Conversely, if the user moves focus to the sidebar’s filter manually, then the value of `isFiltering` automatically becomes `true`, and the sidebar view updates.

```swift
struct Sidebar: View {
    @State private var filterText = ""
    @FocusState private var isFiltering: Bool

    var body: some View {
        VStack {
            Button("Filter Sidebar Contents") {
                isFiltering = true
            }

            TextField("Filter", text: $filterText)
                .focused($isFiltering)
        }
    }
}
```

## See Also

### Inspecting the focus state

- [Binding](binding.md) — A property wrapper type that can read and write a value that indicates the current focus location.
- [wrappedValue](wrappedvalue.md) — The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
