---
title: isTabViewSidebarAvailable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/istabviewsidebaravailable
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/istabviewsidebaravailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/istabviewsidebaravailable.json'
content_hash: 'sha256:75a60fd8931e74f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isTabViewSidebarAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether a tab sidebar is available within the content of a surrounding [TabView](../tabview.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isTabViewSidebarAvailable: Bool { get }
```

## Discussion

This value is only meaningful inside the content views of a [TabView](../tabview.md) that uses a sidebar-capable style such as [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md). Reading it from a view that is not nested inside a `TabView`’s content — for example, a view above the `TabView` in the hierarchy — returns `false`.

```swift
struct ContentView: View {
    var body: some View {
        TabView {
            Tab("Home", systemImage: "house") {
                HomeTab()
            }
        }
        .tabViewStyle(.sidebarAdaptable)
    }
}

struct HomeTab: View {
    @Environment(\.isTabViewSidebarAvailable)
    private var isTabViewSidebarAvailable

    var body: some View {
        if isTabViewSidebarAvailable {
            // Sidebar is (or can become) visible — adjust UI.
        } else {
            // No sidebar in this context.
        }
    }
}
```

Use this value to gate behaviors or UI that depend on the sidebar’s availability, rather than inspecting size classes directly.
