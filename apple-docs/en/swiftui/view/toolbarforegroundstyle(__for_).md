---
title: 'toolbarForegroundStyle(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/toolbarforegroundstyle(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/toolbarforegroundstyle(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/toolbarforegroundstyle%28_%3Afor%3A%29.json'
content_hash: 'sha256:6a0f3b73a30ae467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# toolbarForegroundStyle(_:for:)

<sub>Instance Method</sub>

Specifies the preferred foreground style of bars managed by SwiftUI.

<sub>watchOS</sub>

```swift
nonisolated func toolbarForegroundStyle<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle

```

## Discussion

This examples shows a view that renders the navigation bar with a blue foreground color.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Blue")
        .toolbarForegroundStyle(
            .blue, for: .navigationBar)
}
```

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [windowToolbarStyle(_:)](<../scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](../environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](../toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](../spacersizing.md) — A type which defines how spacers should size themselves.
