---
title: 'toolbarColorScheme(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarcolorscheme(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarcolorscheme(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarcolorscheme%28_%3Afor%3A%29.json'
content_hash: 'sha256:04fd71ad2cf04829'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarColorScheme(_:for:)

<sub>Instance Method</sub>

Specifies the preferred color scheme of a bar managed by SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarColorScheme(_ colorScheme: ColorScheme?, for bars: ToolbarPlacement...) -> some View

```

## Parameters

- `colorScheme` — The preferred color scheme of the background of the bar.

- `bars` — The bars to update the color scheme of or [automatic](../toolbarplacement/automatic.md) if empty.

## Discussion

The preferred color scheme flows up to the nearest container that renders a bar. This could be a [NavigationView](../navigationview.md) or [TabView](../tabview.md) in iOS, or the root view of a [WindowGroup](../windowgroup.md) in macOS. Pass in a value of nil to match the current system’s color scheme.

This examples shows a view that renders the navigation bar with a blue background and dark color scheme:

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(.blue)
            .toolbarColorScheme(.dark)
    }
    // other tabs...
}
```

You can provide multiple [ToolbarPlacement](../toolbarplacement.md) instances to customize multiple bars at once.

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(
                .blue, for: .navigationBar, .tabBar)
            .toolbarColorScheme(
                .dark, for: .navigationBar, .tabBar)
    }
}
```

Note that the provided color scheme is only respected while a background is visible in the requested bar. As the background becomes visible, the bar transitions from the color scheme of the app to the requested color scheme. You can ensure that the color scheme is always respected by specifying that the background of the bar always be visible.

```swift
NavigationView {
    ContentView()
        .toolbarBackground(.visible)
        .toolbarColorScheme(.dark)
}
```

Depending on the specified bars, the requested color scheme may not be able to be fullfilled.

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<../scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](../environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](../toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](../spacersizing.md) — A type which defines how spacers should size themselves.
