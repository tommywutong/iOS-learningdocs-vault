---
title: 'toolbarVisibility(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarvisibility(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarvisibility(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarvisibility%28_%3Afor%3A%29.json'
content_hash: 'sha256:22809a5219b22871'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarVisibility(_:for:)

<sub>Instance Method</sub>

Specifies the visibility of a bar managed by SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarVisibility(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View

```

## Parameters

- `visibility` — The preferred visibility of the bar.

- `bars` — The bars to update the visibility of or [automatic](../toolbarplacement/automatic.md) if empty.

## Discussion

The preferred visibility flows up to the nearest container that renders a bar. This could be a [NavigationView](../navigationview.md) or [TabView](../tabview.md) in iOS, or the root view of a [WindowGroup](../windowgroup.md) in macOS.

This examples shows a view that hides the navigation bar on iOS, or the window toolbar items on macOS.

```swift
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden)
}
```

To hide the entire titlebar on macOS, use this modifier with [windowToolbar](../toolbarplacement/windowtoolbar.md) placement.

```swift
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden, for: .windowToolbar)
}
```

You can provide multiple [ToolbarPlacement](../toolbarplacement.md) instances to hide multiple bars at once.

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarVisibility(
                .hidden, for: .navigationBar, .tabBar)
    }
}
```

> [!note] Note
> In macOS, if you provide [ToolbarCommands](../toolbarcommands.md) to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not [automatic](../toolbarplacement/automatic.md).

Depending on the specified bars, the requested visibility may not be able to be fulfilled.

## See Also

### Setting toolbar visibility

- [toolbar(_:for:)](<toolbar(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](<toolbarbackgroundvisibility(__for_).md>) — Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [ToolbarPlacement](../toolbarplacement.md) — The placement of a toolbar.
- [ContentToolbarPlacement](../contenttoolbarplacement.md)
