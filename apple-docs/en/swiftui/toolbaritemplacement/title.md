---
title: title
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/title
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/title.json'
content_hash: 'sha256:81a582cd935136c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# title

<sub>Type Property</sub>

A placement for items in the title area of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@export(implementation) static var title: ToolbarItemPlacement { get }
```

## Discussion

The view appears when the navigation bar renders its title inline, and takes precedence over the value provided to the `View.navigationTitle(_:)` modifier.

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            DetailView()
                .navigationTitle("Title")
                .navigationSubtitle("Subtitle")
                .toolbar {
                    ToolbarItem(placement: .title) {
                        CustomNavigationTitle()
                    }
                }
        }
    }
}
```
