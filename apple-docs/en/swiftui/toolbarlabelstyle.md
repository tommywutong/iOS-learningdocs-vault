---
title: ToolbarLabelStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarlabelstyle
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarlabelstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarlabelstyle.json'
content_hash: 'sha256:6d4cefeb058add90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarLabelStyle

<sub>Structure</sub>

The label style of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarLabelStyle
```

## Overview

Use this type in conjunction with modifiers like [windowToolbarLabelStyle(fixed:)](<scene/windowtoolbarlabelstyle(fixed_).md>) and [windowToolbarLabelStyle(_:)](<scene/windowtoolbarlabelstyle(__).md>) to customize the appearance of window toolbars managed by SwiftUI.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](toolbarlabelstyle/automatic.md) — The automatic label style. The toolbar will use a labelStyle that best fits the `Scene` it is applied to.
- [iconOnly](toolbarlabelstyle/icononly.md) — The icon only label style. The toolbar contents will only display the control
- [titleAndIcon](toolbarlabelstyle/titleandicon.md) — The title and icon label style. The toolbar contents will display both a control and title
- [titleOnly](toolbarlabelstyle/titleonly.md) — The title only label style. The toolbar contents will only display the title

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [SpacerSizing](spacersizing.md) — A type which defines how spacers should size themselves.
