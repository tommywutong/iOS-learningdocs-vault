---
title: 'matchedTransitionSource(id:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customizabletoolbarcontent/matchedtransitionsource(id:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/matchedtransitionsource(id:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent/matchedtransitionsource%28id%3Ain%3A%29.json'
content_hash: 'sha256:a9d0657298cd0ee4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomizableToolbarContent](../customizabletoolbarcontent.md)

# matchedTransitionSource(id:in:)

<sub>Instance Method</sub>

Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some CustomizableToolbarContent

```

## Parameters

- `id` — The identifier, often derived from the identifier of the data being displayed by the toolbar content.

- `namespace` — The namespace in which defines the `id`. New namespaces are created by adding an [Namespace](../namespace.md) variable to a [View](../view.md) or ``ToolbarContent` type and reading its value in the type’s body method.

## Discussion

Use this modifier in conjunction with `View.navigationTransition(_:)` to provide a source for the transition effect:

```swift
struct ContentView: View {
    @State private var isPresented = false
    @Namespace private var namespace

    var body: some View {
        NavigationStack {
            DetailView()
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        Button("Show Sheet", systemImage: "globe") {
                            isPresented = true
                        }
                    }
                    .matchedTransitionSource(
                        id: "world", in: namespace)
                }
                .sheet(isPresented: $isPresented) {
                    SheetView()
                        .navigationTransition(
                            .zoom(sourceID: "world", in: namespace))
                }
        }
    }
}
```
