---
title: 'toolbar(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+, watchOS 9.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/toolbar(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbar(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbar%28_%3Afor%3A%29.json'
content_hash: 'sha256:d40b8c570b7bfe6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbar(_:for:)

<sub>Instance Method</sub>

Specifies the visibility of a bar managed by SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbar(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View

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
        .toolbar(.hidden)
}
```

To hide the entire titlebar on macOS, use this modifier with [windowToolbar](../toolbarplacement/windowtoolbar.md) placement.

```swift
NavigationView {
    ContentView()
        .toolbar(.hidden, for: .windowToolbar)
}
```

You can provide multiple [ToolbarPlacement](../toolbarplacement.md) instances to hide multiple bars at once.

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbar(
                .hidden, for: .navigationBar, .tabBar)
    }
}
```

> [!note] Note
> In macOS, if you provide [ToolbarCommands](../toolbarcommands.md) to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not [automatic](../toolbarplacement/automatic.md).

Depending on the specified bars, the requested visibility may not be able to be fulfilled.

## See Also

### Setting toolbar visibility

- [toolbarVisibility(_:for:)](<toolbarvisibility(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](<toolbarbackgroundvisibility(__for_).md>) — Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [ToolbarPlacement](../toolbarplacement.md) — The placement of a toolbar.
- [ContentToolbarPlacement](../contenttoolbarplacement.md)
