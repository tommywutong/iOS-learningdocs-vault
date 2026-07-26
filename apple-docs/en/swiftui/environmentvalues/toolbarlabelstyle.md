---
title: toolbarLabelStyle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/toolbarlabelstyle
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarlabelstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/toolbarlabelstyle.json'
content_hash: 'sha256:f6dc3da9fb2c8e8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# toolbarLabelStyle

<sub>Instance Property</sub>

The label style to apply to controls within a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var toolbarLabelStyle: ToolbarLabelStyle? { get }
```

## Discussion

The default is `nil` for items outside the window toolbar.

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<../view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<../view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<../view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<../scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [ToolbarLabelStyle](../toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](../spacersizing.md) — A type which defines how spacers should size themselves.
