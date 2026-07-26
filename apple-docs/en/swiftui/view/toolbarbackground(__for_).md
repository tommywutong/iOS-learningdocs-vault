---
title: 'toolbarBackground(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarbackground(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarbackground(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarbackground%28_%3Afor%3A%29.json'
content_hash: 'sha256:6eb0df60114e8767'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarBackground(_:for:)

<sub>Instance Method</sub>

Specifies the preferred shape style of the background of a bar managed by SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func toolbarBackground<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle

```

## Parameters

- `style` — The style to display as the background of the bar.

- `bars` — The bars to use the style for or [automatic](../toolbarplacement/automatic.md) if empty.

## Discussion

The preferred style flows up to the nearest container that renders a bar. This could be a [NavigationView](../navigationview.md) or [TabView](../tabview.md) in iOS, or the root view of a [WindowGroup](../windowgroup.md) in macOS. This example shows a view that renders the navigation bar with a blue background and dark color scheme.

```swift
NavigationView {
    ContentView()
        .toolbarBackground(.white)
        .toolbarColorScheme(.dark)
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

When used within a [TabView](../tabview.md), the specified style will be preferred while the tab is currently active. You can use a [Group](../group.md) to specify the same preferred background for every tab.

```swift
TabView {
    Group {
        MainView()
        SettingsView()
    }
    .toolbarBackground(.blue, for: .tabBar)
}
```

Depending on the specified bars, the requested style may not be able to be fullfilled.

## See Also

### Styling a toolbar

- [toolbarColorScheme(_:for:)](<toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<../scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](../environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](../toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](../spacersizing.md) — A type which defines how spacers should size themselves.
