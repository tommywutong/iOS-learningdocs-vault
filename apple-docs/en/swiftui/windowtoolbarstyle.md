---
title: WindowToolbarStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowtoolbarstyle
source_url: 'https://developer.apple.com/documentation/swiftui/windowtoolbarstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowtoolbarstyle.json'
content_hash: 'sha256:ecf03e8ad9e685e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowToolbarStyle

<sub>Protocol</sub>

A specification for the appearance and behavior of a window’s toolbar.

<sub>macOS</sub>

```swift
protocol WindowToolbarStyle
```

## Relationships

- **Conforming Types**: [DefaultWindowToolbarStyle](defaultwindowtoolbarstyle.md), [ExpandedWindowToolbarStyle](expandedwindowtoolbarstyle.md), [UnifiedCompactWindowToolbarStyle](unifiedcompactwindowtoolbarstyle.md), [UnifiedWindowToolbarStyle](unifiedwindowtoolbarstyle.md)

## Topics

### Getting built-in window toolbar styles

- [automatic](windowtoolbarstyle/automatic.md) — The automatic window toolbar style.
- [expanded](windowtoolbarstyle/expanded.md) — A window toolbar style which displays its title bar area above the toolbar.
- [unified](windowtoolbarstyle/unified.md) — A window toolbar style which displays its toolbar and title bar inline.
- [unified(showsTitle:)](<windowtoolbarstyle/unified(showstitle_).md>) — A window toolbar style which displays its toolbar and title bar inline.
- [unifiedCompact](windowtoolbarstyle/unifiedcompact.md) — A window toolbar style similar to [unified](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.
- [unifiedCompact(showsTitle:)](<windowtoolbarstyle/unifiedcompact(showstitle_).md>) — A window toolbar style similar to [unified](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.

### Supporting types

- [DefaultWindowToolbarStyle](defaultwindowtoolbarstyle.md) — The default window toolbar style.
- [ExpandedWindowToolbarStyle](expandedwindowtoolbarstyle.md) — A window toolbar style which displays its title bar area above the toolbar.
- [UnifiedWindowToolbarStyle](unifiedwindowtoolbarstyle.md) — A window toolbar style which displays its toolbar and title bar inline.
- [UnifiedCompactWindowToolbarStyle](unifiedcompactwindowtoolbarstyle.md) — A window toolbar style similar to [unified](windowtoolbarstyle/unified.md), but with a more compact vertical sizing.

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [toolbarLabelStyle](environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](toolbarlabelstyle.md) — The label style of a toolbar.
- [SpacerSizing](spacersizing.md) — A type which defines how spacers should size themselves.
