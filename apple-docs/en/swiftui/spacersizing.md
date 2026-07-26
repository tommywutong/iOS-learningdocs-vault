---
title: SpacerSizing
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spacersizing
source_url: 'https://developer.apple.com/documentation/swiftui/spacersizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spacersizing.json'
content_hash: 'sha256:c17394821659a6c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SpacerSizing

<sub>Structure</sub>

A type which defines how spacers should size themselves.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct SpacerSizing
```

## Overview

Use this type in coordination with the [ToolbarSpacer](toolbarspacer.md) type to define if the spacer should be a flexible size, or a fixed size using system-defined sizing rules.

For example, the following adds a fixed-size toolbar spacer between the share and more buttons in the toolbar:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [fixed](spacersizing/fixed.md) — The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.
- [flexible](spacersizing/flexible.md) — The flexible spacer sizing behavior. The spacer will expand to accommodate as much space as it is given in the current context.

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](environmentvalues/toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](toolbarlabelstyle.md) — The label style of a toolbar.
