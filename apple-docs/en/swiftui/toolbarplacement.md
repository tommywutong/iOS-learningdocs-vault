---
title: ToolbarPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarplacement
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarplacement.json'
content_hash: 'sha256:64162562235d8692'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarPlacement

<sub>Structure</sub>

The placement of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarPlacement
```

## Overview

Use this type in conjunction with modifiers like [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) and [toolbarVisibility(_:for:)](<view/toolbarvisibility(__for_).md>) to customize the appearance of different bars managed by SwiftUI. Not all bars support all types of customizations.

See [ToolbarItemPlacement](toolbaritemplacement.md) to learn about the different regions of these toolbars that you can place your own controls into.

## Topics

### Getting placements

- [automatic](toolbarplacement/automatic.md) — The primary toolbar.
- [accessoryBar(id:)](<toolbarplacement/accessorybar(id_).md>) — Creates a unique accessory bar placement.
- [bottomBar](toolbarplacement/bottombar.md) — The bottom toolbar of an app.
- [bottomOrnament](toolbarplacement/bottomornament.md) — The bottom ornament of an app.
- [navigationBar](toolbarplacement/navigationbar.md) — The navigation bar of an app.
- [tabBar](toolbarplacement/tabbar.md) — The tab bar of an app.
- [windowToolbar](toolbarplacement/windowtoolbar.md) — The placement for the containing window’s toolbar, sometimes referred to as the titlebar.

### Deprecated symbols

- [init(id:)](<toolbarplacement/init(id_).md>) — Creates a custom accessory bar placement. _(deprecated)_

### Type Properties

- [statusBar](toolbarplacement/statusbar.md) — The system status bar. _(beta)_

## See Also

### Setting toolbar visibility

- [toolbar(_:for:)](<view/toolbar(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarVisibility(_:for:)](<view/toolbarvisibility(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](<view/toolbarbackgroundvisibility(__for_).md>) — Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [ContentToolbarPlacement](contenttoolbarplacement.md)
