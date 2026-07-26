---
title: 'tabItem(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/tabitem(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabitem%28_%3A%29.json'
content_hash: 'sha256:ec68f07ac7b71dd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabItem(_:)

<sub>Instance Method</sub>

Sets the tab bar item associated with this view.

> [!warning] Deprecated
> Use `Tab(title:image:value:content:)` and related initializers instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func tabItem<V>(@ContentBuilder _ label: () -> V) -> some View where V : View

```

## Parameters

- `label` — The tab bar item to associate with this view.

## Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a [TabView](../tabview.md). The example below adds two views as tabs in a [TabView](../tabview.md):

```swift
struct View1: View {
    var body: some View {
        Text("View 1")
    }
}

struct View2: View {
    var body: some View {
        Text("View 2")
    }
}

struct TabItem: View {
    var body: some View {
        TabView {
            View1()
                .tabItem {
                    Label("Menu", systemImage: "list.dash")
                }

            View2()
                .tabItem {
                    Label("Order", systemImage: "square.and.pencil")
                }
        }
    }
}
```

![A screenshot of a two views configured as tab items in a tab](../../../../attachments/31a47e769ee8bf9c15e5ac357c73020e/SwiftUI-View-tabItem@2x.png)

## See Also

### Deprecated Types

- [NavigationView](../navigationview.md) — A view for presenting a stack of views that represents a visible path in a navigation hierarchy. _(deprecated)_
