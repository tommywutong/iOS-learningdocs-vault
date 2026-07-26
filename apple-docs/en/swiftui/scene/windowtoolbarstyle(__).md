---
title: 'windowToolbarStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 11.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowtoolbarstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowtoolbarstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowtoolbarstyle%28_%3A%29.json'
content_hash: 'sha256:eea5b873943ea39f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowToolbarStyle(_:)

<sub>Instance Method</sub>

Sets the style for the toolbar defined within this scene.

<sub>macOS</sub>

```swift
nonisolated func windowToolbarStyle<S>(_ style: S) -> some Scene where S : WindowToolbarStyle

```

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<../view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<../view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<../view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](../environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](../toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](../spacersizing.md) — A type which defines how spacers should size themselves.
