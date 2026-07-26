---
title: largeSubtitle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/largesubtitle
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/largesubtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/largesubtitle.json'
content_hash: 'sha256:dcfeffe084744ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# largeSubtitle

<sub>Type Property</sub>

A placement for items in the navigation bar’s large title subtitle area.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let largeSubtitle: ToolbarItemPlacement
```

## Discussion

The view appears when the navigation bar renders its title out-of-line, and takes precedence over the value provided to the `View.navigationSubtitle(_:)` modifier.

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            DetailView()
                .navigationTitle("Title")
                .navigationSubtitle("Subtitle")
                .toolbar {
                    ToolbarItem(placement: .largeSubtitle) {
                        CustomLargeNavigationSubtitle()
                    }
                }
        }
    }
}
```
